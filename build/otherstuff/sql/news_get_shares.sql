SET FOREIGN_KEY_CHECKS=0;
/* --- Simple table to keep track of the feeds we have --- */
DROP TABLE IF EXISTS news_feeds;
CREATE TABLE news_feeds(
	feed_id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
	name VARCHAR( 100 ) NOT NULL,
	url VARCHAR( 1000 ) NOT NULL,
	facebook_page_id BIGINT UNSIGNED,
);


/* --- Keeps track of stories --- */
DROP TABLE IF EXISTS news_stories;
CREATE TABLE news_stories(
    story_id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    url VARCHAR(1000),
    title VARCHAR(200),
    subtitle VARCHAR(500),
    feed_id INT UNSIGNED NOT NULL,
	created INT UNSIGNED,
    image VARCHAR(1000),
    FOREIGN KEY feed_id(feed_id) REFERENCES news_feeds(feed_id)
);

/* --- Set of stories which are actively in circulation. Primary key is normalized_score( for order ) , story_id ( for uniqueness )--- */
DROP TABLE IF EXISTS news_social_score_active;
CREATE TABLE news_social_score_active(
		normalized_score FLOAT NOT NULL,
		story_id INT UNSIGNED NOT NULL,
		raw_score	INT NOT NULL,
		PRIMARY KEY (normalized_score, story_id)	#We'll use rank as primary key instead
);

/* --- Set of all stories which were once in circulation. Contains stats for incase they come back from the dead --- */
DROP TABLE IF EXISTS news_social_score_all;
CREATE TABLE news_social_score_all(
		story_id INT UNSIGNED NOT NULL PRIMARY KEY,
		created INT NOT NULL,
		last_update INT NOT NULL DEFAULT 0,
		raw_score	INT NOT NULL DEFAULT 0,
		peak_score INT NOT NULL DEFAULT 0,
		total_shares INT NOT NULL DEFAULT 0,
		reflected_in_stats BOOLEAN DEFAULT FALSE,
		INDEX reflected_in_stats(reflected_in_stats)
);

/* --- Contains stats for every source that helps us normalize scores --- */
DROP TABLE IF EXISTS news_social_score_feed_statistics;
CREATE TABLE news_social_score_feed_statistics(
		feed_id INT UNSIGNED PRIMARY KEY,
		feed_n INT UNSIGNED NOT NULL DEFAULT 0,
		average_peak_score	FLOAT NOT NULL DEFAULT 0,
		std_deviation       FLOAT NOT NULL DEFAULT 0
 );
 
 
 /* --- Table for the update phase --- */
 
 /* --- The table which is truncated, populated and serves as the source for creating the new news_social_score_active table. That last index will slow us down ;_; --- */
 DROP TABLE IF EXISTS news_social_score_update;
 CREATE TABLE news_social_score_update(
	story_id INT UNSIGNED NOT NULL PRIMARY KEY,
	#url VARCHAR(200),
	last_update INT NOT NULL DEFAULT 0,
	old_raw_score	INT NOT NULL ,
	total_shares INT NOT NULL DEFAULT 0,
	new_raw_score INT NOT NULL DEFAULT 0,
	new_normalized_score FLOAT NOT NULL DEFAULT 0,
	created INT NOT NULL DEFAULT 0,
	state ENUM('READY', 'SCORE_COMPUTED','ABOVE_TRESHOLD','BELOW_TRESHOLD','CONSIDERED_IN_SET','UPDATING_STORIES','UPDATED_STORIES','UPDATED_STATS'),
	INDEX index_normalized_score(new_normalized_score),
	INDEX state_created(state,created)
 );
 
 
 /* --- Progress log for if needed --- */
 DROP TABLE IF EXISTS news_social_score_update_progress_log;
 CREATE TABLE news_social_score_update_progress_log(
	update_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
	stage VARCHAR(50) NOT NULL,
	start_time INT NOT NULL,
	end_time INT
 );
 
 /* --- Progress stats for if needed --- */
 DROP TABLE IF EXISTS news_social_score_update_stats;
 CREATE TABLE news_social_score_update_stats(
	update_id INT UNSIGNED NOT NULL,
	stat VARCHAR(50) NOT NULL,
	stat_value INT NOT NULL,
	PRIMARY KEY update_stat(update_id,stat)
 );
 
 SET FOREIGN_KEY_CHECKS=1;