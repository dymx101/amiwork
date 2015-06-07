#from socialscoreupdater import SocialScoreUpdater

from .scrapers.opengraphsharescraper import OpenGraphShareScraper
from databaseinterface.databaseinterface import DatabaseInterface
from localconfig import LocalConfig
import math,time


#from mockfileregistry import MockFileRegistry as MFR

class SocialScoreUpdater:
	'''	-----------Constants-------------- '''
	story_chunk_size = LocalConfig.socialscoreupdater_story_chunk_size			#DB transactions Process 1000 stories in a single go
	treshold_normalized_score =  LocalConfig.socialscoreupdater_treshold_normalized_score				# 1.5 = Top 14% if it followed normal distribution ; 1 = 34%
	treshold_age = LocalConfig.socialscoreupdater_treshold_age					# 2 days
	life_factor = LocalConfig.socialscoreupdater_life_factor					# 
	stat_update_upper = LocalConfig.socialscoreupdater_stat_update_upper		# Should be close enough to give enough importance to the existing stats
	stat_update_lower = LocalConfig.socialscoreupdater_stat_update_lower		# Should be big enough to not be swayed by a day of fame
	
	''' -----------Nested Classes--------------- '''
	class SocialScoreStory:
		def __init__(self,story_id,url,feed_id,previous_score=None,total_shares=None,last_updated=None,created=None,normalized_score=None):
			self.story_id = story_id
			self.url = url
			self.feed_id = feed_id
			#self.feed = feed
			
			self.normalized_score = normalized_score
			self.previous_raw_score = previous_score
			self.updated_raw_score = None
			self.total_shares = total_shares
			
			self.last_updated = last_updated
			
			self.created = created
		
		def __repr__(self):
			return vars(self).__repr__()
	
	'''	-------------------------------- '''
	
	''' Static methods  that aren't related to the update '''
	@staticmethod
	def add_new_story(story_id):
		''' Adds a story to both the active and global set. Responsible for the part that gives newer statistics higher weightages '''
		dbi = DatabaseInterface.get_shared_instance()
		dbi.autocommit(False)
		dbi.execute("INSERT INTO news_social_score_all ( story_id, created ) (SELECT story_id,created FROM news_stories WHERE story_id=%s)",(story_id,))
		dbi.execute("INSERT INTO news_social_score_active ( normalized_score, story_id, raw_score ) (SELECT 0,story_id,0 FROM news_stories WHERE story_id=%s)", (story_id,))
		cursor = dbi.execute("SELECT feed_id,sum_x,sum_x2,feed_n FROM news_social_score_feed_statistics JOIN news_stories USING(feed_id) WHERE story_id=%s", (story_id,) )

		if cursor.rowcount>0:
			row = cursor.fetchone()
			feed_id=row['feed_id']
			new_n = row['feed_n'] + 1
			new_x = row['sum_x']
			new_x2 = row['sum_x2']
			
			if new_n > SocialScoreUpdater.stat_update_upper:	
				'''THIS CAN ACTUALLY HAPPEN DESPITE ME NOT INCREMENTING FEED_N. feed_n < stat_update_upper IS NOT AN INVARIANT! 
				feed_n is incremented when a story is added to the set'''
				scale = (float(stat_update_lower)/new_n)
				new_n = stat_update_lower #(stat_update_lower/new_n)	* new_n
				new_x =  scale * new_x
				new_x2 = scale * new_x2
				dbi.execute("UPDATE news_social_score_feed_statistics SET sum_x=%s, sum_x2=%s, feed_n=%s WHERE feed_id=%s", (new_x,new_x2,new_n,feed_id))
			else:
				dbi.execute("UPDATE news_social_score_feed_statistics SET feed_n=feed_n+1 WHERE feed_id = %s",(feed_id,) )
		
		dbi.commit()
		dbi.autocommit(True)
		
	
	''' ----------------Member methods -------------------- '''
	def __init__(self,update_all=False):
		''' Set update_all=True if you want to query the whole set. If you just want to query the active set, update_all=False '''
		self.update_all = update_all		#Update everything or just the active set?
		self._feed_statistics = None
	
	def prepare_update(self):
		dbi = DatabaseInterface.get_shared_instance()
		dbi.execute('TRUNCATE news_social_score_update',None)
		last_retrieved_id = 0
		dbi.autocommit(False)
		if self.update_all:
			''' Tested. Seems to work. '''
			rowcount = 1
			while rowcount>0:
				cursor = dbi.execute("\
					INSERT INTO news_social_score_update (story_id,last_update,old_raw_score,total_shares,created,state) \
					( SELECT story_id,last_update,raw_score,total_shares,created,'READY' FROM news_social_score_all \
						WHERE story_id>( SELECT IFNULL(MAX(story_id), 0) FROM news_social_score_update ) LIMIT %s)",(SocialScoreUpdater.story_chunk_size,))
				rowcount = cursor.rowcount
				#print rowcount
				dbi.commit()
			#dbi.execute("INSERT INTO news_social_score_update (story_id,last_update,old_raw_score,total_shares,state) ( SELECT story_id,last_update,raw_score,total_shares,'READY' FROM news_social_score_all) ",None)
			
		else:
			''' Tested. Seems to work. '''
			''' Would the below query affect select queries on the active set? I don't need a write lock so it shouldn't '''
			''' The active set is assumed to be small enough for the mysql server to handle by itself. '''
			dbi.execute("INSERT INTO news_social_score_update (story_id,old_raw_score,state) ( SELECT story_id,raw_score,'READY' FROM news_social_score_active) ",None)
			dbi.execute("\
				UPDATE news_social_score_update JOIN news_social_score_all USING(story_id) SET\
				news_social_score_update.total_shares = news_social_score_all.total_shares,\
				news_social_score_update.last_update=news_social_score_all.last_update, \
				news_social_score_update.created=news_social_score_all.created\
				",None
			)
			dbi.commit()
		
		dbi.autocommit(True)
	
	
	
	def update_scores(self):	#Do it in chunks of story_chunk_size
		''' Computes and updates the fields new_raw_score,normalized_score, last_updated, total_shares, state in news_social_score_updated, <story_chunk_size> stories at a time '''
		dbi = DatabaseInterface.get_shared_instance()
		dbi.autocommit(False)
		
		self._load_feed_statistics()
		#print self._feed_statistics
		
		row_count = 1
		while row_count>0 :	
			cursor = dbi.execute("\
				SELECT story_id, feed_id, news_social_score_update.created, url, old_raw_score, total_shares, last_update FROM\
				news_social_score_update JOIN news_stories USING(story_id)\
				WHERE news_social_score_update.state='READY' LIMIT %s",
				(SocialScoreUpdater.story_chunk_size,)
			) #OMG A JOIN!
			if cursor.rowcount==0:
				break
			rowcount = cursor.rowcount
	
			stories = list()
			urls = list()
			for row in cursor.fetchall():
				stories.append( SocialScoreUpdater.SocialScoreStory(row['story_id'],row['url'],row['feed_id'],row['old_raw_score'],row['total_shares'],row['last_update']) ) #story_id,url,feed_id,previous_score=None,last_updated=None,
				urls.append( row['url'] )
			
			#Get the score from Facebook's opengraph
			ogscraper = OpenGraphShareScraper()
			ogscraper.set_urls( urls )
			ogscraper.update_og_shares()
			og_shares = ogscraper.get_result()
			
			#Compute the new scores for each and update in DB ( But commit all at once )
			time_now = int(time.time())
			for story in stories:
				if story.url not in og_shares:
					new_total_shares = 0			#Nothing we can do. facebook has no records of it
				else:
					new_total_shares = og_shares[story.url]
				shares_since = new_total_shares - story.total_shares
				story.total_shares = new_total_shares
				story_id = story.story_id 
				story.updated_raw_score = self._compute_updated_raw_score(story,shares_since,time_now)
				story.normalized_score = self._normalize_across_feeds(story.updated_raw_score,story.feed_id)
				
				query_params = ( story.updated_raw_score, story.total_shares,time_now, story.normalized_score, story.story_id )
				
				dbi.execute("UPDATE news_social_score_update SET new_raw_score=%s , total_shares=%s, last_update=%s, new_normalized_score=%s,state='SCORE_COMPUTED' WHERE story_id=%s",query_params )
				
			dbi.commit()
		
		dbi.autocommit(True)
		''' Even this seems to work correctly. Efficiency i have no idea :p '''
	
	
	def build_new_active_set(self):
		''' Creates a new active set ( news_social_score_active table), and populates it with updated data. 
		rotate_active_set can be called to bring this new active set into use '''
		dbi = DatabaseInterface.get_shared_instance()
		
		dbi.execute("DROP TABLE IF EXISTS news_social_score_active_new",None)	#Creates a new table
		dbi.execute("CREATE TABLE news_social_score_active_new SELECT * FROM news_social_score_active LIMIT 0",None)	#Creates a new table
		
		dbi.autocommit(False)
		
		''' Add the highest scored articles into the new active set '''
		rowcount = 1
		while  rowcount > 0:
			cursor = dbi.execute("UPDATE news_social_score_update SET state='ABOVE_TRESHOLD'  WHERE new_normalized_score > %s AND state='SCORE_COMPUTED' ORDER BY new_normalized_score DESC LIMIT %s", (SocialScoreUpdater.treshold_normalized_score, SocialScoreUpdater.story_chunk_size) )
			rowcount = cursor.rowcount
			if rowcount==0:
				break
			dbi.execute("\
				INSERT INTO news_social_score_active_new (normalized_score, story_id, raw_score ) \
				( SELECT new_normalized_score,story_id,new_raw_score FROM news_social_score_update WHERE state='ABOVE_TRESHOLD' ORDER BY new_normalized_score DESC)\
				", None)
			dbi.execute("UPDATE news_social_score_update SET state='CONSIDERED_IN_SET' WHERE state='ABOVE_TRESHOLD'",None)
			dbi.commit()
		
		#Get those that lie below the treshold but are young enough to stay
		treshold_created_time = int(time.time()) - SocialScoreUpdater.treshold_age
		rowcount = 1
		
		while rowcount > 0:
			cursor = dbi.execute("UPDATE news_social_score_update SET state='ABOVE_TRESHOLD' WHERE created > %s AND state='SCORE_COMPUTED' LIMIT %s", (treshold_created_time,SocialScoreUpdater.story_chunk_size) )
			rowcount = cursor.rowcount
			if rowcount==0:
				break
			
			dbi.execute("\
				INSERT INTO news_social_score_active_new (normalized_score, story_id, raw_score ) \
				( SELECT new_normalized_score,story_id,new_raw_score FROM news_social_score_update WHERE state='ABOVE_TRESHOLD' ORDER BY new_normalized_score DESC)\
				", None)
			dbi.execute("UPDATE news_social_score_update SET state='CONSIDERED_IN_SET' WHERE state='ABOVE_TRESHOLD'",None)
			dbi.commit()
		
		#Update the rest
		rowcount = 1
		while rowcount > 0:
			cursor = dbi.execute("UPDATE news_social_score_update SET state='CONSIDERED_IN_SET' WHERE state='SCORE_COMPUTED' LIMIT %s", (SocialScoreUpdater.story_chunk_size,) )
			rowcount = cursor.rowcount
			dbi.commit()
		
		dbi.commit()
		dbi.autocommit(True)
	
	def rotate_active_set(self):
		''' Swaps in the newly built active set table by renaming the old one to news_social_score_active_old and the new one to news_social_score_active '''
		dbi = DatabaseInterface.get_shared_instance()
		dbi.autocommit(False)
		dbi.execute("DROP TABLE IF EXISTS news_social_score_active_old",None)	#Let's keep this just incase
		dbi.execute("RENAME TABLE news_social_score_active TO news_social_score_active_old, news_social_score_active_new TO news_social_score_active",None)
		dbi.commit()
		dbi.autocommit(True)
	
	def update_permanent_scores(self):
		''' Updates news_social_score_all, which is the main database. news_social_score_active is just a cache of the active set '''
		dbi = DatabaseInterface.get_shared_instance()
		rowcount=1
		while rowcount > 0:
			cursor = dbi.execute("\
				UPDATE  ( SELECT story_id FROM news_social_score_update WHERE state='CONSIDERED_IN_SET' LIMIT %s)t_dummy JOIN news_social_score_update t_ud JOIN news_social_score_all t_all\
				ON t_dummy.story_id = t_ud.story_id  AND t_dummy.story_id=t_all.story_id SET\
				t_all.reflected_in_stats = IF( (t_ud.new_raw_score  > t_all.peak_score AND t_all.reflected_in_stats='UPTODATE'),'OUTDATED',t_all.reflected_in_stats) , \
				t_ud.state='UPDATED_STORIES', t_all.total_shares=t_ud.total_shares, t_all.raw_score = t_ud.new_raw_score,\
				t_all.prev_peak_score = t_all.peak_score, t_all.peak_score=GREATEST(t_all.peak_score, t_ud.new_raw_score), t_all.last_update = t_ud.last_update \
				", (SocialScoreUpdater.story_chunk_size,) )
			rowcount = cursor.rowcount
			dbi.commit()
	
	
	''' I shall write a doc on this and upload it. There are weird preconditions'''
	def update_statistics(self):
		''' PRECONDITION: 
			All stories in news_social_score_all must be accounted for in feed_n. ie, Even when they were at 0-0 score. 
			Yes, it makes a small difference to the std_deviation but the simplification in code is worth the negligible loss of precision. If you find a better way, pls implement
			NOT AN INVARIANT:
				feed_n is less than stat_update_upper. 
			Also remember,
				Std_dev(x) = E[X^2] - E[X]
			
		'''
		dbi = DatabaseInterface.get_shared_instance()
		rowcount=1
		#Let's use some python here.
		cursor = dbi.execute("SELECT feed_id,peak_score,prev_peak_score,reflected_in_stats FROM news_social_score_all JOIN news_stories USING(story_id) WHERE reflected_in_stats!='UPTODATE'",None)
		rows = cursor.fetchall()
		peak_scores = dict()
		added_x = dict()
		added_x2 = dict()
		new_insertions=dict()
		for row in rows:
			feed_id = row['feed_id']
			peak_score = row['peak_score']
			prev_peak_score = row['prev_peak_score']
			if feed_id not in added_x:
				added_x[feed_id] = 0
				added_x2[feed_id] = 0
			added_x[feed_id] += peak_score - prev_peak_score
			added_x2[feed_id] += (peak_score*peak_score) - (prev_peak_score*prev_peak_score)
			
			if row['reflected_in_stats']=='NEVER':
				if feed_id not in new_insertions:
					new_insertions[feed_id] = 0
				new_insertions[feed_id] += 1
			
		
		
		#Let's get stats for each feed
		dbi.autocommit(False)
		for feed_id in new_insertions:
			insert_values = (feed_id,new_insertions[feed_id],new_insertions[feed_id])
			dbi.execute("INSERT INTO news_social_score_feed_statistics (feed_id,feed_n) VALUES(%s,%s) ON DUPLICATE KEY UPDATE feed_n=feed_n+%s", insert_values)
		for feed_id in added_x:
			update_params = (added_x[feed_id], added_x2[feed_id], feed_id)
			dbi.execute('UPDATE news_social_score_feed_statistics SET sum_x=sum_x+%s,sum_x2=sum_x2+%s WHERE feed_id=%s', update_params)
			
		dbi.execute("UPDATE news_social_score_all SET reflected_in_stats='UPTODATE' WHERE reflected_in_stats!='UPTODATE'",None)
		dbi.commit()
		dbi.autocommit(True)
		
		
	
	
	def _load_feed_statistics(self):
		''' Loads the average_peak_score and std_deviation of all feeds from the database.
			Stores them as a tuple (average_peak_score,std_deviation) in self._feed_statistics
			Also computes self._feed_statistics[0] as the (global average_peak_score, global std_deviation ) 
				WHERE global std_deviation  = (std_dev_sum/no_of_feeds) * global average_peak_score			( DESPITE THE GLOBAL BEING COMPUTABLE. If you did it properly, You'd have retarded standard deviation )
			Also remember,
				Std_dev(x) = E[X^2] - E[X]
			'''
		self._feed_statistics = dict()
		dbi = DatabaseInterface.get_shared_instance()
		dbcursor = dbi.execute("SELECT feed_id, sum_x,sum_x2,feed_n FROM news_social_score_feed_statistics",None)
		avg_sum = float(0)
		std_dev_sum = float(0)
		i = 0
		for row in dbcursor.fetchall():
			E_x = float(row['sum_x'])/row['feed_n']
			E_x2 = float(row['sum_x2'])/row['feed_n']
			std_dev = math.sqrt(E_x2 - (E_x*E_x))
			
			self._feed_statistics[row["feed_id"]] = (E_x,std_dev )
			avg_sum += E_x
			std_dev_sum += (float(std_dev)/max(1,E_x))
			i+=1
		if i==0:
			i=1
		avg_avg = avg_sum / i
		avg_std_dev = (std_dev_sum/i) * avg_avg
		if avg_std_dev == 0:
			avg_std_dev = 1
		self._feed_statistics[0] = ( avg_avg, avg_std_dev ) #If you hadn't figured it out by now, This is bullshit :p
		
		
	''' -----------------------------------------------
		---			Score computation functions 	---
		----------------------------------------------- ''' 
	
	def _compute_updated_raw_score(self,social_story, shares_since, time_now):
		return self._compute_raw_score(
			social_story.previous_raw_score,
			shares_since,
			(time_now- social_story.last_updated),
			SocialScoreUpdater.life_factor
		)
	
	
	def _compute_raw_score(self, old_score, shares_since,  time_elapsed, life_factor):
		''' computes the updated score with the time decay '''	
		''' ---------------------------------------------------------------------------------------------------------------------------------- '''
		def _pseudo_exponential_decay_score(initial_score,time_elapsed,life_factor):	
			''' Computes the score using the formula 
					initial_score * ( 1 - (time_elapsed/life_factor) ) + shares_since
				If there are no shares added and the updates are regular enough,  This approximates to :
					Score = initial_score * ( 1 - interval/life_factor)^(time/interval)
				
				( Try plotting	100*(1-0.2)^x	on google. You should get something similar )
			'''
			#print initial_score, ( 1 - float(time_elapsed)/life_factor)
			return (initial_score * ( 1 - float(time_elapsed)/life_factor))  - 1	# Not the formula i promised? It is if you update often enough.
		''' ---------------------------------------------------------------------------------------------------------------------------------- '''	
		return shares_since + max(0,_pseudo_exponential_decay_score(old_score,time_elapsed,life_factor))		# The -1 is important so that we never stagnate
	

	def _normalize_across_feeds(self,score,feed_id):
		''' returns the standard_score of the content. feed_id is the feed that the article belongs to.
			Standard score = ( this.deviation / this.field.std_deviation )
				 WHERE [ this.deviation = (this.value - this.feed.mean) ] '''
		feed_avg,feed_std_dev = self._get_feed_statistics(feed_id)
		if feed_std_dev == 0:
			feed_std_dev = 1	#Can't risk a divide by 0 killing my script
			
		return (score - feed_avg)/feed_std_dev
	
	def _get_feed_statistics(self,feed_id):
		''' returns average_peak_score,std_deviation of the feed_id passed. 
		If we have no stats for the passed feed_ids, the global average is passed '''
		if self._feed_statistics is None:
			self._load_feed_statistics()
			
		stats = self._feed_statistics[0]	#Not much we can do, return global stats
		return stats[0], stats[1]
	