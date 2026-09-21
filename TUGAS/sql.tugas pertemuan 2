-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Sep 21, 2026 at 12:26 PM
-- Server version: 9.1.0
-- PHP Version: 8.3.14

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `logika_fuzzy`
--

-- --------------------------------------------------------

--
-- Table structure for table `tb_domain_usia_anak`
--

DROP TABLE IF EXISTS `tb_domain_usia_anak`;
CREATE TABLE IF NOT EXISTS `tb_domain_usia_anak` (
  `id` int NOT NULL AUTO_INCREMENT,
  `b_bawah` decimal(5,2) DEFAULT NULL,
  `b_atas` decimal(5,2) DEFAULT NULL,
  `fungsi` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `tb_domain_usia_anak`
--

INSERT INTO `tb_domain_usia_anak` (`id`, `b_bawah`, `b_atas`, `fungsi`) VALUES
(1, 0.00, 5.00, '0'),
(2, 5.00, 8.00, 'trapesium_up_anak'),
(3, 8.00, 9.00, '1'),
(4, 9.00, 11.00, 'trapesium_down_anak'),
(5, 11.00, 150.00, '0');

-- --------------------------------------------------------

--
-- Table structure for table `tb_domain_usia_bayi`
--

DROP TABLE IF EXISTS `tb_domain_usia_bayi`;
CREATE TABLE IF NOT EXISTS `tb_domain_usia_bayi` (
  `id` int NOT NULL AUTO_INCREMENT,
  `b_bawah` decimal(5,2) DEFAULT NULL,
  `b_atas` decimal(5,2) DEFAULT NULL,
  `fungsi` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `tb_domain_usia_bayi`
--

INSERT INTO `tb_domain_usia_bayi` (`id`, `b_bawah`, `b_atas`, `fungsi`) VALUES
(1, 0.00, 0.00, '0'),
(2, 0.00, 2.00, 'trapesium_up_bayi'),
(3, 2.00, 3.00, '1'),
(4, 3.00, 5.00, 'trapesium_down_bayi'),
(5, 5.00, 150.00, '0');

-- --------------------------------------------------------

--
-- Table structure for table `tb_domain_usia_dewasa`
--

DROP TABLE IF EXISTS `tb_domain_usia_dewasa`;
CREATE TABLE IF NOT EXISTS `tb_domain_usia_dewasa` (
  `id` int NOT NULL AUTO_INCREMENT,
  `b_bawah` decimal(5,2) DEFAULT NULL,
  `b_atas` decimal(5,2) DEFAULT NULL,
  `fungsi` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `tb_domain_usia_dewasa`
--

INSERT INTO `tb_domain_usia_dewasa` (`id`, `b_bawah`, `b_atas`, `fungsi`) VALUES
(1, 0.00, 20.00, '0'),
(2, 20.00, 42.00, 'trapesium_up_dewasa'),
(3, 42.00, 43.00, '1'),
(4, 43.00, 65.00, 'trapesium_down_dewasa'),
(5, 65.00, 150.00, '0');

-- --------------------------------------------------------

--
-- Table structure for table `tb_domain_usia_lansia`
--

DROP TABLE IF EXISTS `tb_domain_usia_lansia`;
CREATE TABLE IF NOT EXISTS `tb_domain_usia_lansia` (
  `id` int NOT NULL AUTO_INCREMENT,
  `b_bawah` decimal(5,2) DEFAULT NULL,
  `b_atas` decimal(5,2) DEFAULT NULL,
  `fungsi` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `tb_domain_usia_lansia`
--

INSERT INTO `tb_domain_usia_lansia` (`id`, `b_bawah`, `b_atas`, `fungsi`) VALUES
(1, 0.00, 60.00, '0'),
(2, 60.00, 69.50, 'trapesium_up_lansia'),
(3, 69.50, 70.50, '1'),
(4, 70.50, 80.00, 'trapesium_down_lansia'),
(5, 80.00, 150.00, '0');

-- --------------------------------------------------------

--
-- Table structure for table `tb_domain_usia_pemuda`
--

DROP TABLE IF EXISTS `tb_domain_usia_pemuda`;
CREATE TABLE IF NOT EXISTS `tb_domain_usia_pemuda` (
  `id` int NOT NULL AUTO_INCREMENT,
  `b_bawah` decimal(5,2) DEFAULT NULL,
  `b_atas` decimal(5,2) DEFAULT NULL,
  `fungsi` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `tb_domain_usia_pemuda`
--

INSERT INTO `tb_domain_usia_pemuda` (`id`, `b_bawah`, `b_atas`, `fungsi`) VALUES
(1, 0.00, 15.00, '0'),
(2, 15.00, 19.00, 'trapesium_up_pemuda'),
(3, 19.00, 20.00, '1'),
(4, 20.00, 24.00, 'trapesium_down_pemuda'),
(5, 24.00, 150.00, '0');

-- --------------------------------------------------------

--
-- Table structure for table `tb_domain_usia_remaja`
--

DROP TABLE IF EXISTS `tb_domain_usia_remaja`;
CREATE TABLE IF NOT EXISTS `tb_domain_usia_remaja` (
  `id` int NOT NULL AUTO_INCREMENT,
  `b_bawah` decimal(5,2) DEFAULT NULL,
  `b_atas` decimal(5,2) DEFAULT NULL,
  `fungsi` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `tb_domain_usia_remaja`
--

INSERT INTO `tb_domain_usia_remaja` (`id`, `b_bawah`, `b_atas`, `fungsi`) VALUES
(1, 0.00, 10.00, '0'),
(2, 10.00, 14.00, 'trapesium_up_remaja'),
(3, 14.00, 15.00, '1'),
(4, 15.00, 19.00, 'trapesium_down_remaja'),
(5, 19.00, 150.00, '0');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
