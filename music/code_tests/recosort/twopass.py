import sys
from models.song import Song
from dataio.csvdataextractor import CSVDataExtractor
from  recommendationsorters.twopassftsorter import TwoPassFTSorter



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

twopassftsorter = TwoPassFTSorter()
twopassftsorter.set_user_playlist(user_playlist)
twopassftsorter.set_recommendations(recommendations)

twopassftsorter.set_relevant_fields( relevant_fields )
twopassftsorter.build_user_ftree()

ftree= twopassftsorter.user_ftree
#ftree.print_tree()

twopassftsorter.compute_scores()
twopassftsorter.sort()

#ftree= twopassftsorter.user_ftree
#ftree.print_tree()

for song in twopassftsorter.sorted:
	print("%40s %40s %20s %20s %20s" % (song.title,song.artist,song.genre,song.mood,twopassftsorter.score[song]) )
	
