-- phpMyAdmin SQL Dump
-- version 4.4.10
-- http://www.phpmyadmin.net
--
-- Host: localhost:8889
-- Generation Time: Feb 24, 2017 at 07:30 PM
-- Server version: 5.5.42
-- PHP Version: 5.6.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `rentals`
--

--
-- Dumping data for table `rentalsapp_contract`
--

INSERT INTO `rentalsapp_contract` (`id`, `erc_firstName`, `erc_initial`, `erc_lastName`, `erc_cellPhone`, `erc_street`, `erc_city`, `erc_state`, `erc_zip`, `erc_weight`, `erc_height`, `erc_age`, `erc_emailAddress`, `erc_skierType`, `erc_snowboardStance`) VALUES
(1, 'Chris', 'D', 'Pauley', '2152626075', '46 Red Oak Road', 'Lake Harmony', 'PA', '18624', '165', '5'' 10"', 54, 'pauleyc@yahoo.com', '3', '');

--
-- Dumping data for table `rentalsapp_item`
--

INSERT INTO `rentalsapp_item` (`id`, `title`, `description`, `amount`) VALUES
(1, 'Title One', 'Description One', 12),
(2, 'Item Title two', 'Item description for item 2.', 10),
(3, 'Item three', 'This is the description for itme 3.', 30);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
