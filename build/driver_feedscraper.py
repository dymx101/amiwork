from databaseinterface.databaseinterface import DatabaseInterface
from news.contentranking.classes.socialscoreupdater import SocialScoreUpdater
from mailsimple import mail_text
import time,feedparser,requests, urlparse

''' ---------------------------- '''
def xml_extract_info(file_contents):
	parsed =feedparser.parse(file_contents)
	results = []
	for item in parsed.entries:
		results.append( (item.title,item.link) )
	
	return results

def get_simple_url(long_url):
	parsed_url = urlparse.urlparse(long_url)
	simple_url = parsed_url.scheme + "://" + parsed_url.netloc + parsed_url.path
	return simple_url

''' ---------------------------- '''

failures = list()
admin_email = 'krishnancmf8@gmail.com'
try:

	dbi = DatabaseInterface.get_shared_instance()

	cursor = dbi.execute("SELECT feed_id,url,category_id FROM news_feeds JOIN first_test_feed_category USING(feed_id) ",None)
	rows = cursor.fetchall()

	dbi.autocommit(False)
	time_now = int(time.time())
	for row in rows:
		try:
			feed_id = row['feed_id']
			feed_url = row['url']
			category_id = row['category_id']
			#xml = requests.get(feed_url,{}).text
			xml = requests.get(feed_url).text
			results = xml_extract_info(xml)
			for result in results:
				title = result[0]
				url = get_simple_url(result[1])
				#Check if it is in our DB:
				cursor = dbi.execute("SELECT COUNT(*) as row_count FROM news_stories WHERE url=%s",(url,))
				
				if int(cursor.fetchone()['row_count']) == 0:						
					#It's a new story, INSERT!
					insert_values = ( url,title.encode('utf-8'),title.encode('utf-8'),feed_id,None,time_now )
					cursor = dbi.execute("INSERT INTO news_stories (url,title,subtitle,feed_id,image,created) VALUES(%s,%s,%s,%s,%s,%s) ON DUPLICATE KEY UPDATE story_id=story_id",insert_values)
					story_id = cursor.lastrowid
					dbi.execute("INSERT INTO news_story_categories (story_id,category_id) VALUES(%s,%s) ON DUPLICATE KEY UPDATE story_id=story_id",(story_id,category_id))
					#Also add it to the global and active sets
					SocialScoreUpdater.add_new_story(story_id)
					dbi.commit()
			print "Done with ",feed_url
			
		except Exception as e:
			print feed_url, " failed: ",str(e.__doc__)+"\n"+ str(e.message) 
			failures.append( (feed_url, str(e.__doc__) +"\n"+ str(e.message) ) )	
	
	
	''' Prepare and send the report '''
	if len(failures)==0:
		subject = "Feed scrape was completed Succesfully ( 0 failures )"
		report = "Dance dance :D"
	else:
		subject = ("Feed scrape (FAILURES!) was completed with %s failures" %  (len(failures),))
		report = "The following urls failed"
		for failure in failures:
			report+= ("-----------------\n%s:\n%s"%(failure[0],failure[1]) )
	
	mail_text(admin_email, subject, report )
			
	dbi.autocommit(True)
	
	
except Exception as e:
	print "\n------ERROOOOOOOOOOOOOOOR!!!---------\n"
	print e.__doc__ +"\n"+ str(e.message )
	subject='COMPLETE FAILURE OF FEEDSCRAPE!'
	report = e.__doc__ +"\n"+ e.message 
	mail_text(admin_email, subject, report )
