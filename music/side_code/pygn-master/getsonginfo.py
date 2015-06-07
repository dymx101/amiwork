from __future__ import print_function
import sys, pygn, json


clientID = '13118464-4E8A3151390D6E9F3979F8715F51F7F3' # Enter your Client ID from developer.gracenote.com here
userID = '27678420343239243-6E83356B7E66B2E6A2BF0B9B54C551AD' # Get a User ID from pygn.register() - Only register once per end-user

lines = open('krishnan_raw_reco.csv','r').read().split("\n")
for line in lines:
	vals = line.split(",")
	
	artist = vals[3]
	track = vals[4]
	print("Processing : ", (track+ " | " + artist ), file=sys.stderr)
	#print(track, " | " , vals)
	result = pygn.search(clientID=clientID, userID=userID, artist=artist, track=track)
	print(json.dumps(result, sort_keys=True, indent=4))
