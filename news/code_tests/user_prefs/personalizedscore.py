from databaseinterface import DatabaseInterface
from usercategoryinterests import UserCategoryInterests

class PersonalizedScore:
	def __init__(self):
		pass
	
	def set_data(self,content,interests):
		self.content = content
		self.interests = interests
		self._scale_ineterests(interests)
		
	def personalize_scores(self):
		'''-----------------------------------------'''
		def A(X,Ic):
			return -X + sqrt( (X**2) + 2*ln(Ic) )
		'''-----------------------------------------'''	
		for content in self.content:
			overall_interest = self._compute_overall_interest(content.categories)
			content.score += A( X ,  overall_interest )
		
	
	def _scale_interests(self):
		min_interest = min(self.interests, key=self.interests.get)
		for category in self.interests:
			self.interests[category] /= float(min_interest)
			
	
	def _compute_overall_interest(self,categories):
		''' REVISE THIS! IT IS SILLY! '''
		return max(categories, self.interests.get)
		
	
