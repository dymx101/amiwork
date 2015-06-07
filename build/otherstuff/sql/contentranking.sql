-- phpMyAdmin SQL Dump
-- version 4.0.4
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Jun 05, 2015 at 12:09 PM
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
-- Table structure for table `news_categories`
--

CREATE TABLE IF NOT EXISTS `news_categories` (
  `category_id` int(10) unsigned NOT NULL,
  `name` varchar(100) DEFAULT NULL,
  `level` tinyint(4) NOT NULL DEFAULT '0',
  `parent_category` int(10) unsigned DEFAULT NULL,
  PRIMARY KEY (`category_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

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
) ENGINE=InnoDB  DEFAULT CHARSET=latin1;

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
  `peak_score` int(11) NOT NULL DEFAULT '0',
  `total_shares` int(11) NOT NULL DEFAULT '0',
  `reflected_in_stats` tinyint(1) DEFAULT '0',
  PRIMARY KEY (`story_id`),
  KEY `reflected_in_stats` (`reflected_in_stats`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `news_social_score_feed_statistics`
--

CREATE TABLE IF NOT EXISTS `news_social_score_feed_statistics` (
  `feed_id` int(10) unsigned NOT NULL,
  `average_peak_score` float NOT NULL DEFAULT '0',
  `std_deviation` float NOT NULL DEFAULT '0',
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
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

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
  `url` varchar(1000) DEFAULT NULL,
  `title` varchar(200) DEFAULT NULL,
  `subtitle` varchar(500) DEFAULT NULL,
  `feed_id` int(10) unsigned NOT NULL,
  `created` int(10) unsigned DEFAULT NULL,
  `image` varchar(1000) DEFAULT NULL,
  PRIMARY KEY (`story_id`),
  KEY `feed_id` (`feed_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1;

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
) ENGINE=InnoDB  DEFAULT CHARSET=latin1;

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
