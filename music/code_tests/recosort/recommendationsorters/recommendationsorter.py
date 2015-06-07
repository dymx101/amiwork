class RecommendationSorter:
	""" This class serves as an interface for my dirty sorters """
	#Generic functions
	def __init__(self):
		self.playlist = None 			#list()
		self.recommendations = None		#list()
		self.frequencies = None 		#dict()
		self.sorted = None				#list()
	
	
	def set_user_playlist(self,playlist):
		""" Takes a list of items in playlist. Stores them in self.playlist"""
		self.playlist = playlist
	
	
	
	def set_recomendations(self, recommendations):
		""" Takes a list of items in recommendations . Stores them in self.recommendations """
		self.recommendations = recommendations 
	
	
	
	
	#Working functions
	def count_frequencies(self):
		self.playlist_frequencies = self._count_frequencies(self.playlist, self.relevant_fields)
		self.recommendation_frequencies = self._count_frequencies(self.recommendations, self.relevant_fields)
		
	
	def _count_frequencies(self,dataset,fields):
		""" Counts the frequencies of the fields in the data set. Returns a dictionary {x: frequency(x) } """
		frequencies = dict()
		for field in fields:
			frequencies[field] = dict()
			for item in dataset:
				val = getattr(item,field)
				if val not in frequencies[field]: #if not frequencies[field][val]:
					frequencies[field][val] = 0
				
				frequencies[field][val] += 1
		return frequencies	
	
	def score_comparator(x,y):
		""" comparator for the sorting function. Compares the score of 2 songs """
		return self.score[x.key] - self.score[y.key]
	
	
	def sort(self):
		""" Sorts recommendations based on their score """
		self.sorted = sorted(self.recommendations, cmp=score_comparator, reverse=True)
	
	
	
	#Editable functions based on your model
	def frequency(self,attribute,value):
		""" returns the frequency of the 'value' in attribute ( the #of times the attribute 'attribute' takes up the value 'value' ) """
	
	def importance(self, g):
		""" Computes importance of a certain attribute given the frequencies of the attributes in the user's playlist """
		
	
	
	
	def score(self,item):
		""" Computes the score of a certain item """
	
	