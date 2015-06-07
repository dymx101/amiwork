class SocialScoreKeeper:
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
	
	def __init__(self):
		self.social_score_stories = None	# dict of type SocialScoreStory
		
	def get_score(self, url):
		''' returns the last fetched score of the item. Does not do an asynchronous doing asynchronous requests to og'''
		#Do a DB query and return
		pass
	
	
	def add_url(self, url):	#This function should be moved to the SocialScore class where you get to query
		''' Adds a url to the database of links to update ( and to memory if we're doing it ). Will be updated only in the next fetch '''
		#Add the url to the db
	