class GlobalConfig:
	mysql_user= "root"
	mysql_password= ""
	mysql_database= "ami_news"
	mysql_host= 'localhost'
	
	facebook_app_token = "494994220569217|1OG6YypCV2pM3dIlAGOZdCM1TI0"	# Used for scraping and so on
	
	socialscoreupdater_story_chunk_size = 5000				# DB transactions Process 1000 stories in a single go
	socialscoreupdater_treshold_normalized_score	=  1.5	# Top 14% if it followed normal distribution 
	socialscoreupdater_treshold_age = 172800				# 2 days
	socialscoreupdater_life_factor = 86400 					# 1 day
	socialscoreupdater_stat_update_upper = 6000				# Should be close enough to give enough importance to the existing stats
	socialscoreupdater_stat_update_lower = 5000				# Should be big enough to not be swayed by a day of fame

	opengraphscraper_urls_per_request = 20
	opengraphscraper_requests_per_batch = 50
