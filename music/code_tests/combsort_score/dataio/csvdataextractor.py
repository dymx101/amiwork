from models.song import Song

class CSVDataExtractor:

	def pl_from_csv(self,csv):
		vals = csv.split(",")
		s = Song()
		s.songid = vals[0]
		s.userid = vals[1]	#For readability, mainly
		s.title = vals[2]
		s.artist = vals[3]
		s.mood = vals[4]
		s.genre = vals[5]
		return s

	def reco_from_csv(self,csv):
		vals = csv.split(",")
		s = Song()
		s.songid = vals[0]
		#Ignore 	vals[1]
		s.mood = vals[2]
		s.genre = vals[3]
		s.userid = vals[4]
		s.album = vals[5]
		s.artist = vals[6]
		s.title = vals[7]
		
		
		return s
		
	
	def extract_reco(self,recofile):
		reco_raw = recofile.read().split("\n")
		reco = list()
		for s in reco_raw :
			if not s:	#Blank lines
				continue 
			reco.append(self.reco_from_csv(s))
		
		return reco
	
	def extract_pl(self,plfile):
		pl_raw = plfile.read().split("\n")
		pl = list()

		for s in pl_raw:
			if not s:	#Blank lines
				continue 
			pl.append(self.pl_from_csv(s))
		
		return pl


