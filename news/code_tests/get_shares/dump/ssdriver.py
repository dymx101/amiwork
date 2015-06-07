from socialscoreupdater import SocialScoreUpdater

ssk = SocialScoreUpdater()
ssk._load_feed_statistics()
print "Statistics:"
print ssk._feed_statistics

ssk._mock_load_feed()
scores_link = list()
for link in ssk._mock_feed:
	item = ssk._mock_feed[link]
	score = ssk._normalize_across_feeds( item[2], item[0] )
	scores_link.append( (score,link) )

ranking = sorted(scores_link,reverse=True)

for item in ranking:
	print item[0],"\t\t",item[1]