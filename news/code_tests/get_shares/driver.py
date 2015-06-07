from socialscoreupdater import SocialScoreUpdater as SSK

#This doesn't look like the code that does everything but it is :/
ssk = SSK()
ssk._load_from_db()
ssk._mock_load_feed_statistics()

ssk.update_scores()
for url in ssk.social_score_stories:
	print ssk.social_score_stories[url]