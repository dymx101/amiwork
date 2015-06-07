class TermFrequencyClusterer:
	def __init__(self):
		self.articles = None
		self.treshold = 1
	
	def set_articles(self,articles):
		self.articles = articles
	
	def set_treshold(self, treshold):
		self.treshold = treshold
	
	
	def extract_key_words(self):
		''' uses stop words to extract keywords. Also keeps a count of them so we can do something similar to tf-idf for weights '''
		pass
	
	def vectorize(self):
		pass
	
	
	def cluster(self):
		pass
	
	
	def distance(self,item1,item2):
		pass
	
	def jaccard_distance(self,item1,item2):
		pass
	
	def cosine_distance(self,item1,item2):
		pass
	
	
	