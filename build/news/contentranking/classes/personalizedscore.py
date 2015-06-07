from databaseinterface.databaseinterface import DatabaseInterface
from usercategoryinterests import UserCategoryInterests
from news.models.newsstory import NewsStory									#This line isn't needed in python but i'm leaving it here anyway
from math import sqrt,log as ln

class PersonalizedScore:
	def __init__(self):
		pass
	
	def set_data(self,content,interests):
		self.content = content		#List of type NewsStory
		self.interests = interests
		#self._scale_interests()
		
	def personalize_scores(self):
		'''-----------------------------------------'''
		def A(X,Ic):
			return -X + sqrt( (X**2) + 2*ln(Ic) )
		'''-----------------------------------------'''	
		for content in self.content:
			overall_interest = self._compute_overall_interest(content.categories)
			content.score += A( content.score ,  overall_interest )
		
	
	def _compute_overall_interest(self,categories):
		''' REVISE THIS! IT IS SILLY! '''
		max_interest = 1
		for category in categories:
			max_interest = max( max_interest, self.interests[category], )
		return max_interest
	
