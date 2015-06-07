#from socialscoreupdater import SocialScoreUpdater

from opengraphsharescraper import OpenGraphShareScraper
from socialscorekeeper import SocialScoreKeeper			#For the nested class
from databaseinterface import DatabaseInterface
import math,time


from mockfileregistry import MockFileRegistry as MFR


'''
	Scope for improvement:
		- Do a rotate so that a request always works with the same set of scores. Doesn't get updated halfway.
			= If you're using DBs, You'll definitely need to do a rotate :|
		- Keep a counter for each link that gets a score request. If a link exceeds a treshold, Do an asynchronous request to facebook to update the score 
'''
class SocialScoreUpdater:
	'''	-------------------------------- '''
	# 		Constants
	story_chunk_size = 5000				#DB transactions Process 1000 stories in a single go
	treshold_normalized_score	=  1.5	# 1.5 = Top 14% if it followed normal distribution ; 1 = 34%
	treshold_age = 172800				# 2 days
	life_factor = 86400 				# 
	stat_update_upper = 6000			# Should be close enough to give enough importance to the existing stats
	stat_update_lower = 5000			# Should be big enough to not be swayed by a day of fame
	SocialScoreStory = SocialScoreKeeper.SocialScoreStory	#The nested class
	
	''' -------------------------------- '''
	''' Static methods  that aren't related to the update '''
	@staticmethod
	def add_new_story(story_id):
		''' Adds a story to both the active and global set '''
		dbi = DatabaseInterface.get_shared_instance()
		dbi.autocommit(False)
		dbi.execute("INSERT INTO news_social_score_all ( story_id, created ) (SELECT story_id,created FROM news_stories WHERE story_id=%s)",(story_id,))
		dbi.execute("INSERT INTO news_social_score_active ( normalized_score, story_id, raw_score ) (SELECT 0,story_id,0 FROM news_stories WHERE story_id=%s)", (story_id,))
		dbi.commit()
		dbi.autocommit(True)
		
	
	def __init__(self,update_all=False):
		self.scores = None				#Dict of the form 
		self.previous_scores= None 		#For rotation
		self.social_score_stories = None	# dict of type SocialScoreStory
		self._feed_statistics = None
		self.new_raw_scores = None		#Used to store what OG gives us
		self.update_all = update_all
	
	
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
		dbi = DatabaseInterface.get_shared_instance()
		#No read
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
		#Swap the tables by renaming
		dbi = DatabaseInterface.get_shared_instance()
		dbi.autocommit(False)
		dbi.execute("DROP TABLE IF EXISTS news_social_score_active_old",None)	#Let's keep this just incase
		dbi.execute("RENAME TABLE news_social_score_active TO news_social_score_active_old, news_social_score_active_new TO news_social_score_active",None)
		dbi.commit()
		dbi.autocommit(True)
	
	def update_permanent_scores(self):
		dbi = DatabaseInterface.get_shared_instance()
		rowcount=1
		while rowcount > 0:
			cursor = dbi.execute("\
				UPDATE  ( SELECT story_id FROM news_social_score_update WHERE state='CONSIDERED_IN_SET' LIMIT %s)t_dummy JOIN news_social_score_update t_ud JOIN news_social_score_all t_all\
				ON t_dummy.story_id = t_ud.story_id  AND t_dummy.story_id=t_all.story_id SET\
				t_all.reflected_in_stats = IF( (t_ud.new_raw_score  > t_all.peak_score),0,t_all.reflected_in_stats) , \
				t_ud.state='UPDATED_STORIES', t_all.total_shares=t_ud.total_shares, t_all.raw_score = t_ud.new_raw_score,\
				t_all.peak_score=GREATEST(t_all.peak_score, t_ud.new_raw_score), t_all.last_update = t_ud.last_update \
				", (SocialScoreUpdater.story_chunk_size,) )
			rowcount = cursor.rowcount
			dbi.commit()
		
	
	def update_statistics(self):
		dbi = DatabaseInterface.get_shared_instance()
		rowcount=1
		#Let's use some python here.
		cursor = dbi.execute("SELECT feed_id,peak_score FROM news_social_score_all JOIN news_stories USING(story_id) WHERE reflected_in_stats='0'",None)
		rows = cursor.fetchall()
		peak_scores = dict()
		for row in rows:
			if row['feed_id'] not in peak_scores:
				peak_scores[row['feed_id']] = [ row['peak_score'] ]
			else:
				peak_scores[row['feed_id']].append(row['peak_score'])
		
		#Let's get stats for each feed
		cursor = dbi.execute("SELECT feed_id,feed_n,average_peak_score,std_deviation FROM news_social_score_feed_statistics",None)
		rows = cursor.fetchall()
		stats= dict()
		for row in rows:
			stats[row['feed_id']] = row
		
		#Now we compute stuff one by one
		dbi.autocommit(False)
		
		for feed_id in peak_scores:
			sum = 0
			squares = 0	#Sum of squares
			for pscore in peak_scores[feed_id]:
				sum += pscore
				squares += pscore * pscore
			
			''' Std_dev(x) = E[X^2] - E[X] '''
			
			added_n = len(peak_scores[feed_id])
			added_sum = sum
			added_squares = squares												# I STILL HAVE TO SUBTRACT THE MEAN
			
			stat = stats[feed_id]
			existing_n = stat['feed_n']
			existing_avg = stat['average_peak_score']
			existing_sum = existing_n * existing_avg
			
			existing_variance = (stat['std_deviation'] * stat['std_deviation']) 	#Actually, it's variance * n
			existing_squares= (existing_variance + (existing_avg*existing_avg)) * existing_n
			
			
			new_avg = float(added_sum + existing_sum ) / max(1,(added_n + existing_n))
			new_squares = added_squares + existing_squares
			
			new_variance = new_squares/(existing_n+added_n) - (new_avg*new_avg)
			new_std_dev = math.sqrt( new_variance )
			
			
			new_n = existing_n + added_n
			#Now we want to be able to adapt to the changing popularity of feeds. We'll reduce the weights of ancient stats so that they don't keep us down.
			if new_n > SocialScoreUpdater.stat_update_upper:
				new_n = stat_update_lower
			update_params = (new_avg,new_std_dev,new_n,feed_id)
			dbi.execute('UPDATE news_social_score_feed_statistics SET average_peak_score=%s, std_deviation=%s,feed_n=%s WHERE feed_id=%s', update_params)
			''' Whaaaaaaat? What did i just do? 
			I need a way for it to quickly adapt to changes in popularity of the site. 
			So i don't take the actual average of everything. I give some extra weight to more recent scores'''
			
		dbi.execute("UPDATE news_social_score_all SET reflected_in_stats='1' WHERE reflected_in_stats='0'",None)
		dbi.commit()
		dbi.autocommit(True)
		
	
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
			''' Computes the score approximating to the formula ( if there were no votes added )
					initial_score * ( 1 - (time_since_last_update/life_factor) )
				For updates which are small enough, This approximates to :
					Score = initial_score * ( 1 - interval/life_factor)^(time/interval)
				
				Try plotting	100*(1-0.2)^x	on google. You should get something similar
				If it has score=current_score, and the time at which current_score score was calculated is last_updated
				( Remember to prune so that we don't keep irrelevant stuff in db forever )
				
			'''
			#print initial_score, ( 1 - float(time_elapsed)/life_factor)
			return (initial_score * ( 1 - float(time_elapsed)/life_factor))  - 1	# Not the formula i promised? It is if you update often enough.
		''' ---------------------------------------------------------------------------------------------------------------------------------- '''	
		return shares_since + max(0,_pseudo_exponential_decay_score(old_score,time_elapsed,life_factor))		# The -1 is important so that we never stagnate
	

	def _normalize_across_feeds(self,score,feed_id):
		''' Standard score = this.deviation / this.field_std_deviation ; Where [ this.deviation = (this.value - this.mean) ] '''
		feed_avg,feed_std_dev = self._get_feed_statistics(feed_id)
		if feed_std_dev == 0:
			feed_std_dev = 1	#Can't risk a divide by 0 killing my script
			
		return (score - feed_avg)/feed_std_dev
	
	
	
	def _load_feed_statistics(self):
		self._feed_statistics = dict()
		#return self._mock_load_feed_statistics()
		dbi = DatabaseInterface.get_shared_instance()
		dbcursor = dbi.execute("SELECT feed_id, average_peak_score, std_deviation FROM news_social_score_feed_statistics",None)
		avg_sum = float(0)
		std_dev_sum = float(0)
		i = 0
		for row in dbcursor.fetchall():
			self._feed_statistics[row["feed_id"]] = (row["average_peak_score"],row["std_deviation"] )
			avg_sum += row["average_peak_score"]
			std_dev_sum += (float(row["std_deviation"])/max(1,row["average_peak_score"]))
			i+=1
		if i==0:
			i=1
		avg_avg = avg_sum / i
		avg_std_dev = (std_dev_sum/i) * avg_avg
		if avg_std_dev == 0:
			avg_std_dev = 1
		self._feed_statistics[0] = ( avg_avg, avg_std_dev ) #If you hadn't figured it out by now, This is bullshit :p
		
	
	def _get_feed_statistics(self,feed_id):
		'''if feed not in self._feed_statistics:
			stats = self._feed_statistics['global']
		else:
			stats = self._feed_statistics[feed]
		'''
		if self._feed_statistics is None:
			self._load_feed_statistics()
			
		if feed_id not in self._feed_statistics:
			self._dynamically_add_feed_id_to_statistics(feed_id)
		
		stats = self._feed_statistics[feed_id]
		return stats[0], stats[1]
	
	
	def _dynamically_add_feed_id_to_statistics(self,feed_id):
		dbi = DatabaseInterface.get_shared_instance()
		if self._feed_statistics is None:
			self._load_feed_statistics()
		global_average_peak_score = self._feed_statistics[0][0]
		global_average_std_deviation = self._feed_statistics[0][1]
		dbi.execute(
			"INSERT INTO news_social_score_feed_statistics (feed_id, average_peak_score, std_deviation, feed_n) VALUES( %s,%s,%s,%s)", 
			(feed_id, global_average_peak_score, global_average_std_deviation, 0) 
		)
		dbi.commit()
		
		self._feed_statistics[feed_id] = (global_average_peak_score,global_average_std_deviation)
		