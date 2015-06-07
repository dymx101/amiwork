from recommendationsorters.ftree import FTree
import math

class ComboSorter:
	""" Sorter that relies on frequency of occurences in playlist and recommendations to sort """
	#Generic functions
	def __init__(self):
		self.playlist = None 			#list()
		self.recommendations = None		#list()
		self.sorted = None				#list()
		self.relevant_fields = None
		
		self.ftree = None
		#Private 
		self._stat_dict = None
		self._field_combos = None
		self.scoring_function = None
		
	
	def set_scoring_function(self,function_name, subscore_op='add'):
		self.scoring_function = getattr(self,function_name)
		self.subscore_op = subscore_op
		
	
	def set_relevant_fields(self,fields ):
		self.relevant_fields = fields
	
	def set_user_playlist(self,playlist):
		""" Takes a list of items ( of type Song ) in playlist. Stores them in self.playlist"""
		self.playlist = playlist
		
	
	def set_recommendations(self, recommendations):
		""" Takes a list of items ( of type Song ) in recommendations . Stores them in self.recommendations """
		self.recommendations = recommendations 
		
	
	def remove_recommendations_in_playlist(self):
		new_reco = list()
		
		hm = dict() #Create a hashmap
		for song in self.playlist:
			hm[song.songid] = True
		
		for song in self.recommendations:
			if song.songid not in hm:	#Thank god i know what a hashmap is used for -_-
				new_reco.append(song)
		
		self.recommendations = new_reco
		
	
	def build_ftree(self):
		self.ftree = FTree()
		self.ftree.set_items(self.playlist)# + self.recommendations)
		self.ftree.set_fields(self.relevant_fields)
		self.ftree.build()	
		self.ftree.mine_frequencies()	
		self.ftree.compute_stats()
		
	
	#Your access to working functions
	def compute_scores(self,fields=None):
		if fields is None:
			fields = self.relevant_fields
		self.score = self._compute_scores(self.recommendations,fields)
		
	
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
		
	
	def _list_field_combos(self):
		''' Returns a list of all combos that can be generated '''
		''' ---------------------------------------- '''
		def rec(fields,at_index):	#Local scope ftw :p
			''' Returns a list of all combo tuples that can be generated from the suffix starting at at_index '''
			if at_index == len(fields)-1:
				return [ [fields[at_index]] ]
			#Add yourself
			combos = rec( fields,at_index+1 )
			
			only_this = [ fields[at_index] ]
			combo_len = len(combos)
			combos.append( only_this )
			for i in range(0,combo_len):
				combos.append( only_this + combos[i] )
			
			return combos 
			
		''' ---------------------------------------- '''
		if self._field_combos is None:
			self._field_combos= rec(self.relevant_fields,0)
			
		return self._field_combos
	
	
	
	
	def gen_query_dict(self,fc,item):
		field_combos = self._list_field_combos()
		query = dict()
		for field in fc:
			query[field] = getattr(item,field)
		return query
		
	
	
	def _compute_score(self,item,fields=None):
		""" Computes the score of a certain item. Formula used: ??? """
		
		score = 1	#Doesn't really matter if i use 1 instead of 0 for addition, does it? Stick to it
		field_combos = self._list_field_combos()
		
		for fc in field_combos:	
			query_dict = self.gen_query_dict(fc,item)
			if self.subscore_op == 'mul':
				score *= self.scoring_function(query_dict)
			else:
				score += self.scoring_function(query_dict)
			
		return score
	
	
	''' 
	------------------------
		SCORE FUNCTIONS 
	-----------------------
	'''
	def _raw_frequency_score(self,query_dict):
		return self.ftree.get_frequency_from_dict(query_dict)
	
	def _log_score(self, query_dict):
		''' Fields with low cardinality ( such as mood ) dominate (?) '''
		return math.log(1+ self.ftree.get_frequency_from_dict(query_dict))
	
	
	def _normalized_score(self,query_dict):
		''' Addition: Favours a combination of genre,mood by the looks of it... which isn't bad. Otherwise decent balance '''
		''' Multiplication: Favours artists you've heard before over artists you haven't. Massive bummer :( '''
		return self.normalized_frequency(query_dict)
	
	''' The artist field absolutely dominates the cardianlity part. Taking log(1+cardinality) helps massively and it's almost invisible in cardinality score
			Without cardinality, The more difficult matches are given the same weight as easier matches 
			Multiplying scores with cardinality factors as distribution over all multiplications means the result is just the normalized score * k ( k = product_over_all_field_combos( cardinality )
			Not really worth the effort
	'''
			
	def _normalized_with_cardinality(self,query_dict):
		''' Fun but still seems to be dominated by artist '''
		#return math.log(1+self.max_cardinality(query_dict)) * self.normalized_frequency(query_dict) 
		#return math.log(1+self.field_combo_cardinality(query_dict)) * self.normalized_frequency(query_dict)	#Not a big difference. This will be faster
		return self.field_combo_cardinality(query_dict) * self.normalized_frequency(query_dict)	#Not a big difference. This will be faster
	
	def _cardinality_score(self,query_dict):
		''' Surprising. Can't tell much from my skewed playlist '''
		#return math.log(1+self.max_cardinality(query_dict)) * self.ftree.get_frequency_from_dict(query_dict)
		#return math.log(1+self.field_combo_cardinality(query_dict)) * self.ftree.get_frequency_from_dict(query_dict)	#This works horrible because artists has such a high cardinality
		return self.field_combo_cardinality(query_dict) * self.ftree.get_frequency_from_dict(query_dict)	#This works horrible because artists has such a high cardinality
	
	

	''' 
	---------------------------------------------
		FUNCTIONS USED WITHIN SCORING FUNCTIONS 
	----------------------------------------------
	'''

	def normalized_frequency(self,query_dict):
		query_fields = []
		for key in query_dict:
			query_fields.append(key)
		max_val = self.ftree.get_max_freq(query_fields)
		freq = self.ftree.get_frequency_from_dict(query_dict)
		return float(freq+1)/(max_val+1)
			
	
	def field_combo_cardinality(self,query_dict):
		''' Here's the actual cardinality '''
		return self.ftree.get_field_combo_cardinality(query_dict.keys())
	
	"""
	''' These functions are for using max_cardinality ( product of cardinality of atomic fields ) rather than  field_combo_cardinality ( actual cardinality of combination of fields )'''
	''' Commented out to not waste execution. It's not that inefficient though '''
	
	def max_cardinality(self,query_dict):
		cardinality = 1
		for field in query_dict:
			cardinality *= self.stats("cardinality",field)
		
		return cardinality
		
	
	def stats(self, key, subkey=None):
		if self._stat_dict is None:
			#Load stats
			self._stat_dict = dict()
			#Compute field frequency. This approach takes O( |fields| * |items| ) time ( theta actually ). Using the tree would be more efficient
			#This is actually done in the tree now. In the field_combo_cardinality variable
			field_frequency = dict()
			
			for field in self.relevant_fields:
				field_frequency[field] = dict()
			
			for item in self.playlist:
				for field in self.relevant_fields:
					val =getattr(item,field)
					if val not in field_frequency[field]:
						field_frequency[field][val] = 0
					field_frequency[field][val] += 1
			
			for item in self.recommendations:
				for field in self.relevant_fields:
					val =getattr(item,field)
					if val not in field_frequency[field]:
						field_frequency[field][val] = 0
					field_frequency[field][val] += 1
			
			self._stat_dict["cardinality"] = dict()
			for field in self.relevant_fields:
				self._stat_dict["cardinality"][field] = len(field_frequency[field])
			
			
		
		if key in self._stat_dict:
			if subkey is None:
				return self._stat_dict[key]
			else:
				if self._stat_dict[key][subkey] is None:
					return None
				else:
					return self._stat_dict[key][subkey]
		else:
			return None
			
		#"""