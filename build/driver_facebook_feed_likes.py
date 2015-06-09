from news.contentranking.classes.usercategoryinterests import UserCategoryInterests
from news.contentranking.classes.scrapers.facebookpagelikescraper import FacebookPageLikeScraper as FPLS
from databaseinterface.databaseinterface import DatabaseInterface

from news.contentranking.classes.localconfig import LocalConfig as ContentRankingConfig
import sys

dbi = DatabaseInterface.get_shared_instance()

rows = list()
if len(sys.argv)<2:
	cursor = dbi.execute("SELECT user_id,email,access_token FROM first_test_users ",None)
else:
	user_id = sys.argv[1]
	cursor = dbi.execute("SELECT user_id,email,access_token FROM first_test_users WHERE user_id=%s",(user_id,))
rows = cursor.fetchall()

for row in rows:
	
	user_id = row['user_id']
	user_access_token = row['access_token']
	fpls = FPLS(user_access_token)
	fpls.load_feed_ids()
	liked_feed_ids = fpls.get_liked_feed_ids()
	#liked_feed_ids = [4,5,7]
	#print "Liked feed_ids",liked_feed_ids


	dbi = DatabaseInterface.get_shared_instance()
	categories_liked = dict()
	total_likes = 0
	print user_id, ": ",liked_feed_ids
	for feed_id in liked_feed_ids:
		cursor = dbi.execute( "SELECT category_id FROM first_test_feed_category WHERE feed_id=%s", (feed_id,) )
		for rows in cursor.fetchall():
			cat = rows['category_id']
			if cat not in categories_liked:
				categories_liked[cat] = 0
			categories_liked[cat] += 1
			total_likes += 1
		
	#'''
	interest = dict()
	for cat in categories_liked:
		interest[cat] = 1+categories_liked[cat]

	#'''

	read_count = dict()
	base_read_count = ContentRankingConfig.usercategoryinterests_base_read_count


	for cat in interest:
		read_count[cat] =  (base_read_count ** interest[cat]) - base_read_count

	uci = UserCategoryInterests(user_id)
	for cat in read_count:
		uci.add_read_count(read_count[cat], [cat])

	print "Completed for ", row['email']
'''
TRUNCATE TABLE news_user_interests_read_count;
'''