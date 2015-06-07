INSERT INTO news_feeds VALUES(1,'bbc'),(2,'9gag'),(3,'engadget');

INSERT INTO `news_stories`	(`url`, 	`title`,	`subtitle`,`feed_id`, `created`,	`image`) 
			(SELECT			url, 		url, 		url, 		feed_id, 	UNIX_TIMESTAMP(), 		url 	FROM big_test);