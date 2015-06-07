from usercategoryinterests import UserCategoryInterests
from facebookpagelikescraper import FacebookPageLikeScraper

user_id = 1
user_access_token = 'CAACEdEose0cBAFyFoxGJcX5sNpACGbJTlO4o2Hm9pT352tRQYSwzRJmklNZCx8KLVpKnZCmsTqOGzRi6BodWGPfQOxXeqVabMsmNhfQwfnKQLP7qYuJsHylxEh9EkWGM6MupZAJFYaKMmYdHhGiHPtPX1citMYgSnV53y4zI67BEUg8WBe1iIrffO2iVooaZAeL1UCeJyWGxc7R0r7ZBZBHYiO3YXrFMAZD'

fpls = FacebookPageLikeScraper(user_access_token)
fpls.load_feed_ids()
liked_feed_ids = fpls.get_liked_feed_ids()


dbi = DatabaseInterface.get_shared_instance()
categories = dict()	#To have only distinct
for liked_feed_id in liked_feed_ids:
	cursor= dbi.execute("SELECT category_id FROM news_feed_category_mapping WHERE feed_id=%s",(liked_feed_id,))
	for category_id in cursor.fetchall():
		categories[category_id] = 1
		

uci = UserCategoryInterests(user_id)
category_list = categories.keys()
uci.add_read_count(40,category_list)