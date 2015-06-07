from recommendationsorters.ftree import FTree

class TwoPassFTSorter:
	""" Sorter that relies on frequency of occurences in playlist and recommendations to sort """
	#Generic functions
	def __init__(self):
		self.playlist = None 			#list()
		self.recommendations = None		#list()
		self.sorted = None				#list()
		self.relevant_fields = None
		
		self.user_ftree = None
		self.stat_dict = None
		
	
		
	#Editable functions based on your model
	def _compute_score(self,item,fields):
		""" Computes the score of a certain item. = n-tuple score * (n-1)-tuple score """
		
		score = (self.user_ftree.get_subset_frequency(item,[],fields) + 1)
		for field in fields:	
			score += ( self.user_ftree.get_subset_frequency( item,[field],fields) ) #+ 1 )	#Normalized approach
			score += ( self.user_ftree.get_subset_frequency( item,[field],fields) ) #+ 1 )	#Cardinality based approach
			#score *= ( self.user_ftree.get_subset_frequency( item,[field],fields) + 1 )
		
		return score
	
	
	def build_user_ftree(self):
		self.user_ftree = FTree()
		self.user_ftree.set_items(self.playlist+self.recommendations)
		self.user_ftree.set_fields(self.relevant_fields)
		self.user_ftree.build()	
		
	
	
	
	def compute_scores(self,fields=None):
		#First pass on n-tuples
		if fields is None:
			fields = self.relevant_fields
		self.score = self._compute_scores(self.recommendations,fields)
		#Second pass on (n-1) tuples
		
	
	def set_relevant_fields(self,fields ):
		self.relevant_fields = fields
	
	def set_user_playlist(self,playlist):
		""" Takes a list of items ( of type Song ) in playlist. Stores them in self.playlist"""
		self.playlist = playlist
		
	
	def set_recommendations(self, recommendations):
		""" Takes a list of items ( of type Song ) in recommendations . Stores them in self.recommendations """
		self.recommendations = recommendations 
		
	
	
	def stats(self, key, subkey=None):
		if self.stat_dict is None:
			#Load stats
			self.stat_dict = dict()
			self.stat_dict["max_combos"] = float(8)#(8000)	#20 genres, 20 moods, 20 tempos assumed. Do it from a database query when we have data
			field_frequency = dict()
			for field in self.relevant_fields:
				field_frequency[field] = dict()
			
			for item in self.playlist:
				for field in self.relevant_fields:
					val =getattr(item,field)
					if field_frequency[field][val] is None:
						field_frequency[field][val] = 0
					field_frequency[field][val] += 1
			
			for item in self.recommendations:
				for field in self.relevant_fields:
					val =getattr(item,field)
					if field_frequency[field][val] is None:
						field_frequency[field][val] = 0
					field_frequency[field][val] += 1
			
			self.stat_dict["cardinality"] = dict()
			for field in self.relevant_fields:
				self.stat_dict["cardinality"][field] = len(field_frequency[field])
			
			
		
		if key in self.stat_dict:
			if subkey is None:
				return self.stat_dict[key]
			else:
				if self.stat_dict[key][subkey] is None:
					return None
				else:
					return self.stat_dict[key][subkey]
		else:
			return None
			
	
	
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
	def playlist_frequency(self,GMT):	#GMT is a tuple of form (G,M,T)
		""" returns the frequency of the 'value' in attribute ( the #of times the attribute 'attribute' takes up the value 'value' ) in the playlist """
		return self.frequencies[GMT]
	
	def score(self,item):
		""" Returns score of the item as computed """
		return self.score[item]
	
	
	def _compute_scores(self,items,fields):
		""" Computes the scores of all recommended songs """
		score = dict()
		for item in items:
			score[item] = self._compute_score(item,fields)
		
		return score
	
	def normalized_frequency(self,frequency):
		
		
	
	def _cardinality_normalized_frequency(self, frequency_value, fields, avoid_fields):
		cardinality = 1
		for field in fields:
			if field in avoid_fields:
				continue
			else:
				cardinality *= stats("cardinality",field)
		
		return frequency_value * cardinality
		
	
