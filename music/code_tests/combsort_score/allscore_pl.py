import sys
from models.song import Song
from dataio.csvdataextractor import CSVDataExtractor
from recommendationsorters.playlistonly import ComboSorter


if len(sys.argv) < 4:
	print "3 cmd parameters required. Usage:\npy dataextract.py <playlist_file> <recommendations_file> <user_id>"
	exit(1)

plfile = open(sys.argv[1])
recofile = open(sys.argv[2])
user_id = sys.argv[3]


if not (plfile and recofile):
	print "One or more of the files were not found"
	exit(1)



print "Loading files..."

extractor = CSVDataExtractor()
user_playlist = extractor.extract_pl(plfile)
recommendations = extractor.extract_reco(recofile)



relevant_fields = ['genre','mood','artist']
"""
scoring_functions = [
	('_raw_frequency_score','add' ) 
	''' ,('_raw_frequency_score','mul'), #Same as normalized multiplication '''
	''' ,('_log_score','add'),#Same as raw_frequency multiply ''' 
	,('_log_score','mul')
	, ('_normalized_score','add')
	,('_normalized_score','mul')
	,('_normalized_with_cardinality','add')
	''' ,('_normalized_with_cardinality','mul'), #same as normalized multiplication'''
	,('_cardinality_score','add') 
	''' ,('_cardinality_score','mul') #Same as raw_frequency multiplication '''
] """


scoring_functions = [
	('_raw_frequency_score','add' ) 
	,('_log_score','mul')
	, ('_normalized_score','add')
	,('_normalized_score','mul')
	,('_normalized_with_cardinality','add')
	,('_cardinality_score','add') 

] 

print "Setting data..."
combosorter = ComboSorter()

combosorter.set_user_playlist(user_playlist)
combosorter.set_recommendations(recommendations)
combosorter.remove_recommendations_in_playlist()

print "Building ftree..."
combosorter.set_relevant_fields( relevant_fields )
combosorter.build_ftree()

print "Computing scores..."
for sf in scoring_functions:
	print "\t"+sf[0]+" with "+ sf[1]
	combosorter.set_scoring_function(sf[0],sf[1])
	combosorter.compute_scores()
	combosorter.sort()
	
	print "\t\tDone..."
	result_file = open('results/allscore_'+user_id+'/reco_'+sf[0] + '_' + sf[1] +'.out','w')
	for song in combosorter.sorted:
		result_file.write("%40s %40s %20s %20s %20s\n" % (song.title,song.artist,song.genre,song.mood,combosorter.score[song]) )
	result_file.close()
	

#Finally, give us an idea of what hte user likes from the playlist
#'''

print "Setting data..."
plsorter = ComboSorter()

plsorter.set_user_playlist(user_playlist)
plsorter.set_recommendations(user_playlist)

print "Building ftree..."
plsorter.set_relevant_fields( relevant_fields )
plsorter.build_ftree()

plsorter.build_ftree()
print "Computing score..."
for sf in scoring_functions:
	print "\t"+sf[0]+" with "+ sf[1]
	plsorter.set_scoring_function(sf[0],sf[1])
	plsorter.compute_scores()
	plsorter.sort()
	
	print "\t\tDone..."
	result_file = open('results/allscore_'+user_id+'/pl_'+sf[0] + '_' + sf[1] +'.out','w')
	for song in plsorter.sorted:
		result_file.write("%40s %40s %20s %20s %20s\n" % (song.title,song.artist,song.genre,song.mood,plsorter.score[song]) )
	result_file.close()
#'''