from fptree import FPTree
#Feed this to the fptree

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

fptsorter = FPTSorter()
fptsorter.set_user_playlist(pl)
fptsorter.set_recommendations(reco)
fptsorter.set_relevant_fields(['genre','mood','artist'])	#,'tempo'


print fpt.mine_frequencies()