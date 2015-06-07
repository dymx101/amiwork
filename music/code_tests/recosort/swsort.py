import sys
from models.song import Song
from dataio.csvdataextractor import CSVDataExtractor
from  recommendationsorters.simpleweightedsorter import SimpleWeightedSorter

if len(sys.argv) < 3:
	print "2 cmd parameters required. Usage:\npy dataextract.py <playlist_file> <recommendations_file> [include_artist (Possible values=yes)]"
	exit(1)

plfile = open(sys.argv[1])
recofile = open(sys.argv[2])

if not (plfile and recofile):
	print "One or more of the files were not found"
	exit(1)

extractor = CSVDataExtractor()
pl = extractor.extract_pl(plfile)
reco = extractor.extract_reco(recofile)



relevant_fields = ['genre','mood']
if len(sys.argv)>=4 and sys.argv[3] == "yes":
		relevant_fields.append('artist')

swsorter = SimpleWeightedSorter()
swsorter.set_user_playlist(pl)
swsorter.set_recommendations(reco)


swsorter.set_relevant_fields(relevant_fields)

#print pl
#print reco

swsorter.count_frequencies()

swsorter.compute_importances()
#
'''
imp_sum= 0
for attr in swsorter.importance:
	if attr=='artist':
		continue
	else:
		imp_sum+= swsorter.importance[attr]
swsorter.importance['artist'] = imp_sum / (len(swsorter.importance)-1) #average
#'''
swsorter.compute_scores()
swsorter.sort()


for song in swsorter.sorted:
	print("%40s %40s %20s %20s %20s" % (song.title,song.artist,song.genre,song.mood,swsorter.score[song]) )

	



print swsorter.importance