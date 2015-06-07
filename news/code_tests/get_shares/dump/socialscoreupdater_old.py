''' ADD DAILY UPDATES ON FULL SET! '''
#from socialscoreupdater import SocialScoreUpdater

from opengraphsharescraper import OpenGraphShareScraper
from mockfileregistry import MockFileRegistry as MFR
from socialscorekeeper import SocialScoreKeeper			#For the nested class
from databaseinterface import DatabaseInterface
import time

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
	treshold_score_coefficient = 1		#What percent of the average can it be before we prune it?
	treshold_age = 172800				# 2 days
	life_factor = 86400 				# 
	SocialScoreStory = SocialScoreKeeper.SocialScoreStory	#The nested class
	
	''' -------------------------------- '''
	
	def __init__(self,update_all=False):
		self.scores = None				#Dict of the form 
		self.previous_scores= None 		#For rotation
		self.social_score_stories = None	# dict of type SocialScoreStory
		self._feed_statistics = None
		self.new_raw_scores = None		#Used to store what OG gives us
		self.update_all = update_all
	
	""" # This isn't the intended use for this class anymore since we're using DBs. 
	def get_score(self, url):
		''' returns the last fetched score of the item. Does not do an asynchronous doing asynchronous requests to og'''
		if storyid in self.scores:
			return self.scores[url]
		else:
			return 0
	
	
	def add_url(self, url):	#This function should be moved to the SocialScore class where you get to query
		''' Adds a url to the database of links to update ( and to memory if we're doing it ). Will be updated only in the next fetch '''
		self.urls.append(url)
		#And Make the change permanent by adding to DB
	"""
	
	def _prepare_set(self):
		dbi = DatabaseInterface.get_shared_instance()
		dbi.execute("TRUNCATE news_social_score_update",None)
		if self.update_all:
			dbi.execute("INSERT INTO news_social_score_update( ) ( SELECT * FROM news_social_score_all LIMIT )")
		else:
			dbi.execute("INSERT INTO news_social_score_update( SELECT * FROM news_social_score_active LIMIT ")
		#self._mock_load_from_db()
		
	
	def update_scores(self):
		og = OpenGraphShareScraper()
		ogscraper = OpenGraphShareScraper()
		ogscraper.set_urls( self.social_score_stories.keys() )
		ogscraper.update_og_shares()
		self.new_raw_scores = ogscraper.get_result()
		
		# Now compute the updated scores 
		time_now = int(time.time())
		for link in self.social_score_stories:
			self._compute_updated_score( self.social_score_stories[link],time_now )
		
		#time_now = int(time.time())
		#self._prune_unpopular(self.SocialScoreUpdater)
		
		self._update_db_scores()
	
	
	def _compute_updated_score(self,social_story,time_now):
		social_story.updated_raw_score = self.new_raw_scores[social_story.url]
		social_story.updated_raw_score = self._compute_raw_score(
			social_story.updated_raw_score,
			social_story.previous_raw_score,
			(time_now- social_story.last_updated),
			SocialScoreUpdater.life_factor
		)
		social_story.normalized_score = self._normalize_across_feeds( social_story.updated_raw_score, social_story.feed )
		social_story.last_updated = time_now
		return social_story.normalized_score
	
	
	def _update_db_scores(self):
		#DO A MASSIVE TRUNCATE + BATCH INSERT HERE
		#If you're using databases as your primary source of scores ( which makes sense when the project is young, tbh ), Do a rotate.
		#There will be stories added to the old table during this time. Copy them to the new table as is and let them be updated in the next scrape
		#dbi.autocommit(False)
		
		#dbi.autocommit(True)
		#For now, I just write to a file as mock
		self._mock_update_db_scores()
		
	
	
	def _prune_unpopular(self, treshold , min_life,time_now):
		''' Prunes all items below the treshold in self.scores'''
		raise NotImplementedError("_prune_unpopular has yet to be tested")
		for url in self.social_score_stories:
			item = self.social_score_stories[url]
			
			if ( item < treshold_normalized_score) and ( (time_now-item.created) > min_life ):
				del( self.scores[url] ) 
				del( self.social_score_stories[url] )
		
	
	
	def _compute_raw_score(self, new_score, old_score, time_elapsed, life_factor):
		''' computes the updated score with the time decay '''
		return (new_score - old_score) + min(0,self._pseudo_exponential_decay_score(old_score,time_elapsed,life_factor))
		
	
	def _pseudo_exponential_decay_score(self,initial_score,time_elapsed,life_factor):	
		''' Computes the score approximating to the formula ( if there were no votes added )
				initial_score * ( 1 - (time_since_last_update/life_factor) )
			For updates which are small enough, This approximates to :
				Score = initial_score * ( 1 - interval/life_factor)^(time/interval)
			
			Try plotting	100*(1-0.2)^x	on google. You should get something similar
			If it has score=current_score, and the time at which current_score score was calculated is last_updated
			( Remember to prune so that we don't keep irrelevant stuff in db forever )
			
		'''
		return initial_score * ( 1 - time_elapsed/life_factor)	# Not the formula i promised? It is if you update often enough.
	
	def _normalize_across_feeds(self,score,feed):
		''' Pick one?
				Standard score = this.deviation / this.field_std_deviation ; Where [ this.deviation = (this.value - this.mean) ]
		'''
		feed_avg,feed_std_dev = self._get_feed_statistics(feed)
		return (score - feed_avg)/feed_std_dev
	
	
	def _load_feed_statistics(self):
		self._feed_statistics = dict()
		#return self._mock_load_feed_statistics()
		dbi = DatabaseInterface.get_shared_instance()
		dbcursor = dbi.execute("SELECT feed_id, average_peak_score, std_deviation FROM news_social_score_feed_statistics",None)
		for row in dbcursor.fetchall():
			self._feed_statistics[row["feed_id"]] = (row["average_peak_score"],row["std_deviation"] )
		#raise NotImplementedError("You have not implemented _load_feed_statistics")
		#Load from database
	
	def _get_feed_statistics(self,feed_id):
		'''if feed not in self._feed_statistics:
			stats = self._feed_statistics['global']
		else:
			stats = self._feed_statistics[feed]
		'''
		stats = self._feed_statistics[feed_id]
		return stats[0], stats[1]
	
	
	
	
	
	
	''' Mock methods to help testing '''
	def _mock_load_feed_statistics(self):
		f = open(MFR.feed_stats)
		lines = f.read().split("\n")
		f.close()
		self._feed_statistics= dict()
		for line in lines:
			if not line:
				continue
			fields = line.split("\t")
			self._feed_statistics[fields[0]] = ( float(fields[1]),float(fields[2]))
	
	def _mock_load_from_db(self):
		f = open(MFR.db_read[MFR.iter_number])
		lines = f.read().split("\n")
		f.close()
		self.social_score_stories = dict()
		i=0
		for line in lines:
			if not line:
				continue
			i+=1
			fields = line.split("\t")
			self.social_score_stories[fields[1]] = SocialScoreUpdater.SocialScoreStory( i,fields[1], fields[0],int(fields[2]),int(fields[3]),int(fields[4]) )
		return self.social_score_stories
	
	def _mock_update_db_scores(self):
		out_db = open(MFR.db_out[MFR.iter_number],'w')
		for link in self.social_score_stories:
			item = self.social_score_stories[link]
			new_record = "%s\t%s\t%s\t%s\t%s\t%s"%(item.feed,item.url,item.updated_raw_score, item.last_updated, item.created,item.normalized_score)
			out_db.write( new_record + "\n" )
		out_db.close()
	
		
'''
Table schema i need:
	news_social_score
		normalized_score ( float )
		story_id ( For internal purposes.  )
		url 	( To query open graph by ) #Would this be multivalued if we cluster stories?
		last_udpate ( timestamp to calculate decaying score )
		score	( The current raw score of the story. Not the decayed one )
		peak_score
		
		PRIMARY KEY: normalized_score, story_id. This should give you efficient sequential access.
		
	news_social_score_feed_statistics
		feed 
		content_count	# Good idea would be to remove this and assume count to give a constant weigt ( such as 10* #items_per_feed ) so that it gets updated with changes in popularity of the feed. Else the std_dev messes up as well
		average_peak_score	# It's the average of the maximum scores achieved by each content object
		std_deviation
'''