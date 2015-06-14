import time,math
from databaseinterface.databaseinterface import DatabaseInterface
from localconfig import LocalConfig
class UserCategoryInterests:
	''' This class does not consider levels or parents while computing interests. it is completely oblivious '''
	''' ------------------ Static vars ----------------------- '''
	base_read_count = LocalConfig.usercategoryinterests_base_read_count 
	''' ------------------- Subclasses ----------------------- '''
	class CategoryInterest:
		def __init__(self,category_id, read_count, interest= None):
			self.category_id = category_id
			self.read_count = read_count
			self.interest = interest
		
		def __repr__(self):
			return vars(self).__repr__()
	''' ------------------- end subclasses --------------------'''
	
	def __init__(self,user_id):
		self.user_id = user_id
		self.categories = None	# Dict { category_id: CategoryInterest object [,...] }
	
	
	''' UPDATING INTERESTS '''
	def add_read_count(self,read_count,category_ids):	#Seems to work
		''' Increment the read count of each of the category_ids specified by read_count '''
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
	
	
	def get_interest(self,category_id):	
		if category_id in self.categories:
			return self.categories[category_id].interest
		else:
			return 1
	
	def get_combined_interest(self,categories):
		''' Not thoroughly thought through >.< 
		Currently returns the interest(sum_over_categories(read_count))
		'''
		total_read_count = 0
		for category_id in categories:
			if category_id in self.categories:
				total_read_count += self.categories[category_id]
		
		return self._compute_interest(total_read_count)	
		
	
	def get_category_interests(self):
		''' After you call load_category_interest, Call this method to get a dict of the form {category_id: interest}'''
		interest = dict()
		for category_id in self.categories:
			interest[category_id] = self.categories[category_id].interest
		
		return interest
	
	
	def load_category_interests(self):
		''' Loads the interest in all categories of the user_specified '''
		self.categories = dict()
		dbi = DatabaseInterface.get_shared_instance()
		cursor = dbi.execute("SELECT category_id,read_count FROM news_user_interests_read_count where user_id=%s",(self.user_id,))
		rows = cursor.fetchall()
		
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
		''' Computes the interest, which is math.log( base+read_count,base ) '''
		for category_id in self.categories:
			item = self.categories[category_id]
			item.interest = self._compute_interest( item.read_count )
			
	
	
	def _compute_interest(self,read_count):
		''' Returns math.log( base+read_count,base)  which is the interest ( for now ) '''
		return math.log( self.base_read_count + read_count , self.base_read_count) 
	