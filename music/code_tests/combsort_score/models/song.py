

class Song:
	def __init__(self):
		self.songid = None
		self.userid = None	#For readability, mainly
		self.title = None
		self.artist = None
		self.mood = None
		self.genre = None
		self.album = None
	
	def __repr__(self):
		return str(self.__dict__)
	
