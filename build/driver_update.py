from news.contentranking.classes.socialscoreupdater import SocialScoreUpdater as SSU
from mailsimple import mail_text
admin_email = 'krishnancmf8@gmail.com'
#try:
if True:
	update_all = True # False

	ssu = SSU(update_all)
	ssu.prepare_update()
	ssu.update_scores()
	ssu.build_new_active_set()
	ssu.rotate_active_set()

	ssu.update_permanent_scores()
	ssu.update_statistics()
	
	''' Let me know? '''
	subject='Score update completed successfully!'
	report = "YAYAYAYAYAY!"
	mail_text(admin_email, subject, report )
#
'''
except Exception as e:
	print "\n------ERROOOOOOOOOOOOOOOR!!!---------\n"
	print e.__doc__ +"\n"+ str(e.message )
	subject='COMPLETE FAILURE OF SCORE UPDATES!'
	report = e.__doc__ +"\n"+ str(e.message )
	mail_text(admin_email, subject, report )
'''