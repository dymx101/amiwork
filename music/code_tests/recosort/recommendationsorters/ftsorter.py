from recommendationsorters.ftree import FTree

class FTSorter:
	""" Sorter that relies on frequency of occurences in playlist and recommendations to sort """
	#Generic functions
	def __init__(self):
		self.playlist = None 			#list()
		self.recommendations = None		#list()
		self.sorted = None				#list()
		self.relevant_fields = None
		
		self.user_ftree = None
		self.stat_dict = None
		
	
	def set_relevant_fields(self,fields ):
		self.relevant_fields = fields
	
	def set_user_playlist(self,playlist):
		""" Takes a list of items ( of type Song ) in playlist. Stores them in self.playlist"""
		self.playlist = playlist
		
	
	def set_recommendations(self, recommendations):
		""" Takes a list of items ( of type Song ) in recommendations . Stores them in self.recommendations """
		self.recommendations = recommendations 
		
	
	def build_user_ftree(self):
		self.user_ftree = FTree()
		self.user_ftree.set_items(self.playlist)
		self.user_ftree.set_fields(self.relevant_fields)
		self.user_ftree.build()	
		
	
	def stats(self,key):
		if self.stat_dict is None:
			#Load stats
				self.stat_dict = dict()
				self.stat_dict["max_combos"] = float(8)#(8000)	#20 genres, 20 moods, 20 tempos assumed. Do it from a database query when we have data
		
		if key in self.stat_dict:
			return self.stat_dict[key]
		else:
			return None
		
	
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
		
	
	#Editable functions based on your model
	def _compute_score(self,GMT,fields=None):
		""" Computes the score of a certain item """
		support = (self.fondness(GMT,fields)+1) #/ self.stats("max_combos")
		score = support #Do something on it, yeah?
		return score
	
	def fondness(self, GMT,fields=None):
		''' returns a float = (frequency of GMT in user_ftree / no of items in user_ftree) '''
		if fields is None:
			fields=  self.relevant_fields
		return float(self.user_ftree.get_frequency(GMT,fields)) #/ self.user_ftree.item_count()
		
	
