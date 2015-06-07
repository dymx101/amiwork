class UserInterests:
	''' ------------------ Static vars ----------------------- '''
	# None yet

	''' ------------------- Subclasses ----------------------- '''
	class CategoryInterest:
		def __init__(self,category_id, level, read_count, unnormalized_interest=None, interest= None):
			self.category_id = category_id
			self.level = level
			self.read_count = read_count
			self.unnormalized_interest = unnormalized_interest
			self.interest = interest
			
	''' ------------------- end subclasses --------------------'''
	
	def __init__(self):
		'''self.category_list = None
		self._read_count = None	#{ category_id: read_count ,...}
		self._unnormalized_interest = None	# { category_id: unnormalized_interest,...}
		self.interest = None	# { category_id: normalized_interest,... Differs from unnormalized only by a constant factor :/}
		'''
		self.category_ids = None
		self.categories = None
		pass
	
	
	
	def get_user_interests(self,user_id):
		''' public method to call. Does all the work'''
		interest = dict()
		for category in self.categories:
			interest[category_id] = self.categories[category_id].interest
		return interest
	
	
	''' UPDATING INTERESTS '''
	def add_read_count(self,read_count,category_ids):
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
	def load_category_interest(self,load_all=False,load_active_set=False, category_ids=None,levels=None,parents=None):
		''' Ok, but how is the question? Everything in active set? '''
		self.categories = dict()
		dbi = DatabaseInterface.get_shared_instance()
		if load_all:
			self._load_all_categories(dbi)
		else:
			if load_active_set:
				self._load_active_set(dbi)
			if levels:
				self._load_by_level(levels,dbi)
			if parents:
				self._load_by_parents(parents,dbi)
			if category_ids:
				self.load_by_category_ids(category_ids,dbi)
			
		
	
	def _load_all_categories(self,dbi):
		cursor = dbi.execute("SELECT category_id,level,read_count FROM news_user_interests_read_count JOIN news_category USING(category_id)")
		rows = cursor.fetchall()
		self._process_db_rows(cursor.fetchall())
		#pass
	
	
	def _load_active_set(self,dbi):
		throw NotImplementedError("UserInterests._load_active_set is not implemented yet.")
		'''
		cursor= dbi.execute("SELECT category_id,level,read_count FROM news_categories_active JOIN news_user_interests_read_count JOIN news_category USING(category_id)")
		self._process_db_rows(cursor.fetchall())
		'''
		#pass
	
	def _load_categories_by_level(self,levels,dbi):
		for level in levels:
			cursor = dbi.execute("\
				SELECT category_id,level,read_count \
				FROM news_category JOIN news_user_interests_read_count USING(category_id)\
				WHERE level=%s\
				",(level,)
			)
			self._process_db_rows(cursor.fetchall())
		
	
	def _load_categories_by_parent(self,parents,dbi):
		for parent in parents:
			cursor = dbi.execute("\
				SELECT category_id,level,read_count \
				FROM news_category JOIN news_user_interests_read_count USING(category_id)\
				WHERE parent=%s\
				",(parent,)
			)
			self._process_db_rows(cursor.fetchall())
		
	
	def _load_categories_by_id(self, category_ids,dbi):
		for category_id in category_ids:
			cursor = dbi.execute("\
				SELECT category_id,level,read_count \
				FROM news_user_interests_read_count JOIN news_category USING(category_id)\
				WHERE news_user_interests_read_count.category_id=%s\
				",(category_id,)
			)
			self._process_db_rows(cursor.fetchall())
		
	
	def _process_db_rows(self,rows):
		for row in rows:
			if row['category_id'] in self.categories:
				continue
			else:
				self.categories[row['category_id']] = CategoryInterest(row['category_id'], row['level'],row['read_count'] )
		
	
	def _compute_interests(self):
		''' Computes the normalized interest, which is range_normalize( 1 + log(1+read_count) ) )  ( where range_normalize brings values to the range [0,1] ) '''
		self.load_category_read_counts()
		for category in self._read_count:
			item = self.categories[category]
			item.unnormalized_interest = self._compute_unnormalized_interest( item )
		
		return self._normalize_all()
	
	
	def _compute_unnormalized_interest(self,read_count):
		''' Returns 1+ log(1+read_count) ) which is the unnormalized interest ( for now ) '''
		return ( 1 + log(1+read_count) )
	
	def _normalize_all(self):
		''' Normalizes all interests ( WITHIN IT'S LEVEL ) to the range 0-1 '''
		max_unnormalized = dict()
		
		for category in self.categories:
			item = self.categories[category]
			if item.level not in max_unnormalized:
				max_unnormalized[item.level] = item.unnormalized_interest
			else:
				max_unnormalized = max( max_unnormalized , item.unnormalized_interest )
		
		for category in self.categories:
			item = self.categories[category]
			item.interest =  float(item.unnormalized_interest) / (max_unnormalized[item.level])
		
	
	