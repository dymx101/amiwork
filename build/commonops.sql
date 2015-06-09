/* Live compute stats */
/* WARNING: DO NOT BE AN IDIOT. DO NOT RUN THIS IF YOU'VE GOT A HUGE NUMBER OF ROWS! */
SELECT t1.feed_id, sum_x,actual_sum_x,sum_x2,actual_sum_x2, feed_n,actual_feed_n FROM (
	SELECT feed_id, COUNT(*) as actual_feed_n,SUM(peak_score) as actual_sum_x,SUM(peak_score*peak_score) as actual_sum_x2 FROM news_social_score_all JOIN news_stories USING(story_id) GROUP BY feed_id
) t1 JOIN news_social_score_feed_statistics USING(feed_id);