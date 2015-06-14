from news.contentranking.classes.socialscoreupdater import SocialScoreUpdater as SSU

ssu = SSU()
ssu._load_feed_statistics()
print ssu._feed_statistics
for feed_id in ssu._feed_statistics:
	print feed_id, ssu._feed_statistics[feed_id][0],ssu._feed_statistics[feed_id][1],ssu._feed_statistics[feed_id][2]