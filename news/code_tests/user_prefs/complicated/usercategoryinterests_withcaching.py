import time,math
from databaseinterface import DatabaseInterface

class UserCategoryInterests:
	''' This class does not consider levels or parents while computing interests. it is completely oblivious '''
	
	''' ------------------ Static vars ----------------------- '''
	acceptable_cache_age = 1800
	use_caching = False
	
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
		if UserCategoryInterests.use_caching and self._check_cache():
			self._load_from_cache()
		else:
			cursor = dbi.execute("SELECT category_id,read_count FROM news_user_interests_read_count ",None)
			rows = cursor.fetchall()
			
			self._process_db_rows(rows)
			self._compute_interests()
		
		if UserCategoryInterests.use_caching:
			self._cache_interests()
		
		return self.categories
	
	def _process_db_rows(self,rows):
		for row in rows:
			if row['category_id'] in self.categories:
				continue
			else:
				self.categories[row['category_id']] = UserCategoryInterests.CategoryInterest(row['category_id'], row['read_count'] )
		
	''' Calculating functions '''
	
	def _compute_interests(self):
		''' Computes the normalized interest, which is range_normalize( 1 + log(1+read_count) ) )  ( where range_normalize brings values to the range [0,1] ) '''
		for category_id in self.categories:
			item = self.categories[category_id]
			item.unnormalized_interest = self._compute_unnormalized_interest( item.read_count )
			
		return self._normalize_all()
	
	
	def _compute_unnormalized_interest(self,read_count):
		''' Returns 1+ log(1+read_count) ) which is the unnormalized interest ( for now ) '''
		return ( 1 + math.log(1+read_count) )
	
	def _normalize_all(self):
		''' Normalizes all interests to the range 0-1 '''
		max_unnormalized = 0
		
		for category in self.categories:
			item = self.categories[category]
			max_unnormalized = max( max_unnormalized , item.unnormalized_interest )
		
		for category in self.categories:
			item = self.categories[category]
			item.interest =  float(item.unnormalized_interest) / (max_unnormalized)
	

	''' Caching functions '''
	def _check_cache(self):	
		''' Checks if the cache is stale '''
		dbi = DatabaseInterface.get_shared_instance()
		cursor = dbi.execute( "SELECT MIN(cached_time) as oldest_cached FROM cache_news_user_interests WHERE user_id=%s",(self.user_id,) )
		rows = cursor.fetchall()
		oldest_acceptable = int(time.time()) - UserCategoryInterests.acceptable_cache_age
		for row in rows:
			if row['oldest_cached'] < oldest_acceptable:
				dbi.execute("DELETE FROM cache_news_user_interests WHERE user_id=%s AND cached_time < %s", (self.user_id,oldest_acceptable) )
				return False
		
		return True
		
	
	def _load_from_cache(self):	
		''' implements very simple caching on the whole set. Idk why i bothered writing this but maybe it'll help -_- '''
		dbi = DatabaseInterface.get_shared_instance()
		cursor = dbi.execute( "SELECT category_id, read_count, unnormalized_interest, interest, cached_time FROM cache_news_user_interests WHERE user_id=%s",(self.user_id,) )
		rows = cursor.fetchall()
		temp_categories = dict()
		for row in rows:
			self.categories[ row['category_id'] ] = UserCategoryInterests.CategoryInterest(row['category_id'], row['read_count'], row['unnormalized_interest'], row['interest'])
		
		return True
	
	
	def _cache_interests(self):
		dbi = DatabaseInterface.get_shared_instance()
		dbi.autocommit(False)
		
		time_now = int(time.time())
		for category_id in self.categories:
			category = self.categories[category_id]
			query_params = (self.user_id,category.category_id, category.read_count, category.unnormalized_interest, category.interest, time_now)
			dbi.execute("REPLACE INTO cache_news_user_interests (user_id, category_id, read_count, unnormalized_interest, interest, cached_time) VALUES(%s,%s,%s,%s,%s,%s)", query_params )
		dbi.commit()
		
		dbi.autocommit(True)
		