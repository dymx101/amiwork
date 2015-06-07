
class SimpleWeightedSorter:
	""" Sorter that relies on frequency of occurences in playlist and recommendations to sort """
	#Generic functions
	def __init__(self):
		self.playlist = None 			#list()
		self.recommendations = None		#list()
		self.playlist_frequency = None 		#dict()
		self.recommendation_frequency = None 		#dict()
		self.sorted = None				#list()
		self.relevant_fields = None
		self.importance = None			#dict()		# self.importance = None ._.
	
	def set_relevant_fields(self,fields ):
		self.relevant_fields = fields
	
	def set_user_playlist(self,playlist):
		""" Takes a list of items ( of type Song ) in playlist. Stores them in self.playlist"""
		self.playlist = playlist
		
	
	
	def set_recommendations(self, recommendations):
		""" Takes a list of items ( of type Song ) in recommendations . Stores them in self.recommendations """
		self.recommendations = recommendations 
	
	
	
	#Your access to working functions
	def count_frequencies(self):
		self.playlist_frequency = self._count_frequencies(self.playlist, self.relevant_fields)
		self.recommendation_frequency = self._count_frequencies(self.recommendations, self.relevant_fields)
		
	
	def compute_importances(self):
		self.importance = self._compute_importances(self.relevant_fields)
		
	
	def compute_scores(self):
		self.score = self._compute_scores(self.recommendations,self.relevant_fields,self.importance,self.recommendation_frequency)
		
	
	
	
	#Working functions
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
	
	
	def _compute_importances(self,attributes):
		""" Computes the relative importances of all relevant fields ( Relative to the most important one )"""
		importance = dict()
		sum_importance = 0
		for attribute in attributes:
			importance[attribute] = self._compute_importance(attribute,self.playlist_frequency)	#importance is calculated based on playlist frequency
			sum_importance += importance[attribute]
		
		#Scale them down?
		for attribute in importance:
			importance[attribute] = importance[attribute]/sum_importance
			
		return importance
	
	
	def _compute_scores(self,items,attributes,importance,frequency):
		""" Computes the scores of all recommended songs """
		self.score = dict()
		for item in items:
			self.score[item] = self._compute_score(item,attributes,importance,frequency)
		
		return self.score
		
	
	
	def score_comparator(self,x,y):
		""" comparator for the sorting function. Compares the score of 2 songs """
		if self.score[x] < self.score[y]:
			return -1
		elif self.score[x] == self.score[y]:
			return 0
		else:
			return 1
	
	
	def sort(self):
		""" Sorts recommendations based on their score """
		self.sorted = sorted(self.recommendations, cmp=self.score_comparator, reverse=True)
		return self.sorted
	
	
	# Get functions, for if you're interested
	def playlist_frequency(self,attribute,value):
		""" returns the frequency of the 'value' in attribute ( the #of times the attribute 'attribute' takes up the value 'value' ) in the playlist """
		return self.frequencies[attribute][value]
	
	
	def recommendation_frequency(self,attribute,value):
		""" returns the frequency of the 'value' in attribute ( the #of times the attribute 'attribute' takes up the value 'value' ) in the recommendations """
		return self.frequencies[attribute][value]
	
	
	def importance(self, attribute):
		""" Returns importance of the attribute to the user as computed"""
		return self.importance[attribute]
		
	
	def score(self,item):
		""" Returns score of the item as computed """
		return self.score[item]
	
	
	
	#Editable functions based on your model
	
	def _clumping_function(self,f):
		return f**1.3
		
	
	
	def _compute_importance(self, attribute,frequencies):
		""" Computes importance of a certain attribute given the frequencies of the attributes in the user's playlist """
		#For now, We'll just find SUM(x^1.5/)/SUM(X)
		sum = 0
		sample_size = 0
		for g in frequencies[attribute]:
			sample_size += frequencies[attribute][g]
		
		cardinality = len(frequencies[attribute])
		expectation = sample_size / cardinality	# (size of dataset)/(#distinct values of attribute ) ( assumed equally likely though it's not )
		
		
		for g in frequencies[attribute]:
			sum += self._clumping_function(frequencies[attribute][g]/expectation)
			
		return sum / cardinality 
	
	
	def _compute_score(self,item,attributes,importance,frequency):
		""" Computes the score of a certain item """
		base_score = 1	#Change this?
		score = 0
		
		for attr in attributes:
			#score += base_score * (importance[attr]+1) * (frequency[attr][getattr(item,attr)]+1)
			score += base_score * (importance[attr]+1) * ( (frequency[attr][getattr(item,attr)]+1))
			#score += base_score * importance[attr] * frequency[attr][getattr(item,attr)]
		return score
		
	
