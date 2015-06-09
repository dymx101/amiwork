from news.contentranking.classes.socialscoreupdater import SocialScoreUpdater as SSU

ssu = SSU()
ssu._load_feed_statistics()
print ssu._feed_statistics