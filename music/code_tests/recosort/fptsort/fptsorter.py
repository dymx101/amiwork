class FPTSorter:
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
	def build_tree(self):
		self.fpt = FPTree()
		fpt = self.fpt
		fpt.set_transactions(transactions)
		fpt.compute_L()
		fpt.construct_tree()
		
	
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
	
	def _compute_scores(self,items,attributes,importance,frequency):
		""" Computes the scores of all recommended songs """
		self.score = dict()
		for item in items:
			self.score[item] = self._compute_score(item,attributes,frequency)
		
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
	
		
	
	def score(self,item):
		""" Returns score of the item as computed """
		return self.score[item]
	
	
	
	#Editable functions based on your model
	def _compute_score(self,item,attributes,frequency):
		""" Computes the score of a certain item based purely on it's frequency :| """
		score = 0
		for attr in attributes:
			score+= float(frequency[attr][getattr(item,attr)]) / len(frequency[attr])	#Division is to prevent fields with less cardinality dominate
			#score+= frequency[attr][getattr(item,attr)]
		return score
		
	
