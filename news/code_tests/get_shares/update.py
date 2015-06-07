from socialscoreupdater import SocialScoreUpdater as SSU
#
'''
for new_story_id in range(1,600):
	SSU.add_new_story(new_story_id)

exit(0)
#'''
update_all = True # False

ssu = SSU(update_all)
ssu.prepare_update()
ssu.update_scores()
ssu.build_new_active_set()
ssu.rotate_active_set()

ssu.update_permanent_scores()
ssu.update_statistics()