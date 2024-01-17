-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 16, 2024 at 04:25 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `sport_centre`
--

-- --------------------------------------------------------

--
-- Table structure for table `damage`
--

CREATE TABLE `damage` (
  `Item` varchar(30) NOT NULL,
  `Total_Damaged` int(30) NOT NULL,
  `Item_Price` int(30) NOT NULL,
  `Total_Price` int(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `damage`
--

INSERT INTO `damage` (`Item`, `Total_Damaged`, `Item_Price`, `Total_Price`) VALUES
('bicycle', 2, 200, 400),
('netball', 1, 40, 40),
('rugby', 2, 50, 100);

-- --------------------------------------------------------

--
-- Table structure for table `registration`
--

CREATE TABLE `registration` (
  `Name` varchar(30) NOT NULL,
  `ID` int(10) NOT NULL,
  `Phone` int(20) NOT NULL,
  `Email` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `registration`
--

INSERT INTO `registration` (`Name`, `ID`, `Phone`, `Email`) VALUES
('hawa', 0, 172956188, 'hawa12@gmail.com'),
('khuz', 0, 1123035342, 'khuz28@gmail.com'),
('liya', 0, 187643259, '00liya@gmail.com');

-- --------------------------------------------------------

--
-- Table structure for table `rental`
--

CREATE TABLE `rental` (
  `Court` varchar(30) NOT NULL,
  `Items` varchar(30) NOT NULL,
  `Count_Items` int(10) NOT NULL,
  `Day` int(10) NOT NULL,
  `Total_Price` int(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `rental`
--

INSERT INTO `rental` (`Court`, `Items`, `Count_Items`, `Day`, `Total_Price`) VALUES
('Court A', 'Netball', 5, 10, 35),
('No', 'Bicycle', 2, 5, 21),
('Field', 'Rugby', 3, 20, 35);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
