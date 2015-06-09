class LocalConfig:
	socialscoreupdater_story_chunk_size = 5000				# DB transactions Process 1000 stories in a single go
	socialscoreupdater_treshold_normalized_score =  1		# Top 32% if it followed normal distribution 
	socialscoreupdater_treshold_age = 172800				# 2 days	=> Minimum time for which it remains in the active set
	socialscoreupdater_life_factor = 86400					# 12 hours => For a 30 minute update interval, You achieve ~0.12% initial score after 24 hours decay	#THIS IS STRONGLY TIED TO THE UPDATE INTERVAL. BE CAREFUL :|
	socialscoreupdater_stat_update_upper = 6000				# Should be close enough to give enough importance to the existing stats
	socialscoreupdater_stat_update_lower = 5000				# Should be big enough to not be swayed by a day of fame
	
	usercategoryinterests_base_read_count = 5				# The base read count that goes into scoring. read_count = (actual_read_count + base_read_count) is used for calculating interest
															#Also serves as the base of the logarithm taken while calculating interest interest = log(actual_read_count + base_read_count)
	
	opengraphscraper_urls_per_request = 20
	opengraphscraper_requests_per_batch = 20
	
