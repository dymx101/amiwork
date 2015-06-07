
class NewsStory:
	''' Model for a news story '''
	def __init__(self,story_id,url, title,subtitle,feed_id,created,image,categories,score=None):
		self.story_id = story_id
		self.url = url
		self.title = title
		self.subtitle = subtitle
		self.feed_id = feed_id
		self.created = created
		self.image = image
		self.categories = categories
		self.score = score	
	
	def __repr__(self):
		return vars(self).__repr__()
