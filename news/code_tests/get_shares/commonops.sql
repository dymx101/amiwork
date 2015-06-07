TRUNCATE TABLE news_social_score_feed_statistics;
INSERT INTO news_social_score_feed_statistics (feed_id,average_peak_score,std_deviation,feed_n)VALUES ( 2,1000,400,9),
(3,100,20,8),(1,500,125,9);


/* Reset working tables sets */
SET FOREIGN_KEY_CHECKS = 0;
TRUNCATE TABLE news_social_score_all; 
TRUNCATE TABLE news_social_score_active; 
TRUNCATE TABLE news_social_score_feed_statistics; 
SET FOREIGN_KEY_CHECKS = 1;
INSERT INTO news_social_score_all (story_id,created) (SELECT story_id,created FROM news_stories);


/* Top 10 stories */
SELECT story_id,url,normalized_score FROM news_stories JOIN news_social_score_active USING(story_id) ORDER BY normalized_score DESC LIMIT 0,10



/* Full truncate */
/* 

SET FOREIGN_KEY_CHECKS = 0;
TRUNCATE TABLE news_stories;
TRUNCATE TABLE news_social_score_all;
TRUNCATE TABLE news_social_score_active;
TRUNCATE TABLE news_social_score_feed_statistics;
TRUNCATE TABLE news_social_score_update;
TRUNCATE TABLE news_feeds;
SET FOREIGN_KEY_CHECKS = 1;

*/