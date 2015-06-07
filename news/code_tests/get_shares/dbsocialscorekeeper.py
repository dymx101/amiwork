#from socialscorekeeper import SocialScoreKeeper
from opengraphsharecraper import OpenGraphShareScraper

'''
	Scope for improvement:
		- Do a rotate so that a request always works with the same set of scores. Doesn't get updated halfway.
		- Keep a counter for each link that gets a score request. If a link exceeds a treshold, Do an asynchronous request to facebook to update the score 
'''
class DBSocialScoreKeeper:
	'''	-------------------------------- '''
	class StoryId_Url:
		def __init__(self,storyid,url):
			self.storyid = storyid
			self.url = url
		
	'''	-------------------------------- '''
	
	def __init__(self):
		self.scores = None				#Dict of the form 
		self.previous_scores= None 		#For rotation
		self.urls = None		#Tuples of the form (storyId,url)
	
	
	def get_score(self, url):
		''' returns the last fetched score of the item. Does not do an asynchronous doing asynchronous requests to og'''
		if storyid in self.scores:
			return self.scores[url]
		else
			return 0
		
	
	def add_url(self, url):
		''' Adds a url to the list of scores. Will be updated only in the next fetch '''
		self.urls.append(url)
	
	def _update_scores(self):
		og = OpenGraphShareScraper()
		ogscraper = OpenGraphShareScraper()
		ogscraper.set_content(self.story_url_pairs)
		ogscraper.update_og_shares()
		self.scores = ogscraper.get_result()
		
		self._store_db()
	
	def _store_db():
		#DO MASSIVE BATCH INSERT HERE
		pass
	
	def _prune_unpopular(self):
		#Do this before the mass batch insert
		pass
	
	