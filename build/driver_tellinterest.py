from news.contentranking.classes.usercategoryinterests import UserCategoryInterests
from news.contentranking.classes.personalizedscore import PersonalizedScore


ui = UserCategoryInterests(1)
#ui.add_read_count( 1, [3] )
ui.load_category_interests()
#print ui.get_category_interests()

#print ui.categories

category_ids = [1,2,3,4,5]


interests = dict()

for category_id in category_ids:
	interests[category_id] = ui.get_interest(category_id)


pscore = PersonalizedScore()
pscore.set_data([],interests)
print pscore.interests