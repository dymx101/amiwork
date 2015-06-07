import sys
from models.song import Song
from dataio.csvdataextractor import CSVDataExtractor
from  recommendationsorters.frequencysorter import FrequencySorter

if len(sys.argv) < 3:
	print "2 cmd parameters required. Usage:\npy dataextract.py <playlist_file> <recommendations_file>"
	exit(1)

plfile = open(sys.argv[1])
recofile = open(sys.argv[2])

if not (plfile and recofile):
	print "One or more of the files were not found"
	exit(1)

extractor = CSVDataExtractor()
pl = extractor.extract_pl(plfile)
reco = extractor.extract_reco(recofile)

freqsorter = FrequencySorter()
freqsorter.set_user_playlist(pl)
freqsorter.set_recommendations(reco)
freqsorter.set_relevant_fields(['genre','mood','artist'])	#,'tempo'

#print pl
#print reco

freqsorter.count_frequencies()

#'''
imp_sum= 0
#'''
freqsorter.compute_scores()
freqsorter.sort()
for song in freqsorter.sorted:
	print("%40s %40s %40s" % (song.title,song.artist,freqsorter.score[song]) )
	#print song.title, song.artist, freqsorter.score[song]
	

