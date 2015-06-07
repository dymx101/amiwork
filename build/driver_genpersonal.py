from personalize import get_personal_recos
from databaseinterface.databaseinterface import DatabaseInterface
from mail import mail
from mailsimple import mail_text
import time

#try:
if True:
	timesig = int(time.time())
	dbi = DatabaseInterface.get_shared_instance()

	cursor = dbi.execute("SELECT user_id,email,access_token FROM first_test_users ",None)
	rows = cursor.fetchall()
	
	for row in rows:
		
		user_id = row['user_id']
		email = row['email']
		access_token = row['access_token']
		result = get_personal_recos(user_id)
		result_file_name = 'output\\'+str(timesig)+'_'+str(user_id)+'.out'
		result_file = open(result_file_name,'w')
		
		rank=0
		#str= ""
		html= "\
		<html>\n\
		<head>\n\
			<title>Content recommendations</title>\n\
			<style>td{padding:5px;border:1px solid black;}</style>\n\
		</head>\n\
		<body>\n\
		<table>\n\
		"
		top10 = None
		for story in result:
			rank+=1
			html+= ("<tr><td>%s</td><td>%s</td><td>%s</td><td><a href='%s'>%s</a></td></tr>\n" % (rank,story.score,story.title,story.url,story.url) )
			#str+= ("%4s %15s %50s %s\r\n" % (rank,story.score,story.url,story.title) )
			if rank==10:
				top10 = str
		
		html+= "\n\
		</table>\n\
		</body>\n\
		</html>"
		if top10==None:	#incase we have less than 10
			top10 = str
		result_file.write(html)
		
		result_file.close()
		
		rename_file_to = ('content_recommendations_%s.html'% (str(timesig),))
		print "Task completed for ",email
		
		mail(email, 'Re: content recommendations test',top10,result_file_name,rename_file_to)
		
try:
	pass
except Exception as e:
	print "Task failed"
	print str(e.__doc__)
	print str(e.message)
	error_filename = ('output\\failure-'+str(timesig)+'.txt')
	f = open( error_filename, 'w' )
	f.write( str(e.__doc__) +"\n"+ str(e.message) ) 
	f.close()
	report_to_email = 'krishnancmf8@gmail.com'
	report =  ("FAILUUUUUURE!! Recommendation task failed for timesig %s, " % (timesig, ) )
	mail(report_to_email,report, report, error_filename, 'error_file.txt')
	exit(1)

print "Task completed successfully"
report_to_email = 'krishnancmf8@gmail.com'

subject = 'Cron job success: Personal recommendations successfully sent'
report =  ("Recommendations were completed for timesig %s, It took %s time " % (str(timesig), str( (time.time()-timesig) ) ) )
mail_text(report_to_email, subject, report )
