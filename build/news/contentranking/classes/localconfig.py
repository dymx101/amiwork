class LocalConfig:
	socialscoreupdater_story_chunk_size = 5000				# DB transactions Process 1000 stories in a single go
	socialscoreupdater_treshold_normalized_score =  0.5
	socialscoreupdater_treshold_age = 172800				# 2 days	=> Minimum time for which it remains in the active set
	socialscoreupdater_life_factor = 28800					# 12 hours => For a 30 minute update interval, You achieve ~0.12% initial score after 24 hours decay	#THIS IS STRONGLY TIED TO THE UPDATE INTERVAL. BE CAREFUL :|
	socialscoreupdater_stat_update_upper = 6000				# Should be close enough to give enough importance to the existing stats
	socialscoreupdater_stat_update_lower = 5000				# Should be big enough to not be swayed by a day of fame
	
	usercategoryinterests_base_read_count = 5				# The base read count that goes into scoring. read_count = (actual_read_count + base_read_count) is used for calculating interest
															#Also serves as the base of the logarithm taken while calculating interest interest = log(actual_read_count + base_read_count)
	personalization_scale_point = 1
	personalization_scale_how_many = 13
	''' You want the number of content from each feed to having a score >= scale_point to be equal to personalization_score_how_many
	
		(Had they all followed exponential distribution with mean 0 :|. 
			Exponential gave a decent RMSE when considering CDF for small values ( top 2%, 5%,etc).
			Lognormal performed really well for top 10%,20%
	'''
	personalization_feed_size_factor_log_base = 10
	
	
	opengraphscraper_urls_per_request = 20
	opengraphscraper_requests_per_batch = 20
	
