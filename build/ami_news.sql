-- phpMyAdmin SQL Dump
-- version 4.0.4
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Jun 07, 2015 at 05:08 PM
-- Server version: 5.6.12-log
-- PHP Version: 5.4.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `ami_news`
--
CREATE DATABASE IF NOT EXISTS `ami_news` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;
USE `ami_news`;

-- --------------------------------------------------------

--
-- Table structure for table `cache_news_user_interests`
--

CREATE TABLE IF NOT EXISTS `cache_news_user_interests` (
  `user_id` int(10) unsigned NOT NULL,
  `category_id` int(10) unsigned NOT NULL,
  `read_count` float DEFAULT NULL,
  `unnormalized_interest` float NOT NULL,
  `interest` float NOT NULL,
  `cached_time` int(10) unsigned DEFAULT NULL,
  PRIMARY KEY (`user_id`,`category_id`),
  KEY `cached_time` (`cached_time`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `first_test_feed_category`
--

CREATE TABLE IF NOT EXISTS `first_test_feed_category` (
  `feed_id` int(10) unsigned NOT NULL,
  `category_id` int(10) unsigned DEFAULT NULL,
  PRIMARY KEY (`feed_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `first_test_feed_category`
--

INSERT INTO `first_test_feed_category` (`feed_id`, `category_id`) VALUES
(1, 1),
(2, 1),
(3, 1),
(4, 2),
(5, 3),
(6, 3),
(7, 3),
(8, 4),
(9, 4),
(10, 4),
(11, 5),
(12, 5),
(13, 5);

-- --------------------------------------------------------

--
-- Table structure for table `first_test_users`
--

CREATE TABLE IF NOT EXISTS `first_test_users` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `email` varchar(500) NOT NULL,
  `access_token` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `first_test_users`
--

INSERT INTO `first_test_users` (`user_id`, `email`, `access_token`) VALUES
(1, 'krishnancmf8@gmail.com', 'CAACEdEose0cBAE7jD2CdffHkZANoZAeeYiYkgDu0SZBL0zVaqZAAqTGWXmn3ruOa41Skz7YSsgNZA49IFxvXIZAxx6tqdIGkHZBVLKIDKRuuLZBIfZAGJcYDIn8ZCK5nxyDNXUGPXI0atGK9JR1XW7r2rMy1C5eiVyUFqrA3pcMCV6JjEWZAJWuRPn3qSNuPBTBTDNoTmiOBfY6haZBZBBWg66F6y');

-- --------------------------------------------------------

--
-- Table structure for table `news_categories`
--

CREATE TABLE IF NOT EXISTS `news_categories` (
  `category_id` int(10) unsigned NOT NULL,
  `name` varchar(100) DEFAULT NULL,
  `level` tinyint(4) NOT NULL DEFAULT '0',
  `parent_category` int(10) unsigned DEFAULT NULL,
  PRIMARY KEY (`category_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `news_categories`
--

INSERT INTO `news_categories` (`category_id`, `name`, `level`, `parent_category`) VALUES
(1, 'IndianNews', 0, NULL),
(2, 'InternationalSports', 0, NULL),
(3, 'InternationalNews', 0, NULL),
(4, 'Humour', 0, NULL),
(5, 'TechCrunch_YourStory_TheVerge', 0, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `news_feeds`
--

CREATE TABLE IF NOT EXISTS `news_feeds` (
  `feed_id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `url` varchar(1000) NOT NULL,
  `facebook_page_id` bigint(18) unsigned DEFAULT NULL,
  PRIMARY KEY (`feed_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=14 ;

--
-- Dumping data for table `news_feeds`
--

INSERT INTO `news_feeds` (`feed_id`, `name`, `url`, `facebook_page_id`) VALUES
(1, 'TheHindu', 'http://www.thehindu.com/?service=rss', 163974433696568),
(2, 'TimesOfIndia', 'http://dynamic.feedsportal.com/pf/555218/http://toi.timesofindia.indiatimes.com/rssfeedstopstories.cms', 26781952138),
(3, 'EconomicTimes', 'http://economictimes.indiatimes.com/rssfeedsdefault.cms', 21540067693),
(4, 'BBCSport', 'http://feeds.bbci.co.uk/sport/0/rss.xml?edition=int', 317278538359186),
(5, 'BBCNews', 'http://feeds.bbci.co.uk/news/rss.xml?edition=int', 228735667216),
(6, 'NewyorkTimes', 'http://rss.nytimes.com/services/xml/rss/nyt/InternationalHome.xml', 5281959998),
(7, 'HuffingtonPost', 'http://www.huffingtonpost.com/feeds/index.xml', 18468761129),
(8, '9gag', 'http://9gag-rss.com/api/rss/get?code=9GAG&format=2', 21785951839),
(9, 'Scoopwoop', 'http://www.scoopwhoop.com/feed/', 110141895861579),
(10, 'TheViralFever', 'http://www.theviralfever.com/?feed=rss2', 230013210408109),
(11, 'TheVerge', 'http://www.theverge.com/rss/frontpage', 193742123995472),
(12, 'Techcrunch', 'http://feeds.feedburner.com/TechCrunch/', 8062627951),
(13, 'YourStory', 'http://yourstory.com/feed/', 467687645161);

-- --------------------------------------------------------

--
-- Table structure for table `news_social_score_active`
--

CREATE TABLE IF NOT EXISTS `news_social_score_active` (
  `normalized_score` float NOT NULL,
  `story_id` int(10) unsigned NOT NULL,
  `raw_score` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `news_social_score_all`
--

CREATE TABLE IF NOT EXISTS `news_social_score_all` (
  `story_id` int(10) unsigned NOT NULL,
  `created` int(11) NOT NULL,
  `last_update` int(11) NOT NULL DEFAULT '0',
  `raw_score` int(11) NOT NULL DEFAULT '0',
  `prev_peak_score` int(11) NOT NULL DEFAULT '0',
  `peak_score` int(11) NOT NULL DEFAULT '0',
  `total_shares` int(11) NOT NULL DEFAULT '0',
  `reflected_in_stats` enum('NEVER','OUTDATED','UPTODATE') DEFAULT 'NEVER',
  PRIMARY KEY (`story_id`),
  KEY `reflected_in_stats` (`reflected_in_stats`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `news_social_score_feed_statistics`
--

CREATE TABLE IF NOT EXISTS `news_social_score_feed_statistics` (
  `feed_id` int(10) unsigned NOT NULL,
  `sum_x` bigint(20) NOT NULL DEFAULT '0',
  `sum_x2` bigint(20) NOT NULL DEFAULT '0',
  `feed_n` int(10) unsigned NOT NULL DEFAULT '0',
  PRIMARY KEY (`feed_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `news_social_score_update`
--

CREATE TABLE IF NOT EXISTS `news_social_score_update` (
  `story_id` int(10) unsigned NOT NULL,
  `last_update` int(11) NOT NULL DEFAULT '0',
  `old_raw_score` int(11) NOT NULL,
  `total_shares` int(11) NOT NULL DEFAULT '0',
  `new_raw_score` int(11) NOT NULL DEFAULT '0',
  `new_normalized_score` float NOT NULL DEFAULT '0',
  `created` int(11) NOT NULL DEFAULT '0',
  `state` enum('READY','SCORE_COMPUTED','ABOVE_TRESHOLD','BELOW_TRESHOLD','CONSIDERED_IN_SET','UPDATED_STORIES','UPDATED_STATS') DEFAULT NULL,
  PRIMARY KEY (`story_id`),
  KEY `index_normalized_score` (`new_normalized_score`),
  KEY `state_created` (`state`,`created`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `news_social_score_update_progress_log`
--

CREATE TABLE IF NOT EXISTS `news_social_score_update_progress_log` (
  `update_id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `stage` varchar(50) NOT NULL,
  `start_time` int(11) NOT NULL,
  `end_time` int(11) DEFAULT NULL,
  PRIMARY KEY (`update_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `news_social_score_update_stats`
--

CREATE TABLE IF NOT EXISTS `news_social_score_update_stats` (
  `update_id` int(10) unsigned NOT NULL,
  `stat` varchar(50) NOT NULL,
  `stat_value` int(11) NOT NULL,
  PRIMARY KEY (`update_id`,`stat`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `news_stories`
--

CREATE TABLE IF NOT EXISTS `news_stories` (
  `story_id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `url` varchar(750) DEFAULT NULL,
  `title` varchar(200) DEFAULT NULL,
  `subtitle` varchar(500) DEFAULT NULL,
  `feed_id` int(10) unsigned NOT NULL,
  `created` int(10) unsigned DEFAULT NULL,
  `image` varchar(1000) DEFAULT NULL,
  PRIMARY KEY (`story_id`),
  UNIQUE KEY `url` (`url`),
  KEY `feed_id` (`feed_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `news_story_categories`
--

CREATE TABLE IF NOT EXISTS `news_story_categories` (
  `story_id` int(10) unsigned NOT NULL,
  `category_id` int(10) unsigned NOT NULL,
  PRIMARY KEY (`story_id`,`category_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `news_user_interests_read_count`
--

CREATE TABLE IF NOT EXISTS `news_user_interests_read_count` (
  `row_id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `user_id` int(10) unsigned NOT NULL,
  `category_id` int(10) unsigned NOT NULL,
  `read_count` float NOT NULL DEFAULT '0',
  PRIMARY KEY (`row_id`),
  UNIQUE KEY `user_category` (`user_id`,`category_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE IF NOT EXISTS `users` (
  `user_id` int(11) NOT NULL,
  `email` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`user_id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`user_id`, `email`) VALUES
(1, 'krishnancmf8@gmail.com');

--
-- Constraints for dumped tables
--

--
-- Constraints for table `news_stories`
--
ALTER TABLE `news_stories`
  ADD CONSTRAINT `news_stories_ibfk_1` FOREIGN KEY (`feed_id`) REFERENCES `news_feeds` (`feed_id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
