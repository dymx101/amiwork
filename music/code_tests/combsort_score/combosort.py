import sys
from models.song import Song
from dataio.csvdataextractor import CSVDataExtractor
from recommendationsorters.combosorter import ComboSorter


if len(sys.argv) < 3:
	print "2 cmd parameters required. Usage:\npy dataextract.py <playlist_file> <recommendations_file> [include_artist (Possible values=yes)]"
	exit(1)

plfile = open(sys.argv[1])
recofile = open(sys.argv[2])

if not (plfile and recofile):
	print "One or more of the files were not found"
	exit(1)

extractor = CSVDataExtractor()
user_playlist = extractor.extract_pl(plfile)
recommendations = extractor.extract_reco(recofile)



relevant_fields = ['genre','mood']
if len(sys.argv)>=4 and sys.argv[3] == "yes":
		relevant_fields.append('artist')

combosorter = ComboSorter()
#'''
combosorter.set_user_playlist(user_playlist)
combosorter.set_recommendations(recommendations)
combosorter.remove_recommendations_in_playlist()
#'''
''' #Tests on your own playlist
combosorter.set_user_playlist(user_playlist)
combosorter.set_recommendations(user_playlist)

#'''
combosorter.set_relevant_fields( relevant_fields )#,"artist"] )
combosorter.build_ftree()


combosorter.compute_scores()
combosorter.sort()


#print len(combosorter.ftree.frequency)	#3039 for me :O

for song in combosorter.sorted:
	print("%40s %40s %20s %20s %20s" % (song.title,song.artist,song.genre,song.mood,combosorter.score[song]) )
'''
print "----------------------------------------"
for song in combosorter.playlist:#combosorter.sorted:
	print("%40s %40s %20s %20s %20s" % (song.title,song.artist,song.genre,song.mood,"N/A") )
'''