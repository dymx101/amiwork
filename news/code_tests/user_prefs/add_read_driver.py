from usercategoryinterests import UserCategoryInterests

ui = UserCategoryInterests(1)
#ui.add_read_count( 1, [3] )
ui.load_category_interests()
print ui.get_category_interests()

print ui.categories