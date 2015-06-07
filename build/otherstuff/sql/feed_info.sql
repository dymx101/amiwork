-- phpMyAdmin SQL Dump
-- version 4.0.4
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Jun 06, 2015 at 02:16 PM
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

--
-- Dumping data for table `news_categories`
--

INSERT INTO `news_categories` (`category_id`, `name`, `level`, `parent_category`) VALUES
(1, 'IndianNews', 0, NULL),
(2, 'InternationalSports', 0, NULL),
(3, 'InternationalNews', 0, NULL),
(4, 'Humour', 0, NULL),
(5, 'TechCrunch_YourStory_TheVerge', 0, NULL);

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

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
