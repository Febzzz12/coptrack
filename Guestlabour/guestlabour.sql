-- phpMyAdmin SQL Dump
-- version 3.3.9
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: May 31, 2022 at 09:58 AM
-- Server version: 5.5.8
-- PHP Version: 5.3.5

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/* f */;
--
-- Database: `guestlabour`
--

-- --------------------------------------------------------

--
-- Table structure for table `booking`
--

CREATE TABLE IF NOT EXISTS `booking` (
  `bid` int(50) NOT NULL AUTO_INCREMENT,
  `uid` int(50) NOT NULL,
  `lid` int(50) NOT NULL,
  `bdate` varchar(50) NOT NULL,
  `date` varchar(50) NOT NULL,
  `status` varchar(50) NOT NULL,
  `days` varchar(50) NOT NULL,
  `amt` varchar(50) NOT NULL,
  PRIMARY KEY (`bid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `booking`
--

INSERT INTO `booking` (`bid`, `uid`, `lid`, `bdate`, `date`, `status`, `days`, `amt`) VALUES
(1, 1, 7, '2022-05-31 12:18:35.911336', '2022-06-01', 'payed', '2', '200'),
(2, 1, 7, '2022-05-31 12:19:32.289298', '2022-06-01', 'applied', '3', '100');

-- --------------------------------------------------------

--
-- Table structure for table `complaint`
--

CREATE TABLE IF NOT EXISTS `complaint` (
  `cid` int(50) NOT NULL AUTO_INCREMENT,
  `description` varchar(50) NOT NULL,
  `userid` int(50) NOT NULL,
  `actions` varchar(50) NOT NULL,
  `date` varchar(50) NOT NULL,
  PRIMARY KEY (`cid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=5 ;

--
-- Dumping data for table `complaint`
--

INSERT INTO `complaint` (`cid`, `description`, `userid`, `actions`, `date`) VALUES
(1, 'hloooooo', 1, 'haaiiiiiiiiiiii', '2022-05-31 12:12:34.302140'),
(2, 'hai', 1, '', '2022-05-31 12:13:43.346706'),
(3, 'hm', 1, '', '2022-05-31 12:14:04.823225'),
(4, 'k', 1, '', '2022-05-31 12:14:22.905478');

-- --------------------------------------------------------

--
-- Table structure for table `labour`
--

CREATE TABLE IF NOT EXISTS `labour` (
  `lid` int(50) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `age` varchar(50) NOT NULL,
  `aadhar` varchar(50) NOT NULL,
  `voterid` varchar(50) NOT NULL,
  `address` varchar(50) NOT NULL,
  `phone` varchar(50) NOT NULL,
  `place` varchar(50) NOT NULL,
  `pincode` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `job` varchar(50) NOT NULL,
  `status` varchar(50) NOT NULL,
  `police` varchar(50) NOT NULL,
  `img` varchar(50) NOT NULL,
  PRIMARY KEY (`lid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=8 ;

--
-- Dumping data for table `labour`
--

INSERT INTO `labour` (`lid`, `name`, `age`, `aadhar`, `voterid`, `address`, `phone`, `place`, `pincode`, `password`, `job`, `status`, `police`, `img`) VALUES
(7, 'jan', '1998-05-05', '987654321098', '123456', 'jan villa', '9876543210', 'kochi', '682023', 'jan@123', 'Cleaning', 'approved', 'north', 'media/7.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `login`
--

CREATE TABLE IF NOT EXISTS `login` (
  `username` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `usertype` varchar(50) NOT NULL,
  `status` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `login`
--

INSERT INTO `login` (`username`, `password`, `usertype`, `status`) VALUES
('meenu@gmail.com', 'meenu@123', 'user', 'approved'),
('north@gmail.com', 'north@123', 'police', 'approved'),
('9876543210', 'jan@123', 'labour', 'approved'),
('admin@gmail.com', 'admin@123', 'admin', 'approved');

-- --------------------------------------------------------

--
-- Table structure for table `police`
--

CREATE TABLE IF NOT EXISTS `police` (
  `pid` int(50) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `address` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `phone` varchar(50) NOT NULL,
  `place` varchar(50) NOT NULL,
  `pincode` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `status` varchar(50) NOT NULL,
  PRIMARY KEY (`pid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `police`
--

INSERT INTO `police` (`pid`, `name`, `address`, `email`, `phone`, `place`, `pincode`, `password`, `status`) VALUES
(1, 'north', 'kacheripady', 'north@gmail.com', '9876543210', 'kochi', '682023', 'north@123', 'approved');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE IF NOT EXISTS `user` (
  `uid` int(50) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `address` varchar(50) NOT NULL,
  `place` varchar(50) NOT NULL,
  `phone` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `pincode` varchar(50) NOT NULL,
  `status` varchar(50) NOT NULL,
  PRIMARY KEY (`uid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`uid`, `name`, `address`, `place`, `phone`, `email`, `password`, `pincode`, `status`) VALUES
(1, 'meenu', 'kochi', '9876543210', 'meenu villa', 'meenu@gmail.com', 'meenu@123', '682023', 'approved');
