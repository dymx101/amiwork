import sys
from models.song import Song
from dataio.csvdataextractor import CSVDataExtractor
from recommendationsorters.ftsorter import FTSorter


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

ftsorter = FTSorter()
ftsorter.set_user_playlist(user_playlist)
ftsorter.set_recommendations(recommendations)
ftsorter.set_relevant_fields( relevant_fields )#,"artist"] )
ftsorter.build_user_ftree()

ftree= ftsorter.user_ftree
#ftree.print_tree()

ftsorter.compute_scores()
ftsorter.sort()

#ftree= ftsorter.user_ftree
#ftree.print_tree()

for song in ftsorter.sorted:
	print("%40s %40s %20s %20s %20s" % (song.title,song.artist,song.genre,song.mood,ftsorter.score[song]) )

