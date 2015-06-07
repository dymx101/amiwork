import time,math
from databaseinterface import DatabaseInterface

class UserCategoryInterests:
	''' This class does not consider levels or parents while computing interests. it is completely oblivious '''
	base_read_count = 10
	''' ------------------ Static vars ----------------------- '''
	#	None yet
	''' ------------------- Subclasses ----------------------- '''
	class CategoryInterest:
		def __init__(self,category_id, read_count, unnormalized_interest=None, interest= None):
			self.category_id = category_id
			self.read_count = read_count
			self.unnormalized_interest = unnormalized_interest
			self.interest = interest
		
		def __repr__(self):
			return vars(self).__repr__()
	''' ------------------- end subclasses --------------------'''
	
	def __init__(self,user_id):
		'''
		self.category_ids = None
		self.category_list = None
		self._read_count = None	#{ category_id: read_count ,...}
		self._unnormalized_interest = None	# { category_id: unnormalized_interest,...}
		self.interest = None	# { category_id: normalized_interest,... Differs from unnormalized only by a constant factor :/}
		'''
		self.user_id = user_id
		self.categories = None
		
	
	
	
	def get_category_interests(self):
		''' public method to call. Does all the work'''
		interest = dict()
		for category_id in self.categories:
			interest[category_id] = self.categories[category_id].interest
		
		return interest
	
	
	
	''' UPDATING INTERESTS '''
	def add_read_count(self,read_count,category_ids):	#Seems to work
		dbi = DatabaseInterface.get_shared_instance()
		dbi.autocommit(False)
		
		for category_id in category_ids:
			dbi.execute("\
				INSERT INTO news_user_interests_read_count (user_id,category_id,read_count) VALUES( %s,%s, %s )\
				ON DUPLICATE KEY UPDATE read_count= read_count+%s\
				", ( self.user_id, category_id, read_count, read_count )
			)
		dbi.commit()
		
		dbi.autocommit(True)
	
	
	''' READING INTERESTS '''
	
	def load_category_interests(self):
		''' Ok, but how is the question? Everything in active set? '''
		self.categories = dict()
		dbi = DatabaseInterface.get_shared_instance()
		cursor = dbi.execute("SELECT category_id,read_count FROM news_user_interests_read_count ",None)
		rows = cursor.fetchall()
		print "ROWS",rows
		self._process_db_rows(rows)
		self._compute_interests()
		
		return self.categories
	
	def _process_db_rows(self,rows):
		for row in rows:
			if row['category_id'] in self.categories:
				continue
			else:
				self.categories[row['category_id']] = self.CategoryInterest(row['category_id'], row['read_count'] )
		
	''' Calculating functions '''
	
	def _compute_interests(self):
		''' Computes the normalized interest, which is range_normalize( math.log( base+read_count,base ) )  )  ( where range_normalize brings values to the range [0,1] ) '''
		for category_id in self.categories:
			item = self.categories[category_id]
			print item.read_count
			item.unnormalized_interest = self._compute_unnormalized_interest( item.read_count )
			
		return self._normalize_all()
	
	
	
	def _compute_unnormalized_interest(self,read_count):
		''' Returns math.log( base+read_count,base)  which is the unnormalized interest ( for now ) '''
		return math.log( self.base_read_count + read_count , base) 
	
	def _normalize_all(self):
		''' Normalizes all interests to the range 0-1 '''
		max_unnormalized = 0
		
		for category in self.categories:
			item = self.categories[category]
			max_unnormalized = max( max_unnormalized , item.unnormalized_interest )
		
		for category in self.categories:
			item = self.categories[category]
			item.interest =  float(item.unnormalized_interest) / (max_unnormalized)
		
	
