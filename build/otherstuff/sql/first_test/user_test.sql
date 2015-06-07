DROP TABLE IF EXISTS first_test_users;
CREATE TABLE first_test_users(
	user_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
	email VARCHAR(500) NOT NULL,
	access_token VARCHAR(500)
);

/*Let's keep this 1-1 now 
#ALREADY EXISTS
DROP TABLE IF EXISTS first_test_news_story_category;
CREATE TABLE first_test_news_story_category(
	story_id INT UNSIGNED PRIMARY KEY,	
	category_id INT UNSIGNED
);
*/
DROP TABLE IF EXISTS first_test_feed_category;
CREATE TABLE first_test_feed_category(
	feed_id INT UNSIGNED PRIMARY KEY,	
	category_id INT UNSIGNED
);