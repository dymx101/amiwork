import math
class FrequencySorter:
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
		self.combined_frequency = None
	
	
	#Editable functions based on your model
	
	def compute_scores(self):
		frequency = self._normalize_frequencies(self.combined_frequency)
		self.score = self._compute_scores(self.recommendations,self.relevant_fields,self.importance,self.combined_frequency)
	
	def _compute_score(self,item,attributes,frequency):
		""" Computes the score of a certain item based purely on it's frequency :| """
		score = 0
		print getattr(item,"title")
		for attr in attributes:
			#Cardinality based scoring.
			#print "\t",attr,getattr(item,attr), math.log( 1 + float(frequency[attr][getattr(item,attr)]) * len(frequency[attr]) )
			#score+= math.log( 1 + float(frequency[attr][getattr(item,attr)]) * len(frequency[attr]) )	#Multiplication is to prevent fields with less cardinality dominate
			
			#Normalized scoring
			print "\t",attr,getattr(item,attr), frequency[attr][getattr(item,attr)]
			score += frequency[attr][getattr(item,attr)]
			
		print score
		return score
		
	
	def _normalize_frequencies(self,frequency):
		scale_to = 1
		max_val = 0
		min_val = 0
		for attr in frequency:
			max_val = 0
			for val in frequency[attr]:
				if frequency[attr][val] > max_val:
					max_val = frequency[attr][val] #+0 #Ok, passed by value, I guess
					
			for val in frequency[attr]:
				frequency[attr][val] = float(frequency[attr][val])/(max_val - min_val)
			
		return frequency
		
	
	#Your access to working functions
	def count_frequencies(self):
		self.playlist_frequency = self._count_frequencies(self.playlist, self.relevant_fields)
		self.recommendation_frequency = self._count_frequencies(self.recommendations, self.relevant_fields)
		self.combined_frequency = dict()
		
		for field in self.playlist_frequency:
			self.combined_frequency[field] = dict()
			for attr in self.playlist_frequency[field]:
				self.combined_frequency[field][attr] = self.playlist_frequency[field][attr]
			
		for field in self.recommendation_frequency:
			for attr in self.recommendation_frequency[field]:
				if attr not in self.combined_frequency[field]:
					self.combined_frequency[field][attr] = 0
				self.combined_frequency[field][attr] += self.recommendation_frequency[field][attr]
			
		
	
	

	
	
	
	#Below this, there's nothing interesting.
	
	def set_relevant_fields(self,fields ):
		self.relevant_fields = fields
	
	def set_user_playlist(self,playlist):
		""" Takes a list of items ( of type Song ) in playlist. Stores them in self.playlist"""
		self.playlist = playlist
		
	
	
	def set_recommendations(self, recommendations):
		""" Takes a list of items ( of type Song ) in recommendations . Stores them in self.recommendations """
		self.recommendations = recommendations 
	
	
	
	
	
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
	
	
	
