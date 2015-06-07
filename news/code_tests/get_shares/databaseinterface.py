import MySQLdb
from config import Config

class DatabaseInterface:
	shared_instance = None
	@staticmethod
	def get_shared_instance():
		if DatabaseInterface.shared_instance is None:
			DatabaseInterface.shared_instance = DatabaseInterface(True)	#New connection
		return DatabaseInterface.shared_instance
	
	def __init__(self,share=False):
		self.dbi = None
		self.cursor = None
		self.connect(share)	# Why not?
		
	
	def _map_functions(self):
		self.autocommit = self.dbi.autocommit
		self.commit = self.dbi.commit
		self.rolback = self.dbi.rollback
		
	
	def connect(self,share=False):
		try:
			self.dbi = MySQLdb.connect(Config.mysql_host,Config.mysql_user,Config.mysql_password,Config.mysql_database)
			self.cursor = self.dbi.cursor(MySQLdb.cursors.DictCursor)
			#All hail autocommit!
			self.dbi.autocommit(True)
			if share:
				shared_instance = self
			
		except MySQLdb.Error, e:
			self.close()
			raise BaseException("MySQL could not connect: %s" %e)
		
		self._map_functions()
		
	
	def execute(self,queryStr, args):
		self.executeQuery(queryStr,args)
		return self.cursor
	
	def executeQuery(self,queryStr,args): #Yes, It needs to be this complicated.
		try:
			self.cursor.execute(queryStr,args)
		except (AttributeError, MySQLdb.OperationalError, MySQLdb.InterfaceError): #MySQL has gone away
			self.connect()	#Reconnect incase it went away :(
			self.cursor.execute(queryStr,args)
		
	
	
	def close(self):
		#Closing/Querying a closed connection crashes python. So be careful
		if self.dbi!= None and self.dbi.open!=0:
			self.dbi.close()
		self.dbi = None
		self.dbiCursor = None
