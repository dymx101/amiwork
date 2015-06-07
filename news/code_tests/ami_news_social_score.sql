-- phpMyAdmin SQL Dump
-- version 4.0.4
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Jun 03, 2015 at 07:36 AM
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
-- Table structure for table `big_test`
--

CREATE TABLE IF NOT EXISTS `big_test` (
  `feed_id` int(1) DEFAULT NULL,
  `url` varchar(97) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `big_test`
--

INSERT INTO `big_test` (`feed_id`, `url`) VALUES
(1, 'http://www.bbc.co.uk/news/world-us-canada-32986950'),
(1, 'http://www.bbc.co.uk/news/world-asia-china-32987573'),
(1, 'http://www.bbc.co.uk/news/world-us-canada-32982140'),
(1, 'http://www.bbc.co.uk/news/world-europe-32987562'),
(1, 'http://www.bbc.co.uk/news/world-europe-32985554'),
(1, 'http://www.bbc.co.uk/news/business-32970412'),
(1, 'http://www.bbc.co.uk/news/world-us-canada-32984591'),
(1, 'http://www.bbc.co.uk/news/world-us-canada-32982217'),
(1, 'http://www.bbc.co.uk/news/world-us-canada-32980208'),
(1, 'http://www.bbc.co.uk/news/world-europe-32974603'),
(1, 'http://www.bbc.co.uk/news/science-environment-32976838'),
(1, 'http://www.bbc.co.uk/news/science-environment-32976352'),
(1, 'http://www.bbc.co.uk/sport/0/football/32975524'),
(1, 'http://www.bbc.co.uk/news/world-asia-32987675'),
(1, 'http://www.bbc.co.uk/news/world-africa-32987472'),
(1, 'http://www.bbc.co.uk/news/world-asia-32987198'),
(1, 'http://www.bbc.co.uk/news/world-latin-america-32982248'),
(1, 'http://www.bbc.co.uk/news/world-us-canada-32985385'),
(1, 'http://www.bbc.co.uk/news/uk-32985384'),
(1, 'http://www.bbc.co.uk/news/world-32985895'),
(1, 'http://www.bbc.co.uk/news/world-middle-east-32973202'),
(1, 'http://www.bbc.co.uk/news/uk-politics-32972880'),
(1, 'http://www.bbc.co.uk/news/world-europe-32975794'),
(1, 'http://www.bbc.co.uk/news/world-32973203'),
(1, 'http://www.bbc.co.uk/news/science-environment-32901834'),
(1, 'http://www.bbc.co.uk/news/business-32852468'),
(1, 'http://www.bbc.co.uk/sport/0/cricket/32986595'),
(1, 'http://www.bbc.co.uk/newsbeat/32973341'),
(1, 'http://www.bbc.co.uk/news/business-32969992'),
(1, 'http://www.bbc.co.uk/news/business-11876811'),
(1, 'http://www.bbc.co.uk/news/technology-32982609'),
(1, 'http://www.bbc.co.uk/news/technology-32973815'),
(1, 'http://www.bbc.co.uk/news/entertainment-arts-32973176'),
(1, 'http://www.bbc.co.uk/news/entertainment-arts-32971919'),
(1, 'http://www.bbc.co.uk/news/science-environment-32958033'),
(1, 'http://www.bbc.co.uk/news/science-environment-32967386'),
(1, 'http://www.bbc.co.uk/news/world-asia-32969054'),
(1, 'http://www.bbc.co.uk/news/world-us-canada-32969338'),
(1, 'http://www.bbc.co.uk/sport/0/football/32982449'),
(1, 'http://www.bbc.co.uk/sport/0/cricket/32984979'),
(1, 'http://www.bbc.co.uk/news/magazine-32960509'),
(1, 'http://www.bbc.co.uk/news/magazine-32966907'),
(1, 'http://www.bbc.co.uk/news/world-asia-32971952'),
(1, 'http://www.bbc.co.uk/news/world-europe-32960470'),
(1, 'http://www.bbc.co.uk/news/world-africa-32978735'),
(1, 'http://www.bbc.co.uk/news/entertainment-arts-32975956'),
(1, 'http://www.bbc.co.uk/news/world-europe-32972406'),
(1, 'http://www.bbc.co.uk/news/world-latin-america-32973483'),
(1, 'http://www.bbc.co.uk/news/world-middle-east-32962870'),
(1, 'http://www.bbc.co.uk/news/world-us-canada-32979612'),
(1, 'http://www.bbc.co.uk/news/education-32978355'),
(1, 'http://www.bbc.co.uk/news/uk-england-nottinghamshire-32986664'),
(1, 'http://www.bbc.co.uk/news/uk-england-stoke-staffordshire-32987550'),
(1, 'http://www.bbc.co.uk/news/uk-politics-32985571'),
(1, 'http://www.bbc.co.uk/news/world-africa-32448072'),
(1, 'http://www.bbc.co.uk/news/in-pictures-32960657'),
(1, 'http://www.bbc.co.uk/news/in-pictures-32960656'),
(1, 'http://www.bbc.co.uk/news/science-environment-32935898'),
(1, 'http://www.bbc.co.uk/news/magazine-32888643'),
(1, 'http://www.bbc.co.uk/news/uk-scotland-south-scotland-32897366'),
(1, 'http://www.bbc.co.uk/news/entertainment-arts-32851421'),
(1, 'http://www.bbc.co.uk/news/world-asia-india-32733902'),
(1, 'http://www.bbc.co.uk/news/magazine-32839660'),
(1, 'http://www.bbc.co.uk/news/world-europe-32972893'),
(1, 'http://www.bbc.co.uk/news/world-asia-32811867'),
(1, 'http://www.bbc.co.uk/news/magazine-32976515'),
(1, 'http://www.bbc.co.uk/news/magazine-32965494'),
(1, 'http://www.bbc.co.uk/news/magazine-32965229'),
(2, 'http://9gag.com/trending/'),
(2, 'http://9gag.com/gag/ae0vm7B'),
(2, 'http://9gag.com/gag/anKpB4o'),
(2, 'http://9gag.com/gag/a2YBYoE'),
(2, 'http://9gag.com/gag/ae0vx5q'),
(2, 'http://9gag.com/gag/aKPrQb1'),
(2, 'http://9gag.com/gag/avg3d0O'),
(2, 'http://9gag.com/gag/ay0OKqV'),
(2, 'http://9gag.com/gag/ay0g088'),
(2, 'http://9gag.com/gag/aWWwPK3'),
(2, 'http://9gag.com/gag/a7y4y7z'),
(2, 'http://9gag.com/gag/aKPr9V3'),
(2, 'http://9gag.com/gag/aB3q3YN'),
(2, 'http://9gag.com/gag/ao0bDvn'),
(2, 'http://9gag.com/gag/aE1LXQK'),
(2, 'http://9gag.com/gag/aWWwXzZ'),
(2, 'http://9gag.com/gag/aE1rGde'),
(2, 'http://9gag.com/gag/aKPrGgZ'),
(2, 'http://9gag.com/gag/ap0y00M'),
(2, 'http://9gag.com/gag/aGwWyV5'),
(2, 'http://9gag.com/gag/aMr3opM'),
(2, 'http://9gag.com/gag/ae0o00O'),
(2, 'http://9gag.com/gag/axZX7Kp'),
(2, 'http://9gag.com/gag/aB3q33Z'),
(2, 'http://9gag.com/gag/a4dDBYm'),
(2, 'http://9gag.com/gag/a1eG6yb'),
(2, 'http://9gag.com/gag/aRP5PrB'),
(2, 'http://9gag.com/gag/ay0OXyX'),
(2, 'http://9gag.com/gag/adYZYY9'),
(2, 'http://9gag.com/gag/axZXArp'),
(2, 'http://9gag.com/gag/avg3jqO'),
(3, 'http://www.engadget.com/2015/06/03/steam-will-refund-nearly-any-online-purchase-within-two-weeks/'),
(3, 'http://www.engadget.com/2015/06/02/heroes-of-the-storm-out-today/'),
(3, 'http://www.engadget.com/2015/06/02/amd-sixth-gen-a-chip/'),
(3, 'http://www.engadget.com/2015/06/02/gravity-ghost-indie-game-ps4/'),
(3, 'http://www.engadget.com/2015/06/02/logitech-harmony-ps4-control/'),
(3, 'http://www.engadget.com/2015/06/02/magic-leap-augmented-reality-platform/'),
(3, 'http://www.engadget.com/2015/06/02/jxe-streams-metal-gear/'),
(3, 'http://www.engadget.com/2015/06/02/msi-gaming-laptop-concept-eye-tracking/'),
(3, 'http://www.engadget.com/2015/06/02/henry-oculus-story-studio/'),
(3, 'http://www.engadget.com/2015/06/02/amazon-fire-tv-gamefly-app/'),
(3, 'http://www.engadget.com/2015/06/02/youtube-e3-hub/'),
(3, 'http://www.engadget.com/2015/06/02/nintendo-android-rumor-squashed/'),
(3, 'http://www.engadget.com/2015/06/02/lego-dimensions-vs-disney-infinity/'),
(3, 'http://www.engadget.com/2015/06/02/ps4-1tb-fcc/'),
(3, 'http://www.engadget.com/2015/06/02/acer-intel-predator/'),
(3, 'http://www.engadget.com/2015/06/01/xbox-one-indie-pack-australia/'),
(3, 'http://www.engadget.com/2015/06/01/nintendo-new-games-e3-2015/'),
(3, 'http://www.engadget.com/2015/06/01/call-of-duty-advanced-warfare-carrier/'),
(3, 'http://www.engadget.com/2015/06/01/xcom-2-announcement/'),
(3, 'http://www.engadget.com/2015/06/01/lego-worlds/'),
(3, 'http://www.engadget.com/2015/06/01/why-rock-band-4-got-the-gang-back-together/'),
(3, 'http://www.engadget.com/2015/06/01/nvidia-g-sync-comes-to-laptops/'),
(3, 'http://www.engadget.com/2015/06/01/nintendo-nx-android/'),
(3, 'http://www.engadget.com/2015/06/01/agar-io/'),
(3, 'http://www.engadget.com/2015/05/31/nvidia-gtx-980-ti/');

-- --------------------------------------------------------

--
-- Table structure for table `news_feeds`
--

CREATE TABLE IF NOT EXISTS `news_feeds` (
  `feed_id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`feed_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

--
-- Dumping data for table `news_feeds`
--

INSERT INTO `news_feeds` (`feed_id`, `name`) VALUES
(1, 'bbc'),
(2, '9gag'),
(3, 'engadget');

-- --------------------------------------------------------

--
-- Table structure for table `news_social_score_active`
--

CREATE TABLE IF NOT EXISTS `news_social_score_active` (
  `normalized_score` float NOT NULL,
  `story_id` int(10) unsigned NOT NULL,
  `raw_score` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `news_social_score_active`
--

INSERT INTO `news_social_score_active` (`normalized_score`, `story_id`, `raw_score`) VALUES
(5.01825, 44, 33779),
(4.55758, 28, 30898),
(3.39002, 39, 23596),
(3.35229, 119, 5641),
(2.60133, 81, 39),
(2.60133, 85, 39),
(1.93357, 122, 3709),
(1.8184, 124, 3552),
(1.40887, 80, 26),
(1.40887, 86, 26),
(1.31807, 52, 10637),
(1.22542, 89, 24),
(1.21027, 113, 2723),
(1.16531, 58, 9682),
(0.897027, 37, 8004),
(0.858506, 73, 20),
(0.646004, 1, 6434),
(0.525843, 35, 5682),
(0.479633, 114, 1728),
(0.238289, 108, 1399),
(0.124684, 97, 12),
(0.0881882, 65, 2945),
(0.0330152, 88, 11),
(-0.00384766, 53, 2370),
(-0.0241426, 2, 2243),
(-0.0358072, 3, 2170),
(-0.0479512, 13, 2094),
(-0.0587708, 76, 10),
(-0.0587708, 78, 10),
(-0.0587708, 96, 10),
(-0.0767122, 8, 1914),
(-0.0918172, 121, 949),
(-0.121134, 49, 1636),
(-0.1312, 33, 1573),
(-0.150498, 70, 9),
(-0.150498, 87, 9),
(-0.154171, 111, 864),
(-0.156127, 36, 1417),
(-0.16843, 59, 1340),
(-0.182045, 109, 826),
(-0.185527, 46, 1233),
(-0.193038, 56, 1186),
(-0.195913, 48, 1168),
(-0.197671, 45, 1157),
(-0.229309, 51, 959),
(-0.242226, 90, 8),
(-0.260787, 30, 763),
(-0.26606, 38, 730),
(-0.284276, 42, 616),
(-0.290348, 32, 578),
(-0.293064, 55, 561),
(-0.298816, 11, 525),
(-0.309687, 110, 653),
(-0.313836, 63, 431),
(-0.324862, 29, 362),
(-0.326779, 41, 350),
(-0.327897, 12, 343),
(-0.333954, 83, 7),
(-0.333954, 98, 7),
(-0.335088, 9, 298),
(-0.347072, 17, 223),
(-0.347099, 104, 602),
(-0.349149, 43, 210),
(-0.350587, 60, 201),
(-0.350747, 62, 200),
(-0.353783, 34, 181),
(-0.3557, 10, 169),
(-0.360654, 27, 138),
(-0.361772, 31, 131),
(-0.365128, 47, 110),
(-0.365607, 6, 107),
(-0.366566, 66, 101),
(-0.367365, 54, 96),
(-0.367525, 50, 95),
(-0.367844, 64, 93),
(-0.368324, 19, 90),
(-0.369602, 4, 82),
(-0.369762, 18, 81),
(-0.370241, 67, 78),
(-0.370241, 61, 78),
(-0.371519, 15, 70),
(-0.373756, 26, 56),
(-0.373916, 40, 55),
(-0.373916, 7, 55),
(-0.373916, 68, 55),
(-0.375354, 23, 46),
(-0.375354, 25, 46),
(-0.375514, 22, 45),
(-0.375993, 5, 42),
(-0.376313, 57, 40),
(-0.377911, 24, 30),
(-0.379349, 16, 21),
(-0.380148, 20, 16),
(-0.380148, 21, 16),
(-0.381266, 14, 9),
(-0.382311, 118, 554),
(-0.416055, 115, 508),
(-0.425681, 91, 6),
(-0.517409, 74, 5),
(-0.518755, 120, 368),
(-0.521689, 123, 364),
(-0.522421, 100, 363),
(-0.544429, 105, 333),
(-0.562035, 107, 309),
(-0.596513, 112, 262),
(-0.609137, 82, 4),
(-0.617786, 116, 233),
(-0.633924, 102, 211),
(-0.647129, 101, 193),
(-0.651531, 117, 187),
(-0.664001, 106, 170),
(-0.691877, 103, 132),
(-0.700864, 77, 3),
(-0.700864, 79, 3),
(-0.792592, 71, 2),
(-0.792592, 75, 2),
(-0.88432, 95, 1),
(-0.975989, 72, 0),
(-0.975989, 84, 0),
(-0.975989, 92, 0),
(-0.975989, 93, 0),
(-0.975989, 94, 0),
(-0.975989, 99, 0);

-- --------------------------------------------------------

--
-- Table structure for table `news_social_score_active_old`
--

CREATE TABLE IF NOT EXISTS `news_social_score_active_old` (
  `normalized_score` float NOT NULL,
  `story_id` int(10) unsigned NOT NULL,
  `raw_score` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `news_social_score_active_old`
--

INSERT INTO `news_social_score_active_old` (`normalized_score`, `story_id`, `raw_score`) VALUES
(33801, 44, 33801),
(30910, 28, 30910),
(23585, 39, 23585),
(10620, 52, 10620),
(9689, 58, 9689),
(8010, 37, 8010),
(6427, 1, 6427),
(5685, 35, 5685),
(5646, 119, 5646),
(3712, 122, 3712),
(3555, 124, 3555),
(2936, 65, 2936),
(2725, 113, 2725),
(2348, 53, 2348),
(2241, 2, 2241),
(2170, 3, 2170),
(2096, 13, 2096),
(1910, 8, 1910),
(1730, 114, 1730),
(1638, 49, 1638),
(1575, 33, 1575),
(1418, 36, 1418),
(1400, 108, 1400),
(1342, 59, 1342),
(1233, 46, 1233),
(1188, 56, 1188),
(1168, 48, 1168),
(1159, 45, 1159),
(956, 51, 956),
(951, 121, 951),
(866, 111, 866),
(826, 109, 826),
(764, 30, 764),
(731, 38, 731),
(654, 110, 654),
(617, 42, 617),
(602, 104, 602),
(578, 32, 578),
(562, 55, 562),
(555, 118, 555),
(526, 11, 526),
(509, 115, 509),
(430, 63, 430),
(369, 120, 369),
(365, 123, 365),
(363, 29, 363),
(360, 100, 360),
(351, 41, 351),
(343, 12, 343),
(333, 105, 333),
(310, 107, 310),
(299, 9, 299),
(263, 112, 263),
(234, 116, 234),
(223, 17, 223),
(211, 43, 211),
(211, 102, 211),
(202, 60, 202),
(201, 62, 201),
(194, 101, 194),
(188, 117, 188),
(182, 34, 182),
(171, 106, 171),
(170, 10, 170),
(139, 27, 139),
(133, 103, 133),
(131, 31, 131),
(111, 47, 111),
(108, 6, 108),
(102, 66, 102),
(97, 54, 97),
(96, 50, 96),
(94, 64, 94),
(91, 19, 91),
(83, 4, 83),
(82, 18, 82),
(79, 61, 79),
(78, 67, 78),
(71, 15, 71),
(56, 7, 56),
(56, 26, 56),
(56, 68, 56),
(54, 40, 54),
(47, 23, 47),
(47, 25, 47),
(46, 22, 46),
(43, 5, 43),
(41, 57, 41),
(40, 81, 40),
(40, 85, 40),
(31, 24, 31),
(27, 80, 27),
(27, 86, 27),
(25, 89, 25),
(22, 16, 22),
(21, 73, 21),
(17, 20, 17),
(17, 21, 17),
(13, 97, 13),
(11, 76, 11),
(11, 78, 11),
(11, 88, 11),
(11, 96, 11),
(10, 14, 10),
(10, 70, 10),
(10, 87, 10),
(9, 90, 9),
(8, 83, 8),
(8, 98, 8),
(7, 91, 7),
(6, 74, 6),
(5, 82, 5),
(4, 77, 4),
(4, 79, 4),
(3, 71, 3),
(3, 75, 3),
(2, 95, 2),
(1, 84, 1),
(1, 92, 1),
(1, 99, 1),
(0, 72, 0),
(0, 93, 0),
(0, 94, 0);

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

--
-- Dumping data for table `news_social_score_all`
--

INSERT INTO `news_social_score_all` (`story_id`, `created`, `last_update`, `raw_score`, `peak_score`, `total_shares`, `reflected_in_stats`) VALUES
(1, 1433313932, 1433316697, 6434, 6434, 6439, 1),
(2, 1433313932, 1433316697, 2243, 2243, 2245, 1),
(3, 1433313932, 1433316697, 2170, 2170, 2172, 1),
(4, 1433313932, 1433316697, 82, 83, 83, 1),
(5, 1433313932, 1433316697, 42, 43, 43, 1),
(6, 1433313932, 1433316697, 107, 108, 108, 1),
(7, 1433313932, 1433316697, 55, 56, 56, 1),
(8, 1433313932, 1433316697, 1914, 1914, 1916, 1),
(9, 1433313932, 1433316697, 298, 299, 299, 1),
(10, 1433313932, 1433316697, 169, 170, 170, 1),
(11, 1433313932, 1433316697, 525, 526, 526, 1),
(12, 1433313932, 1433316697, 343, 343, 344, 1),
(13, 1433313932, 1433316697, 2094, 2096, 2096, 1),
(14, 1433313932, 1433316697, 9, 10, 10, 1),
(15, 1433313932, 1433316697, 70, 71, 71, 1),
(16, 1433313932, 1433316697, 21, 22, 22, 1),
(17, 1433313932, 1433316697, 223, 223, 224, 1),
(18, 1433313932, 1433316697, 81, 82, 82, 1),
(19, 1433313932, 1433316697, 90, 91, 91, 1),
(20, 1433313932, 1433316697, 16, 17, 17, 1),
(21, 1433313932, 1433316697, 16, 17, 17, 1),
(22, 1433313932, 1433316697, 45, 46, 46, 1),
(23, 1433313932, 1433316697, 46, 47, 47, 1),
(24, 1433313932, 1433316697, 30, 31, 31, 1),
(25, 1433313932, 1433316697, 46, 47, 47, 1),
(26, 1433313932, 1433316697, 56, 56, 57, 1),
(27, 1433313932, 1433316697, 138, 139, 139, 1),
(28, 1433313932, 1433316697, 30898, 30910, 30919, 1),
(29, 1433313932, 1433316697, 362, 363, 363, 1),
(30, 1433313932, 1433316697, 763, 764, 764, 1),
(31, 1433313932, 1433316697, 131, 131, 132, 1),
(32, 1433313932, 1433316697, 578, 578, 579, 1),
(33, 1433313932, 1433316697, 1573, 1575, 1575, 1),
(34, 1433313932, 1433316697, 181, 182, 182, 1),
(35, 1433313932, 1433316697, 5682, 5685, 5687, 1),
(36, 1433313932, 1433316697, 1417, 1418, 1419, 1),
(37, 1433313932, 1433316697, 8004, 8010, 8010, 1),
(38, 1433313932, 1433316697, 730, 731, 731, 1),
(39, 1433313932, 1433316697, 23596, 23596, 23612, 1),
(40, 1433313932, 1433316697, 55, 55, 56, 1),
(41, 1433313932, 1433316697, 350, 351, 351, 1),
(42, 1433313932, 1433316697, 616, 617, 617, 1),
(43, 1433313932, 1433316697, 210, 211, 211, 1),
(44, 1433313932, 1433316697, 33779, 33801, 33802, 1),
(45, 1433313932, 1433316697, 1157, 1159, 1159, 1),
(46, 1433313932, 1433316697, 1233, 1233, 1235, 1),
(47, 1433313932, 1433316697, 110, 111, 111, 1),
(48, 1433313932, 1433316697, 1168, 1168, 1170, 1),
(49, 1433313932, 1433316697, 1636, 1638, 1638, 1),
(50, 1433313932, 1433316697, 95, 96, 96, 1),
(51, 1433313932, 1433316697, 959, 959, 961, 1),
(52, 1433313932, 1433316697, 10637, 10637, 10645, 1),
(53, 1433313932, 1433316697, 2370, 2370, 2372, 1),
(54, 1433313932, 1433316697, 96, 97, 97, 1),
(55, 1433313932, 1433316697, 561, 562, 562, 1),
(56, 1433313932, 1433316697, 1186, 1188, 1188, 1),
(57, 1433313932, 1433316697, 40, 41, 41, 1),
(58, 1433313932, 1433316697, 9682, 9689, 9689, 1),
(59, 1433313932, 1433316697, 1340, 1342, 1342, 1),
(60, 1433313932, 1433316697, 201, 202, 202, 1),
(61, 1433313932, 1433316697, 78, 79, 79, 1),
(62, 1433313932, 1433316697, 200, 201, 201, 1),
(63, 1433313932, 1433316697, 431, 431, 432, 1),
(64, 1433313932, 1433316697, 93, 94, 94, 1),
(65, 1433313932, 1433316697, 2945, 2945, 2948, 1),
(66, 1433313932, 1433316697, 101, 102, 102, 1),
(67, 1433313932, 1433316697, 78, 78, 79, 1),
(68, 1433313932, 1433316697, 55, 56, 56, 1),
(70, 1433313932, 1433316697, 9, 10, 10, 1),
(71, 1433313932, 1433316697, 2, 3, 3, 1),
(72, 1433313932, 1433316697, 0, 0, 0, 1),
(73, 1433313932, 1433316697, 20, 21, 21, 1),
(74, 1433313932, 1433316697, 5, 6, 6, 1),
(75, 1433313932, 1433316697, 2, 3, 3, 1),
(76, 1433313932, 1433316697, 10, 11, 11, 1),
(77, 1433313932, 1433316697, 3, 4, 4, 1),
(78, 1433313932, 1433316697, 10, 11, 11, 1),
(79, 1433313932, 1433316697, 3, 4, 4, 1),
(80, 1433313932, 1433316697, 26, 27, 27, 1),
(81, 1433313932, 1433316697, 39, 40, 40, 1),
(82, 1433313932, 1433316697, 4, 5, 5, 1),
(83, 1433313932, 1433316697, 7, 8, 8, 1),
(84, 1433313932, 1433316697, 0, 1, 1, 1),
(85, 1433313932, 1433316697, 39, 40, 40, 1),
(86, 1433313932, 1433316697, 26, 27, 27, 1),
(87, 1433313932, 1433316697, 9, 10, 10, 1),
(88, 1433313932, 1433316697, 11, 11, 12, 1),
(89, 1433313932, 1433316697, 24, 25, 25, 1),
(90, 1433313932, 1433316697, 8, 9, 9, 1),
(91, 1433313932, 1433316697, 6, 7, 7, 1),
(92, 1433313932, 1433316697, 0, 1, 1, 1),
(93, 1433313932, 1433316697, 0, 0, 0, 1),
(94, 1433313932, 1433316697, 0, 0, 0, 1),
(95, 1433313932, 1433316697, 1, 2, 2, 1),
(96, 1433313932, 1433316697, 10, 11, 11, 1),
(97, 1433313932, 1433316697, 12, 13, 13, 1),
(98, 1433313932, 1433316697, 7, 8, 8, 1),
(99, 1433313932, 1433316697, 0, 1, 1, 1),
(100, 1433313932, 1433316697, 363, 363, 364, 1),
(101, 1433313932, 1433316697, 193, 194, 194, 1),
(102, 1433313932, 1433316697, 211, 211, 212, 1),
(103, 1433313932, 1433316697, 132, 133, 133, 1),
(104, 1433313932, 1433316697, 602, 602, 603, 1),
(105, 1433313932, 1433316697, 333, 333, 334, 1),
(106, 1433313932, 1433316697, 170, 171, 171, 1),
(107, 1433313932, 1433316697, 309, 310, 310, 1),
(108, 1433313932, 1433316697, 1399, 1400, 1401, 1),
(109, 1433313932, 1433316697, 826, 826, 828, 1),
(110, 1433313932, 1433316697, 653, 654, 654, 1),
(111, 1433313932, 1433316697, 864, 866, 866, 1),
(112, 1433313932, 1433316697, 262, 263, 263, 1),
(113, 1433313932, 1433316697, 2723, 2725, 2726, 1),
(114, 1433313932, 1433316697, 1728, 1730, 1730, 1),
(115, 1433313932, 1433316697, 508, 509, 509, 1),
(116, 1433313932, 1433316697, 233, 234, 234, 1),
(117, 1433313932, 1433316697, 187, 188, 188, 1),
(118, 1433313932, 1433316697, 554, 555, 555, 1),
(119, 1433313932, 1433316697, 5641, 5646, 5646, 1),
(120, 1433313932, 1433316697, 368, 369, 369, 1),
(121, 1433313932, 1433316697, 949, 951, 951, 1),
(122, 1433313932, 1433316697, 3709, 3712, 3712, 1),
(123, 1433313932, 1433316697, 364, 365, 365, 1),
(124, 1433313932, 1433316697, 3552, 3555, 3555, 1);

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

--
-- Dumping data for table `news_social_score_feed_statistics`
--

INSERT INTO `news_social_score_feed_statistics` (`feed_id`, `average_peak_score`, `std_deviation`, `feed_n`) VALUES
(1, 2748.04, 6401.04, 78),
(2, 10.6333, 10.8949, 30),
(3, 1047.12, 1342.86, 26);

-- --------------------------------------------------------

--
-- Table structure for table `news_social_score_opengraph_shares`
--

CREATE TABLE IF NOT EXISTS `news_social_score_opengraph_shares` (
  `story_id` int(10) unsigned NOT NULL,
  `shares` int(10) unsigned DEFAULT NULL,
  PRIMARY KEY (`story_id`)
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

--
-- Dumping data for table `news_social_score_update`
--

INSERT INTO `news_social_score_update` (`story_id`, `last_update`, `old_raw_score`, `total_shares`, `new_raw_score`, `new_normalized_score`, `created`, `state`) VALUES
(1, 1433316697, 6427, 6439, 6434, 0.646004, 1433313932, 'UPDATED_STORIES'),
(2, 1433316697, 2241, 2245, 2243, -0.0241426, 1433313932, 'UPDATED_STORIES'),
(3, 1433316697, 2170, 2172, 2170, -0.0358072, 1433313932, 'UPDATED_STORIES'),
(4, 1433316697, 83, 83, 82, -0.369602, 1433313932, 'UPDATED_STORIES'),
(5, 1433316697, 43, 43, 42, -0.375993, 1433313932, 'UPDATED_STORIES'),
(6, 1433316697, 108, 108, 107, -0.365607, 1433313932, 'UPDATED_STORIES'),
(7, 1433316697, 56, 56, 55, -0.373916, 1433313932, 'UPDATED_STORIES'),
(8, 1433316697, 1910, 1916, 1914, -0.0767122, 1433313932, 'UPDATED_STORIES'),
(9, 1433316697, 299, 299, 298, -0.335088, 1433313932, 'UPDATED_STORIES'),
(10, 1433316697, 170, 170, 169, -0.3557, 1433313932, 'UPDATED_STORIES'),
(11, 1433316697, 526, 526, 525, -0.298816, 1433313932, 'UPDATED_STORIES'),
(12, 1433316697, 343, 344, 343, -0.327897, 1433313932, 'UPDATED_STORIES'),
(13, 1433316697, 2096, 2096, 2094, -0.0479512, 1433313932, 'UPDATED_STORIES'),
(14, 1433316697, 10, 10, 9, -0.381266, 1433313932, 'UPDATED_STORIES'),
(15, 1433316697, 71, 71, 70, -0.371519, 1433313932, 'UPDATED_STORIES'),
(16, 1433316697, 22, 22, 21, -0.379349, 1433313932, 'UPDATED_STORIES'),
(17, 1433316697, 223, 224, 223, -0.347072, 1433313932, 'UPDATED_STORIES'),
(18, 1433316697, 82, 82, 81, -0.369762, 1433313932, 'UPDATED_STORIES'),
(19, 1433316697, 91, 91, 90, -0.368324, 1433313932, 'UPDATED_STORIES'),
(20, 1433316697, 17, 17, 16, -0.380148, 1433313932, 'UPDATED_STORIES'),
(21, 1433316697, 17, 17, 16, -0.380148, 1433313932, 'UPDATED_STORIES'),
(22, 1433316697, 46, 46, 45, -0.375514, 1433313932, 'UPDATED_STORIES'),
(23, 1433316697, 47, 47, 46, -0.375354, 1433313932, 'UPDATED_STORIES'),
(24, 1433316697, 31, 31, 30, -0.377911, 1433313932, 'UPDATED_STORIES'),
(25, 1433316697, 47, 47, 46, -0.375354, 1433313932, 'UPDATED_STORIES'),
(26, 1433316697, 56, 57, 56, -0.373756, 1433313932, 'UPDATED_STORIES'),
(27, 1433316697, 139, 139, 138, -0.360654, 1433313932, 'UPDATED_STORIES'),
(28, 1433316697, 30910, 30919, 30898, 4.55758, 1433313932, 'UPDATED_STORIES'),
(29, 1433316697, 363, 363, 362, -0.324862, 1433313932, 'UPDATED_STORIES'),
(30, 1433316697, 764, 764, 763, -0.260787, 1433313932, 'UPDATED_STORIES'),
(31, 1433316697, 131, 132, 131, -0.361772, 1433313932, 'UPDATED_STORIES'),
(32, 1433316697, 578, 579, 578, -0.290348, 1433313932, 'UPDATED_STORIES'),
(33, 1433316697, 1575, 1575, 1573, -0.1312, 1433313932, 'UPDATED_STORIES'),
(34, 1433316697, 182, 182, 181, -0.353783, 1433313932, 'UPDATED_STORIES'),
(35, 1433316697, 5685, 5687, 5682, 0.525843, 1433313932, 'UPDATED_STORIES'),
(36, 1433316697, 1418, 1419, 1417, -0.156127, 1433313932, 'UPDATED_STORIES'),
(37, 1433316697, 8010, 8010, 8004, 0.897027, 1433313932, 'UPDATED_STORIES'),
(38, 1433316697, 731, 731, 730, -0.26606, 1433313932, 'UPDATED_STORIES'),
(39, 1433316697, 23585, 23612, 23596, 3.39002, 1433313932, 'UPDATED_STORIES'),
(40, 1433316697, 54, 56, 55, -0.373916, 1433313932, 'UPDATED_STORIES'),
(41, 1433316697, 351, 351, 350, -0.326779, 1433313932, 'UPDATED_STORIES'),
(42, 1433316697, 617, 617, 616, -0.284276, 1433313932, 'UPDATED_STORIES'),
(43, 1433316697, 211, 211, 210, -0.349149, 1433313932, 'UPDATED_STORIES'),
(44, 1433316697, 33801, 33802, 33779, 5.01825, 1433313932, 'UPDATED_STORIES'),
(45, 1433316697, 1159, 1159, 1157, -0.197671, 1433313932, 'UPDATED_STORIES'),
(46, 1433316697, 1233, 1235, 1233, -0.185527, 1433313932, 'UPDATED_STORIES'),
(47, 1433316697, 111, 111, 110, -0.365128, 1433313932, 'UPDATED_STORIES'),
(48, 1433316697, 1168, 1170, 1168, -0.195913, 1433313932, 'UPDATED_STORIES'),
(49, 1433316697, 1638, 1638, 1636, -0.121134, 1433313932, 'UPDATED_STORIES'),
(50, 1433316697, 96, 96, 95, -0.367525, 1433313932, 'UPDATED_STORIES'),
(51, 1433316697, 956, 961, 959, -0.229309, 1433313932, 'UPDATED_STORIES'),
(52, 1433316697, 10620, 10645, 10637, 1.31807, 1433313932, 'UPDATED_STORIES'),
(53, 1433316697, 2348, 2372, 2370, -0.00384766, 1433313932, 'UPDATED_STORIES'),
(54, 1433316697, 97, 97, 96, -0.367365, 1433313932, 'UPDATED_STORIES'),
(55, 1433316697, 562, 562, 561, -0.293064, 1433313932, 'UPDATED_STORIES'),
(56, 1433316697, 1188, 1188, 1186, -0.193038, 1433313932, 'UPDATED_STORIES'),
(57, 1433316697, 41, 41, 40, -0.376313, 1433313932, 'UPDATED_STORIES'),
(58, 1433316697, 9689, 9689, 9682, 1.16531, 1433313932, 'UPDATED_STORIES'),
(59, 1433316697, 1342, 1342, 1340, -0.16843, 1433313932, 'UPDATED_STORIES'),
(60, 1433316697, 202, 202, 201, -0.350587, 1433313932, 'UPDATED_STORIES'),
(61, 1433316697, 79, 79, 78, -0.370241, 1433313932, 'UPDATED_STORIES'),
(62, 1433316697, 201, 201, 200, -0.350747, 1433313932, 'UPDATED_STORIES'),
(63, 1433316697, 430, 432, 431, -0.313836, 1433313932, 'UPDATED_STORIES'),
(64, 1433316697, 94, 94, 93, -0.367844, 1433313932, 'UPDATED_STORIES'),
(65, 1433316697, 2936, 2948, 2945, 0.0881882, 1433313932, 'UPDATED_STORIES'),
(66, 1433316697, 102, 102, 101, -0.366566, 1433313932, 'UPDATED_STORIES'),
(67, 1433316697, 78, 79, 78, -0.370241, 1433313932, 'UPDATED_STORIES'),
(68, 1433316697, 56, 56, 55, -0.373916, 1433313932, 'UPDATED_STORIES'),
(70, 1433316697, 10, 10, 9, -0.150498, 1433313932, 'UPDATED_STORIES'),
(71, 1433316697, 3, 3, 2, -0.792592, 1433313932, 'UPDATED_STORIES'),
(72, 1433316697, 0, 0, 0, -0.975989, 1433313932, 'UPDATED_STORIES'),
(73, 1433316697, 21, 21, 20, 0.858506, 1433313932, 'UPDATED_STORIES'),
(74, 1433316697, 6, 6, 5, -0.517409, 1433313932, 'UPDATED_STORIES'),
(75, 1433316697, 3, 3, 2, -0.792592, 1433313932, 'UPDATED_STORIES'),
(76, 1433316697, 11, 11, 10, -0.0587708, 1433313932, 'UPDATED_STORIES'),
(77, 1433316697, 4, 4, 3, -0.700864, 1433313932, 'UPDATED_STORIES'),
(78, 1433316697, 11, 11, 10, -0.0587708, 1433313932, 'UPDATED_STORIES'),
(79, 1433316697, 4, 4, 3, -0.700864, 1433313932, 'UPDATED_STORIES'),
(80, 1433316697, 27, 27, 26, 1.40887, 1433313932, 'UPDATED_STORIES'),
(81, 1433316697, 40, 40, 39, 2.60133, 1433313932, 'UPDATED_STORIES'),
(82, 1433316697, 5, 5, 4, -0.609137, 1433313932, 'UPDATED_STORIES'),
(83, 1433316697, 8, 8, 7, -0.333954, 1433313932, 'UPDATED_STORIES'),
(84, 1433316697, 1, 1, 0, -0.975989, 1433313932, 'UPDATED_STORIES'),
(85, 1433316697, 40, 40, 39, 2.60133, 1433313932, 'UPDATED_STORIES'),
(86, 1433316697, 27, 27, 26, 1.40887, 1433313932, 'UPDATED_STORIES'),
(87, 1433316697, 10, 10, 9, -0.150498, 1433313932, 'UPDATED_STORIES'),
(88, 1433316697, 11, 12, 11, 0.0330152, 1433313932, 'UPDATED_STORIES'),
(89, 1433316697, 25, 25, 24, 1.22542, 1433313932, 'UPDATED_STORIES'),
(90, 1433316697, 9, 9, 8, -0.242226, 1433313932, 'UPDATED_STORIES'),
(91, 1433316697, 7, 7, 6, -0.425681, 1433313932, 'UPDATED_STORIES'),
(92, 1433316697, 1, 1, 0, -0.975989, 1433313932, 'UPDATED_STORIES'),
(93, 1433316697, 0, 0, 0, -0.975989, 1433313932, 'UPDATED_STORIES'),
(94, 1433316697, 0, 0, 0, -0.975989, 1433313932, 'UPDATED_STORIES'),
(95, 1433316697, 2, 2, 1, -0.88432, 1433313932, 'UPDATED_STORIES'),
(96, 1433316697, 11, 11, 10, -0.0587708, 1433313932, 'UPDATED_STORIES'),
(97, 1433316697, 13, 13, 12, 0.124684, 1433313932, 'UPDATED_STORIES'),
(98, 1433316697, 8, 8, 7, -0.333954, 1433313932, 'UPDATED_STORIES'),
(99, 1433316697, 1, 1, 0, -0.975989, 1433313932, 'UPDATED_STORIES'),
(100, 1433316697, 360, 364, 363, -0.522421, 1433313932, 'UPDATED_STORIES'),
(101, 1433316697, 194, 194, 193, -0.647129, 1433313932, 'UPDATED_STORIES'),
(102, 1433316697, 211, 212, 211, -0.633924, 1433313932, 'UPDATED_STORIES'),
(103, 1433316697, 133, 133, 132, -0.691877, 1433313932, 'UPDATED_STORIES'),
(104, 1433316697, 602, 603, 602, -0.347099, 1433313932, 'UPDATED_STORIES'),
(105, 1433316697, 333, 334, 333, -0.544429, 1433313932, 'UPDATED_STORIES'),
(106, 1433316697, 171, 171, 170, -0.664001, 1433313932, 'UPDATED_STORIES'),
(107, 1433316697, 310, 310, 309, -0.562035, 1433313932, 'UPDATED_STORIES'),
(108, 1433316697, 1400, 1401, 1399, 0.238289, 1433313932, 'UPDATED_STORIES'),
(109, 1433316697, 826, 828, 826, -0.182045, 1433313932, 'UPDATED_STORIES'),
(110, 1433316697, 654, 654, 653, -0.309687, 1433313932, 'UPDATED_STORIES'),
(111, 1433316697, 866, 866, 864, -0.154171, 1433313932, 'UPDATED_STORIES'),
(112, 1433316697, 263, 263, 262, -0.596513, 1433313932, 'UPDATED_STORIES'),
(113, 1433316697, 2725, 2726, 2723, 1.21027, 1433313932, 'UPDATED_STORIES'),
(114, 1433316697, 1730, 1730, 1728, 0.479633, 1433313932, 'UPDATED_STORIES'),
(115, 1433316697, 509, 509, 508, -0.416055, 1433313932, 'UPDATED_STORIES'),
(116, 1433316697, 234, 234, 233, -0.617786, 1433313932, 'UPDATED_STORIES'),
(117, 1433316697, 188, 188, 187, -0.651531, 1433313932, 'UPDATED_STORIES'),
(118, 1433316697, 555, 555, 554, -0.382311, 1433313932, 'UPDATED_STORIES'),
(119, 1433316697, 5646, 5646, 5641, 3.35229, 1433313932, 'UPDATED_STORIES'),
(120, 1433316697, 369, 369, 368, -0.518755, 1433313932, 'UPDATED_STORIES'),
(121, 1433316697, 951, 951, 949, -0.0918172, 1433313932, 'UPDATED_STORIES'),
(122, 1433316697, 3712, 3712, 3709, 1.93357, 1433313932, 'UPDATED_STORIES'),
(123, 1433316697, 365, 365, 364, -0.521689, 1433313932, 'UPDATED_STORIES'),
(124, 1433316697, 3555, 3555, 3552, 1.8184, 1433313932, 'UPDATED_STORIES');

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
  `url` varchar(1000) DEFAULT NULL,
  `title` varchar(200) DEFAULT NULL,
  `subtitle` varchar(500) DEFAULT NULL,
  `feed_id` int(10) unsigned NOT NULL,
  `created` int(10) unsigned DEFAULT NULL,
  `image` varchar(1000) DEFAULT NULL,
  PRIMARY KEY (`story_id`),
  KEY `feed_id` (`feed_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=128 ;

--
-- Dumping data for table `news_stories`
--

INSERT INTO `news_stories` (`story_id`, `url`, `title`, `subtitle`, `feed_id`, `created`, `image`) VALUES
(1, 'http://www.bbc.co.uk/news/world-us-canada-32986950', 'http://www.bbc.co.uk/news/world-us-canada-32986950', 'http://www.bbc.co.uk/news/world-us-canada-32986950', 1, 1433313932, 'http://www.bbc.co.uk/news/world-us-canada-32986950'),
(2, 'http://www.bbc.co.uk/news/world-asia-china-32987573', 'http://www.bbc.co.uk/news/world-asia-china-32987573', 'http://www.bbc.co.uk/news/world-asia-china-32987573', 1, 1433313932, 'http://www.bbc.co.uk/news/world-asia-china-32987573'),
(3, 'http://www.bbc.co.uk/news/world-us-canada-32982140', 'http://www.bbc.co.uk/news/world-us-canada-32982140', 'http://www.bbc.co.uk/news/world-us-canada-32982140', 1, 1433313932, 'http://www.bbc.co.uk/news/world-us-canada-32982140'),
(4, 'http://www.bbc.co.uk/news/world-europe-32987562', 'http://www.bbc.co.uk/news/world-europe-32987562', 'http://www.bbc.co.uk/news/world-europe-32987562', 1, 1433313932, 'http://www.bbc.co.uk/news/world-europe-32987562'),
(5, 'http://www.bbc.co.uk/news/world-europe-32985554', 'http://www.bbc.co.uk/news/world-europe-32985554', 'http://www.bbc.co.uk/news/world-europe-32985554', 1, 1433313932, 'http://www.bbc.co.uk/news/world-europe-32985554'),
(6, 'http://www.bbc.co.uk/news/business-32970412', 'http://www.bbc.co.uk/news/business-32970412', 'http://www.bbc.co.uk/news/business-32970412', 1, 1433313932, 'http://www.bbc.co.uk/news/business-32970412'),
(7, 'http://www.bbc.co.uk/news/world-us-canada-32984591', 'http://www.bbc.co.uk/news/world-us-canada-32984591', 'http://www.bbc.co.uk/news/world-us-canada-32984591', 1, 1433313932, 'http://www.bbc.co.uk/news/world-us-canada-32984591'),
(8, 'http://www.bbc.co.uk/news/world-us-canada-32982217', 'http://www.bbc.co.uk/news/world-us-canada-32982217', 'http://www.bbc.co.uk/news/world-us-canada-32982217', 1, 1433313932, 'http://www.bbc.co.uk/news/world-us-canada-32982217'),
(9, 'http://www.bbc.co.uk/news/world-us-canada-32980208', 'http://www.bbc.co.uk/news/world-us-canada-32980208', 'http://www.bbc.co.uk/news/world-us-canada-32980208', 1, 1433313932, 'http://www.bbc.co.uk/news/world-us-canada-32980208'),
(10, 'http://www.bbc.co.uk/news/world-europe-32974603', 'http://www.bbc.co.uk/news/world-europe-32974603', 'http://www.bbc.co.uk/news/world-europe-32974603', 1, 1433313932, 'http://www.bbc.co.uk/news/world-europe-32974603'),
(11, 'http://www.bbc.co.uk/news/science-environment-32976838', 'http://www.bbc.co.uk/news/science-environment-32976838', 'http://www.bbc.co.uk/news/science-environment-32976838', 1, 1433313932, 'http://www.bbc.co.uk/news/science-environment-32976838'),
(12, 'http://www.bbc.co.uk/news/science-environment-32976352', 'http://www.bbc.co.uk/news/science-environment-32976352', 'http://www.bbc.co.uk/news/science-environment-32976352', 1, 1433313932, 'http://www.bbc.co.uk/news/science-environment-32976352'),
(13, 'http://www.bbc.co.uk/sport/0/football/32975524', 'http://www.bbc.co.uk/sport/0/football/32975524', 'http://www.bbc.co.uk/sport/0/football/32975524', 1, 1433313932, 'http://www.bbc.co.uk/sport/0/football/32975524'),
(14, 'http://www.bbc.co.uk/news/world-asia-32987675', 'http://www.bbc.co.uk/news/world-asia-32987675', 'http://www.bbc.co.uk/news/world-asia-32987675', 1, 1433313932, 'http://www.bbc.co.uk/news/world-asia-32987675'),
(15, 'http://www.bbc.co.uk/news/world-africa-32987472', 'http://www.bbc.co.uk/news/world-africa-32987472', 'http://www.bbc.co.uk/news/world-africa-32987472', 1, 1433313932, 'http://www.bbc.co.uk/news/world-africa-32987472'),
(16, 'http://www.bbc.co.uk/news/world-asia-32987198', 'http://www.bbc.co.uk/news/world-asia-32987198', 'http://www.bbc.co.uk/news/world-asia-32987198', 1, 1433313932, 'http://www.bbc.co.uk/news/world-asia-32987198'),
(17, 'http://www.bbc.co.uk/news/world-latin-america-32982248', 'http://www.bbc.co.uk/news/world-latin-america-32982248', 'http://www.bbc.co.uk/news/world-latin-america-32982248', 1, 1433313932, 'http://www.bbc.co.uk/news/world-latin-america-32982248'),
(18, 'http://www.bbc.co.uk/news/world-us-canada-32985385', 'http://www.bbc.co.uk/news/world-us-canada-32985385', 'http://www.bbc.co.uk/news/world-us-canada-32985385', 1, 1433313932, 'http://www.bbc.co.uk/news/world-us-canada-32985385'),
(19, 'http://www.bbc.co.uk/news/uk-32985384', 'http://www.bbc.co.uk/news/uk-32985384', 'http://www.bbc.co.uk/news/uk-32985384', 1, 1433313932, 'http://www.bbc.co.uk/news/uk-32985384'),
(20, 'http://www.bbc.co.uk/news/world-32985895', 'http://www.bbc.co.uk/news/world-32985895', 'http://www.bbc.co.uk/news/world-32985895', 1, 1433313932, 'http://www.bbc.co.uk/news/world-32985895'),
(21, 'http://www.bbc.co.uk/news/world-middle-east-32973202', 'http://www.bbc.co.uk/news/world-middle-east-32973202', 'http://www.bbc.co.uk/news/world-middle-east-32973202', 1, 1433313932, 'http://www.bbc.co.uk/news/world-middle-east-32973202'),
(22, 'http://www.bbc.co.uk/news/uk-politics-32972880', 'http://www.bbc.co.uk/news/uk-politics-32972880', 'http://www.bbc.co.uk/news/uk-politics-32972880', 1, 1433313932, 'http://www.bbc.co.uk/news/uk-politics-32972880'),
(23, 'http://www.bbc.co.uk/news/world-europe-32975794', 'http://www.bbc.co.uk/news/world-europe-32975794', 'http://www.bbc.co.uk/news/world-europe-32975794', 1, 1433313932, 'http://www.bbc.co.uk/news/world-europe-32975794'),
(24, 'http://www.bbc.co.uk/news/world-32973203', 'http://www.bbc.co.uk/news/world-32973203', 'http://www.bbc.co.uk/news/world-32973203', 1, 1433313932, 'http://www.bbc.co.uk/news/world-32973203'),
(25, 'http://www.bbc.co.uk/news/science-environment-32901834', 'http://www.bbc.co.uk/news/science-environment-32901834', 'http://www.bbc.co.uk/news/science-environment-32901834', 1, 1433313932, 'http://www.bbc.co.uk/news/science-environment-32901834'),
(26, 'http://www.bbc.co.uk/news/business-32852468', 'http://www.bbc.co.uk/news/business-32852468', 'http://www.bbc.co.uk/news/business-32852468', 1, 1433313932, 'http://www.bbc.co.uk/news/business-32852468'),
(27, 'http://www.bbc.co.uk/sport/0/cricket/32986595', 'http://www.bbc.co.uk/sport/0/cricket/32986595', 'http://www.bbc.co.uk/sport/0/cricket/32986595', 1, 1433313932, 'http://www.bbc.co.uk/sport/0/cricket/32986595'),
(28, 'http://www.bbc.co.uk/newsbeat/32973341', 'http://www.bbc.co.uk/newsbeat/32973341', 'http://www.bbc.co.uk/newsbeat/32973341', 1, 1433313932, 'http://www.bbc.co.uk/newsbeat/32973341'),
(29, 'http://www.bbc.co.uk/news/business-32969992', 'http://www.bbc.co.uk/news/business-32969992', 'http://www.bbc.co.uk/news/business-32969992', 1, 1433313932, 'http://www.bbc.co.uk/news/business-32969992'),
(30, 'http://www.bbc.co.uk/news/business-11876811', 'http://www.bbc.co.uk/news/business-11876811', 'http://www.bbc.co.uk/news/business-11876811', 1, 1433313932, 'http://www.bbc.co.uk/news/business-11876811'),
(31, 'http://www.bbc.co.uk/news/technology-32982609', 'http://www.bbc.co.uk/news/technology-32982609', 'http://www.bbc.co.uk/news/technology-32982609', 1, 1433313932, 'http://www.bbc.co.uk/news/technology-32982609'),
(32, 'http://www.bbc.co.uk/news/technology-32973815', 'http://www.bbc.co.uk/news/technology-32973815', 'http://www.bbc.co.uk/news/technology-32973815', 1, 1433313932, 'http://www.bbc.co.uk/news/technology-32973815'),
(33, 'http://www.bbc.co.uk/news/entertainment-arts-32973176', 'http://www.bbc.co.uk/news/entertainment-arts-32973176', 'http://www.bbc.co.uk/news/entertainment-arts-32973176', 1, 1433313932, 'http://www.bbc.co.uk/news/entertainment-arts-32973176'),
(34, 'http://www.bbc.co.uk/news/entertainment-arts-32971919', 'http://www.bbc.co.uk/news/entertainment-arts-32971919', 'http://www.bbc.co.uk/news/entertainment-arts-32971919', 1, 1433313932, 'http://www.bbc.co.uk/news/entertainment-arts-32971919'),
(35, 'http://www.bbc.co.uk/news/science-environment-32958033', 'http://www.bbc.co.uk/news/science-environment-32958033', 'http://www.bbc.co.uk/news/science-environment-32958033', 1, 1433313932, 'http://www.bbc.co.uk/news/science-environment-32958033'),
(36, 'http://www.bbc.co.uk/news/science-environment-32967386', 'http://www.bbc.co.uk/news/science-environment-32967386', 'http://www.bbc.co.uk/news/science-environment-32967386', 1, 1433313932, 'http://www.bbc.co.uk/news/science-environment-32967386'),
(37, 'http://www.bbc.co.uk/news/world-asia-32969054', 'http://www.bbc.co.uk/news/world-asia-32969054', 'http://www.bbc.co.uk/news/world-asia-32969054', 1, 1433313932, 'http://www.bbc.co.uk/news/world-asia-32969054'),
(38, 'http://www.bbc.co.uk/news/world-us-canada-32969338', 'http://www.bbc.co.uk/news/world-us-canada-32969338', 'http://www.bbc.co.uk/news/world-us-canada-32969338', 1, 1433313932, 'http://www.bbc.co.uk/news/world-us-canada-32969338'),
(39, 'http://www.bbc.co.uk/sport/0/football/32982449', 'http://www.bbc.co.uk/sport/0/football/32982449', 'http://www.bbc.co.uk/sport/0/football/32982449', 1, 1433313932, 'http://www.bbc.co.uk/sport/0/football/32982449'),
(40, 'http://www.bbc.co.uk/sport/0/cricket/32984979', 'http://www.bbc.co.uk/sport/0/cricket/32984979', 'http://www.bbc.co.uk/sport/0/cricket/32984979', 1, 1433313932, 'http://www.bbc.co.uk/sport/0/cricket/32984979'),
(41, 'http://www.bbc.co.uk/news/magazine-32960509', 'http://www.bbc.co.uk/news/magazine-32960509', 'http://www.bbc.co.uk/news/magazine-32960509', 1, 1433313932, 'http://www.bbc.co.uk/news/magazine-32960509'),
(42, 'http://www.bbc.co.uk/news/magazine-32966907', 'http://www.bbc.co.uk/news/magazine-32966907', 'http://www.bbc.co.uk/news/magazine-32966907', 1, 1433313932, 'http://www.bbc.co.uk/news/magazine-32966907'),
(43, 'http://www.bbc.co.uk/news/world-asia-32971952', 'http://www.bbc.co.uk/news/world-asia-32971952', 'http://www.bbc.co.uk/news/world-asia-32971952', 1, 1433313932, 'http://www.bbc.co.uk/news/world-asia-32971952'),
(44, 'http://www.bbc.co.uk/news/world-europe-32960470', 'http://www.bbc.co.uk/news/world-europe-32960470', 'http://www.bbc.co.uk/news/world-europe-32960470', 1, 1433313932, 'http://www.bbc.co.uk/news/world-europe-32960470'),
(45, 'http://www.bbc.co.uk/news/world-africa-32978735', 'http://www.bbc.co.uk/news/world-africa-32978735', 'http://www.bbc.co.uk/news/world-africa-32978735', 1, 1433313932, 'http://www.bbc.co.uk/news/world-africa-32978735'),
(46, 'http://www.bbc.co.uk/news/entertainment-arts-32975956', 'http://www.bbc.co.uk/news/entertainment-arts-32975956', 'http://www.bbc.co.uk/news/entertainment-arts-32975956', 1, 1433313932, 'http://www.bbc.co.uk/news/entertainment-arts-32975956'),
(47, 'http://www.bbc.co.uk/news/world-europe-32972406', 'http://www.bbc.co.uk/news/world-europe-32972406', 'http://www.bbc.co.uk/news/world-europe-32972406', 1, 1433313932, 'http://www.bbc.co.uk/news/world-europe-32972406'),
(48, 'http://www.bbc.co.uk/news/world-latin-america-32973483', 'http://www.bbc.co.uk/news/world-latin-america-32973483', 'http://www.bbc.co.uk/news/world-latin-america-32973483', 1, 1433313932, 'http://www.bbc.co.uk/news/world-latin-america-32973483'),
(49, 'http://www.bbc.co.uk/news/world-middle-east-32962870', 'http://www.bbc.co.uk/news/world-middle-east-32962870', 'http://www.bbc.co.uk/news/world-middle-east-32962870', 1, 1433313932, 'http://www.bbc.co.uk/news/world-middle-east-32962870'),
(50, 'http://www.bbc.co.uk/news/world-us-canada-32979612', 'http://www.bbc.co.uk/news/world-us-canada-32979612', 'http://www.bbc.co.uk/news/world-us-canada-32979612', 1, 1433313932, 'http://www.bbc.co.uk/news/world-us-canada-32979612'),
(51, 'http://www.bbc.co.uk/news/education-32978355', 'http://www.bbc.co.uk/news/education-32978355', 'http://www.bbc.co.uk/news/education-32978355', 1, 1433313932, 'http://www.bbc.co.uk/news/education-32978355'),
(52, 'http://www.bbc.co.uk/news/uk-england-nottinghamshire-32986664', 'http://www.bbc.co.uk/news/uk-england-nottinghamshire-32986664', 'http://www.bbc.co.uk/news/uk-england-nottinghamshire-32986664', 1, 1433313932, 'http://www.bbc.co.uk/news/uk-england-nottinghamshire-32986664'),
(53, 'http://www.bbc.co.uk/news/uk-england-stoke-staffordshire-32987550', 'http://www.bbc.co.uk/news/uk-england-stoke-staffordshire-32987550', 'http://www.bbc.co.uk/news/uk-england-stoke-staffordshire-32987550', 1, 1433313932, 'http://www.bbc.co.uk/news/uk-england-stoke-staffordshire-32987550'),
(54, 'http://www.bbc.co.uk/news/uk-politics-32985571', 'http://www.bbc.co.uk/news/uk-politics-32985571', 'http://www.bbc.co.uk/news/uk-politics-32985571', 1, 1433313932, 'http://www.bbc.co.uk/news/uk-politics-32985571'),
(55, 'http://www.bbc.co.uk/news/world-africa-32448072', 'http://www.bbc.co.uk/news/world-africa-32448072', 'http://www.bbc.co.uk/news/world-africa-32448072', 1, 1433313932, 'http://www.bbc.co.uk/news/world-africa-32448072'),
(56, 'http://www.bbc.co.uk/news/in-pictures-32960657', 'http://www.bbc.co.uk/news/in-pictures-32960657', 'http://www.bbc.co.uk/news/in-pictures-32960657', 1, 1433313932, 'http://www.bbc.co.uk/news/in-pictures-32960657'),
(57, 'http://www.bbc.co.uk/news/in-pictures-32960656', 'http://www.bbc.co.uk/news/in-pictures-32960656', 'http://www.bbc.co.uk/news/in-pictures-32960656', 1, 1433313932, 'http://www.bbc.co.uk/news/in-pictures-32960656'),
(58, 'http://www.bbc.co.uk/news/science-environment-32935898', 'http://www.bbc.co.uk/news/science-environment-32935898', 'http://www.bbc.co.uk/news/science-environment-32935898', 1, 1433313932, 'http://www.bbc.co.uk/news/science-environment-32935898'),
(59, 'http://www.bbc.co.uk/news/magazine-32888643', 'http://www.bbc.co.uk/news/magazine-32888643', 'http://www.bbc.co.uk/news/magazine-32888643', 1, 1433313932, 'http://www.bbc.co.uk/news/magazine-32888643'),
(60, 'http://www.bbc.co.uk/news/uk-scotland-south-scotland-32897366', 'http://www.bbc.co.uk/news/uk-scotland-south-scotland-32897366', 'http://www.bbc.co.uk/news/uk-scotland-south-scotland-32897366', 1, 1433313932, 'http://www.bbc.co.uk/news/uk-scotland-south-scotland-32897366'),
(61, 'http://www.bbc.co.uk/news/entertainment-arts-32851421', 'http://www.bbc.co.uk/news/entertainment-arts-32851421', 'http://www.bbc.co.uk/news/entertainment-arts-32851421', 1, 1433313932, 'http://www.bbc.co.uk/news/entertainment-arts-32851421'),
(62, 'http://www.bbc.co.uk/news/world-asia-india-32733902', 'http://www.bbc.co.uk/news/world-asia-india-32733902', 'http://www.bbc.co.uk/news/world-asia-india-32733902', 1, 1433313932, 'http://www.bbc.co.uk/news/world-asia-india-32733902'),
(63, 'http://www.bbc.co.uk/news/magazine-32839660', 'http://www.bbc.co.uk/news/magazine-32839660', 'http://www.bbc.co.uk/news/magazine-32839660', 1, 1433313932, 'http://www.bbc.co.uk/news/magazine-32839660'),
(64, 'http://www.bbc.co.uk/news/world-europe-32972893', 'http://www.bbc.co.uk/news/world-europe-32972893', 'http://www.bbc.co.uk/news/world-europe-32972893', 1, 1433313932, 'http://www.bbc.co.uk/news/world-europe-32972893'),
(65, 'http://www.bbc.co.uk/news/world-asia-32811867', 'http://www.bbc.co.uk/news/world-asia-32811867', 'http://www.bbc.co.uk/news/world-asia-32811867', 1, 1433313932, 'http://www.bbc.co.uk/news/world-asia-32811867'),
(66, 'http://www.bbc.co.uk/news/magazine-32976515', 'http://www.bbc.co.uk/news/magazine-32976515', 'http://www.bbc.co.uk/news/magazine-32976515', 1, 1433313932, 'http://www.bbc.co.uk/news/magazine-32976515'),
(67, 'http://www.bbc.co.uk/news/magazine-32965494', 'http://www.bbc.co.uk/news/magazine-32965494', 'http://www.bbc.co.uk/news/magazine-32965494', 1, 1433313932, 'http://www.bbc.co.uk/news/magazine-32965494'),
(68, 'http://www.bbc.co.uk/news/magazine-32965229', 'http://www.bbc.co.uk/news/magazine-32965229', 'http://www.bbc.co.uk/news/magazine-32965229', 1, 1433313932, 'http://www.bbc.co.uk/news/magazine-32965229'),
(70, 'http://9gag.com/gag/ae0vm7B', 'http://9gag.com/gag/ae0vm7B', 'http://9gag.com/gag/ae0vm7B', 2, 1433313932, 'http://9gag.com/gag/ae0vm7B'),
(71, 'http://9gag.com/gag/anKpB4o', 'http://9gag.com/gag/anKpB4o', 'http://9gag.com/gag/anKpB4o', 2, 1433313932, 'http://9gag.com/gag/anKpB4o'),
(72, 'http://9gag.com/gag/a2YBYoE', 'http://9gag.com/gag/a2YBYoE', 'http://9gag.com/gag/a2YBYoE', 2, 1433313932, 'http://9gag.com/gag/a2YBYoE'),
(73, 'http://9gag.com/gag/ae0vx5q', 'http://9gag.com/gag/ae0vx5q', 'http://9gag.com/gag/ae0vx5q', 2, 1433313932, 'http://9gag.com/gag/ae0vx5q'),
(74, 'http://9gag.com/gag/aKPrQb1', 'http://9gag.com/gag/aKPrQb1', 'http://9gag.com/gag/aKPrQb1', 2, 1433313932, 'http://9gag.com/gag/aKPrQb1'),
(75, 'http://9gag.com/gag/avg3d0O', 'http://9gag.com/gag/avg3d0O', 'http://9gag.com/gag/avg3d0O', 2, 1433313932, 'http://9gag.com/gag/avg3d0O'),
(76, 'http://9gag.com/gag/ay0OKqV', 'http://9gag.com/gag/ay0OKqV', 'http://9gag.com/gag/ay0OKqV', 2, 1433313932, 'http://9gag.com/gag/ay0OKqV'),
(77, 'http://9gag.com/gag/ay0g088', 'http://9gag.com/gag/ay0g088', 'http://9gag.com/gag/ay0g088', 2, 1433313932, 'http://9gag.com/gag/ay0g088'),
(78, 'http://9gag.com/gag/aWWwPK3', 'http://9gag.com/gag/aWWwPK3', 'http://9gag.com/gag/aWWwPK3', 2, 1433313932, 'http://9gag.com/gag/aWWwPK3'),
(79, 'http://9gag.com/gag/a7y4y7z', 'http://9gag.com/gag/a7y4y7z', 'http://9gag.com/gag/a7y4y7z', 2, 1433313932, 'http://9gag.com/gag/a7y4y7z'),
(80, 'http://9gag.com/gag/aKPr9V3', 'http://9gag.com/gag/aKPr9V3', 'http://9gag.com/gag/aKPr9V3', 2, 1433313932, 'http://9gag.com/gag/aKPr9V3'),
(81, 'http://9gag.com/gag/aB3q3YN', 'http://9gag.com/gag/aB3q3YN', 'http://9gag.com/gag/aB3q3YN', 2, 1433313932, 'http://9gag.com/gag/aB3q3YN'),
(82, 'http://9gag.com/gag/ao0bDvn', 'http://9gag.com/gag/ao0bDvn', 'http://9gag.com/gag/ao0bDvn', 2, 1433313932, 'http://9gag.com/gag/ao0bDvn'),
(83, 'http://9gag.com/gag/aE1LXQK', 'http://9gag.com/gag/aE1LXQK', 'http://9gag.com/gag/aE1LXQK', 2, 1433313932, 'http://9gag.com/gag/aE1LXQK'),
(84, 'http://9gag.com/gag/aWWwXzZ', 'http://9gag.com/gag/aWWwXzZ', 'http://9gag.com/gag/aWWwXzZ', 2, 1433313932, 'http://9gag.com/gag/aWWwXzZ'),
(85, 'http://9gag.com/gag/aE1rGde', 'http://9gag.com/gag/aE1rGde', 'http://9gag.com/gag/aE1rGde', 2, 1433313932, 'http://9gag.com/gag/aE1rGde'),
(86, 'http://9gag.com/gag/aKPrGgZ', 'http://9gag.com/gag/aKPrGgZ', 'http://9gag.com/gag/aKPrGgZ', 2, 1433313932, 'http://9gag.com/gag/aKPrGgZ'),
(87, 'http://9gag.com/gag/ap0y00M', 'http://9gag.com/gag/ap0y00M', 'http://9gag.com/gag/ap0y00M', 2, 1433313932, 'http://9gag.com/gag/ap0y00M'),
(88, 'http://9gag.com/gag/aGwWyV5', 'http://9gag.com/gag/aGwWyV5', 'http://9gag.com/gag/aGwWyV5', 2, 1433313932, 'http://9gag.com/gag/aGwWyV5'),
(89, 'http://9gag.com/gag/aMr3opM', 'http://9gag.com/gag/aMr3opM', 'http://9gag.com/gag/aMr3opM', 2, 1433313932, 'http://9gag.com/gag/aMr3opM'),
(90, 'http://9gag.com/gag/ae0o00O', 'http://9gag.com/gag/ae0o00O', 'http://9gag.com/gag/ae0o00O', 2, 1433313932, 'http://9gag.com/gag/ae0o00O'),
(91, 'http://9gag.com/gag/axZX7Kp', 'http://9gag.com/gag/axZX7Kp', 'http://9gag.com/gag/axZX7Kp', 2, 1433313932, 'http://9gag.com/gag/axZX7Kp'),
(92, 'http://9gag.com/gag/aB3q33Z', 'http://9gag.com/gag/aB3q33Z', 'http://9gag.com/gag/aB3q33Z', 2, 1433313932, 'http://9gag.com/gag/aB3q33Z'),
(93, 'http://9gag.com/gag/a4dDBYm', 'http://9gag.com/gag/a4dDBYm', 'http://9gag.com/gag/a4dDBYm', 2, 1433313932, 'http://9gag.com/gag/a4dDBYm'),
(94, 'http://9gag.com/gag/a1eG6yb', 'http://9gag.com/gag/a1eG6yb', 'http://9gag.com/gag/a1eG6yb', 2, 1433313932, 'http://9gag.com/gag/a1eG6yb'),
(95, 'http://9gag.com/gag/aRP5PrB', 'http://9gag.com/gag/aRP5PrB', 'http://9gag.com/gag/aRP5PrB', 2, 1433313932, 'http://9gag.com/gag/aRP5PrB'),
(96, 'http://9gag.com/gag/ay0OXyX', 'http://9gag.com/gag/ay0OXyX', 'http://9gag.com/gag/ay0OXyX', 2, 1433313932, 'http://9gag.com/gag/ay0OXyX'),
(97, 'http://9gag.com/gag/adYZYY9', 'http://9gag.com/gag/adYZYY9', 'http://9gag.com/gag/adYZYY9', 2, 1433313932, 'http://9gag.com/gag/adYZYY9'),
(98, 'http://9gag.com/gag/axZXArp', 'http://9gag.com/gag/axZXArp', 'http://9gag.com/gag/axZXArp', 2, 1433313932, 'http://9gag.com/gag/axZXArp'),
(99, 'http://9gag.com/gag/avg3jqO', 'http://9gag.com/gag/avg3jqO', 'http://9gag.com/gag/avg3jqO', 2, 1433313932, 'http://9gag.com/gag/avg3jqO'),
(100, 'http://www.engadget.com/2015/06/03/steam-will-refund-nearly-any-online-purchase-within-two-weeks/', 'http://www.engadget.com/2015/06/03/steam-will-refund-nearly-any-online-purchase-within-two-weeks/', 'http://www.engadget.com/2015/06/03/steam-will-refund-nearly-any-online-purchase-within-two-weeks/', 3, 1433313932, 'http://www.engadget.com/2015/06/03/steam-will-refund-nearly-any-online-purchase-within-two-weeks/'),
(101, 'http://www.engadget.com/2015/06/02/heroes-of-the-storm-out-today/', 'http://www.engadget.com/2015/06/02/heroes-of-the-storm-out-today/', 'http://www.engadget.com/2015/06/02/heroes-of-the-storm-out-today/', 3, 1433313932, 'http://www.engadget.com/2015/06/02/heroes-of-the-storm-out-today/'),
(102, 'http://www.engadget.com/2015/06/02/amd-sixth-gen-a-chip/', 'http://www.engadget.com/2015/06/02/amd-sixth-gen-a-chip/', 'http://www.engadget.com/2015/06/02/amd-sixth-gen-a-chip/', 3, 1433313932, 'http://www.engadget.com/2015/06/02/amd-sixth-gen-a-chip/'),
(103, 'http://www.engadget.com/2015/06/02/gravity-ghost-indie-game-ps4/', 'http://www.engadget.com/2015/06/02/gravity-ghost-indie-game-ps4/', 'http://www.engadget.com/2015/06/02/gravity-ghost-indie-game-ps4/', 3, 1433313932, 'http://www.engadget.com/2015/06/02/gravity-ghost-indie-game-ps4/'),
(104, 'http://www.engadget.com/2015/06/02/logitech-harmony-ps4-control/', 'http://www.engadget.com/2015/06/02/logitech-harmony-ps4-control/', 'http://www.engadget.com/2015/06/02/logitech-harmony-ps4-control/', 3, 1433313932, 'http://www.engadget.com/2015/06/02/logitech-harmony-ps4-control/'),
(105, 'http://www.engadget.com/2015/06/02/magic-leap-augmented-reality-platform/', 'http://www.engadget.com/2015/06/02/magic-leap-augmented-reality-platform/', 'http://www.engadget.com/2015/06/02/magic-leap-augmented-reality-platform/', 3, 1433313932, 'http://www.engadget.com/2015/06/02/magic-leap-augmented-reality-platform/'),
(106, 'http://www.engadget.com/2015/06/02/jxe-streams-metal-gear/', 'http://www.engadget.com/2015/06/02/jxe-streams-metal-gear/', 'http://www.engadget.com/2015/06/02/jxe-streams-metal-gear/', 3, 1433313932, 'http://www.engadget.com/2015/06/02/jxe-streams-metal-gear/'),
(107, 'http://www.engadget.com/2015/06/02/msi-gaming-laptop-concept-eye-tracking/', 'http://www.engadget.com/2015/06/02/msi-gaming-laptop-concept-eye-tracking/', 'http://www.engadget.com/2015/06/02/msi-gaming-laptop-concept-eye-tracking/', 3, 1433313932, 'http://www.engadget.com/2015/06/02/msi-gaming-laptop-concept-eye-tracking/'),
(108, 'http://www.engadget.com/2015/06/02/henry-oculus-story-studio/', 'http://www.engadget.com/2015/06/02/henry-oculus-story-studio/', 'http://www.engadget.com/2015/06/02/henry-oculus-story-studio/', 3, 1433313932, 'http://www.engadget.com/2015/06/02/henry-oculus-story-studio/'),
(109, 'http://www.engadget.com/2015/06/02/amazon-fire-tv-gamefly-app/', 'http://www.engadget.com/2015/06/02/amazon-fire-tv-gamefly-app/', 'http://www.engadget.com/2015/06/02/amazon-fire-tv-gamefly-app/', 3, 1433313932, 'http://www.engadget.com/2015/06/02/amazon-fire-tv-gamefly-app/'),
(110, 'http://www.engadget.com/2015/06/02/youtube-e3-hub/', 'http://www.engadget.com/2015/06/02/youtube-e3-hub/', 'http://www.engadget.com/2015/06/02/youtube-e3-hub/', 3, 1433313932, 'http://www.engadget.com/2015/06/02/youtube-e3-hub/'),
(111, 'http://www.engadget.com/2015/06/02/nintendo-android-rumor-squashed/', 'http://www.engadget.com/2015/06/02/nintendo-android-rumor-squashed/', 'http://www.engadget.com/2015/06/02/nintendo-android-rumor-squashed/', 3, 1433313932, 'http://www.engadget.com/2015/06/02/nintendo-android-rumor-squashed/'),
(112, 'http://www.engadget.com/2015/06/02/lego-dimensions-vs-disney-infinity/', 'http://www.engadget.com/2015/06/02/lego-dimensions-vs-disney-infinity/', 'http://www.engadget.com/2015/06/02/lego-dimensions-vs-disney-infinity/', 3, 1433313932, 'http://www.engadget.com/2015/06/02/lego-dimensions-vs-disney-infinity/'),
(113, 'http://www.engadget.com/2015/06/02/ps4-1tb-fcc/', 'http://www.engadget.com/2015/06/02/ps4-1tb-fcc/', 'http://www.engadget.com/2015/06/02/ps4-1tb-fcc/', 3, 1433313932, 'http://www.engadget.com/2015/06/02/ps4-1tb-fcc/'),
(114, 'http://www.engadget.com/2015/06/02/acer-intel-predator/', 'http://www.engadget.com/2015/06/02/acer-intel-predator/', 'http://www.engadget.com/2015/06/02/acer-intel-predator/', 3, 1433313932, 'http://www.engadget.com/2015/06/02/acer-intel-predator/'),
(115, 'http://www.engadget.com/2015/06/01/xbox-one-indie-pack-australia/', 'http://www.engadget.com/2015/06/01/xbox-one-indie-pack-australia/', 'http://www.engadget.com/2015/06/01/xbox-one-indie-pack-australia/', 3, 1433313932, 'http://www.engadget.com/2015/06/01/xbox-one-indie-pack-australia/'),
(116, 'http://www.engadget.com/2015/06/01/nintendo-new-games-e3-2015/', 'http://www.engadget.com/2015/06/01/nintendo-new-games-e3-2015/', 'http://www.engadget.com/2015/06/01/nintendo-new-games-e3-2015/', 3, 1433313932, 'http://www.engadget.com/2015/06/01/nintendo-new-games-e3-2015/'),
(117, 'http://www.engadget.com/2015/06/01/call-of-duty-advanced-warfare-carrier/', 'http://www.engadget.com/2015/06/01/call-of-duty-advanced-warfare-carrier/', 'http://www.engadget.com/2015/06/01/call-of-duty-advanced-warfare-carrier/', 3, 1433313932, 'http://www.engadget.com/2015/06/01/call-of-duty-advanced-warfare-carrier/'),
(118, 'http://www.engadget.com/2015/06/01/xcom-2-announcement/', 'http://www.engadget.com/2015/06/01/xcom-2-announcement/', 'http://www.engadget.com/2015/06/01/xcom-2-announcement/', 3, 1433313932, 'http://www.engadget.com/2015/06/01/xcom-2-announcement/'),
(119, 'http://www.engadget.com/2015/06/01/lego-worlds/', 'http://www.engadget.com/2015/06/01/lego-worlds/', 'http://www.engadget.com/2015/06/01/lego-worlds/', 3, 1433313932, 'http://www.engadget.com/2015/06/01/lego-worlds/'),
(120, 'http://www.engadget.com/2015/06/01/why-rock-band-4-got-the-gang-back-together/', 'http://www.engadget.com/2015/06/01/why-rock-band-4-got-the-gang-back-together/', 'http://www.engadget.com/2015/06/01/why-rock-band-4-got-the-gang-back-together/', 3, 1433313932, 'http://www.engadget.com/2015/06/01/why-rock-band-4-got-the-gang-back-together/'),
(121, 'http://www.engadget.com/2015/06/01/nvidia-g-sync-comes-to-laptops/', 'http://www.engadget.com/2015/06/01/nvidia-g-sync-comes-to-laptops/', 'http://www.engadget.com/2015/06/01/nvidia-g-sync-comes-to-laptops/', 3, 1433313932, 'http://www.engadget.com/2015/06/01/nvidia-g-sync-comes-to-laptops/'),
(122, 'http://www.engadget.com/2015/06/01/nintendo-nx-android/', 'http://www.engadget.com/2015/06/01/nintendo-nx-android/', 'http://www.engadget.com/2015/06/01/nintendo-nx-android/', 3, 1433313932, 'http://www.engadget.com/2015/06/01/nintendo-nx-android/'),
(123, 'http://www.engadget.com/2015/06/01/agar-io/', 'http://www.engadget.com/2015/06/01/agar-io/', 'http://www.engadget.com/2015/06/01/agar-io/', 3, 1433313932, 'http://www.engadget.com/2015/06/01/agar-io/'),
(124, 'http://www.engadget.com/2015/05/31/nvidia-gtx-980-ti/', 'http://www.engadget.com/2015/05/31/nvidia-gtx-980-ti/', 'http://www.engadget.com/2015/05/31/nvidia-gtx-980-ti/', 3, 1433313932, 'http://www.engadget.com/2015/05/31/nvidia-gtx-980-ti/');

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
