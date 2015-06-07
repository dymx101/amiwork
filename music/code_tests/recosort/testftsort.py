from recommendationsorters.ftsorter import FTSorter

class GMTClass:
	def __init__(self,tup):
		self.genre = tup[0]
		self.mood = tup[1]
		self.tempo = tup[2]


tup = [
	( "Rock", "Happy", "High"),
	( "Rock", "Happy", "High"),
	( "Pop", "Happy", "High"),
	( "Country", "Happy", "High"),
	( "Rock", "Sad", "Low"),
	( "Pop", "Melancholy", "Medium"),
]

rec_tup = [
	( "Rock", "Happy", "High"),
	( "Pop", "Happy", "High"),
	( "Pop", "Happy", "Low")
]

user_playlist = []
for t in tup:
	user_playlist.append(GMTClass(t))

recommendations = []
for t in rec_tup:
	recommendations.append(GMTClass(t))


ftsorter = FTSorter()
ftsorter.set_user_playlist(user_playlist)
ftsorter.set_recommendations(recommendations)
ftsorter.set_relevant_fields( ["genre","mood","tempo"] )
ftsorter.build_user_ftree()

ftree= ftsorter.user_ftree
#ftree.print_tree()

ftsorter.compute_scores()
ftsorter.sort()

ftree= ftsorter.user_ftree
ftree.print_tree()

print ftsorter.score
for song in ftsorter.sorted:
	print("%20s %20s %20s %10s" % (song.genre,song.mood,song.tempo,ftsorter.score[song]) )