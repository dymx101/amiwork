from databaseinterface.databaseinterface import DatabaseInterface
from usercategoryinterests import UserCategoryInterests
from news.models.newsstory import NewsStory									#This line isn't needed in python but i'm leaving it here anyway
#from news.contentranking.classes.localconfig import LocalConfig 
from .localconfig import LocalConfig 
from math import sqrt,log as log,log as ln


class PersonalizedScore:
	personalization_scale_point = LocalConfig.personalization_scale_point
	personalization_scale_how_many = LocalConfig.personalization_scale_how_many
	#feed_size_factor_log_base = LocalConfig.personalization_feed_size_factor_log_base
	
	def __init__(self):
		self.content = None 		#List of type NewsStory
		self.interests = None
		self._feed_sizes = None
	
	def set_data(self,content,interests):
		self.content = content		#List of type NewsStory
		self.interests = interests
		self._compute_feed_sizes()
	
	def personalize_scores(self):
		'''-----------------------------------------'''
		def K(feed_size,interest):
			scale_point = float(self.personalization_scale_point)
			how_many = float(self.personalization_scale_how_many)
			desired_ratio = float(1)#float(overall_interest)
			#print feed_size, 1- (		(ln(desired_ratio*std_size/feed_size) / float(self.interest_ratio_x)) 	)	
			
			return 		-(ln(desired_ratio*how_many/feed_size) / float(scale_point))
		
		def size_factor(feed_n):
			base = self.feed_size_factor_log_base
			return log(max(base, feed_n),base)
		'''-----------------------------------------'''
		
		for content in self.content:
			feed_size = self._feed_sizes[content.feed_id]
			
			overall_interest = self._compute_overall_interest(content.categories)
			
			content.score /= K(feed_size,overall_interest)
		
	"""	
	def personalize_scores(self):
		'''-----------------------------------------'''
		def A(X,Ic):
			if X<0:
				X *= -1
			return -X + sqrt( (X**2) + 2*ln(Ic) )
		'''-----------------------------------------'''	
		for content in self.content:
			overall_interest = self._compute_overall_interest(content.categories)
			content.score += A( content.score ,  overall_interest )
		
	"""
	def _compute_overall_interest(self,categories):
		''' REVISE THIS! IT IS SILLY! '''
		max_interest = 1
		for category in categories:
			max_interest = max( max_interest, self.interests[category], )
		return max_interest
	
	def _compute_feed_sizes(self):
		self._feed_sizes = dict()
		for content in self.content:
			feed_id = content.feed_id
			if feed_id not in self._feed_sizes:
				self._feed_sizes[feed_id] = 0
			self._feed_sizes[feed_id]+=1
			
	