from news.contentranking.classes.usercategoryinterests import UserCategoryInterests
from news.contentranking.classes.personalizedscore import PersonalizedScore
from news.models.newsstory import NewsStory
from databaseinterface.databaseinterface import DatabaseInterface


def get_personal_recos(user_id):
	''' --------- FUNCTIONS -----'''

	def score_comparator(x,y):
		if x.score < y.score:
			return -1
		elif x.score == y.score:
			return 0
		else:
			return 1

	''' --------- MAIN -----'''
	ui = UserCategoryInterests(user_id)
	#ui.add_read_count( 1, [3] )
	ui.load_category_interests()

	#Load ALL stories with the normalized score 
	dbi = DatabaseInterface.get_shared_instance()
	cursor = dbi.execute("SELECT * FROM news_stories JOIN news_social_score_active USING(story_id)", None)
	rows = cursor.fetchall()
	content = []
	seen_categories= dict()
	for r in rows:
		cursor = dbi.execute("SELECT category_id FROM news_story_categories WHERE story_id=%s",(r['story_id'],))
		category_rows = cursor.fetchall()
		story_categories = list()
		for c in category_rows:
			story_categories.append(c['category_id'])
			seen_categories[c['category_id']] = True
		content.append( NewsStory(r['story_id'],r['url'],r['title'],r['subtitle'],r['feed_id'],r['created'],r['image'],story_categories,r['normalized_score']) )

	interests = dict()
	#print "\ncontent",content,"\nseen_categories",seen_categories
	for category_id in seen_categories:
		interests[category_id] = ui.get_interest(category_id)


	pscore = PersonalizedScore()
	pscore.set_data(content,interests)
	pscore.personalize_scores()


	return sorted(content, cmp= score_comparator, reverse=True)
