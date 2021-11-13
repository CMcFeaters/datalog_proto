-- MariaDB dump 10.19  Distrib 10.6.4-MariaDB, for Win64 (AMD64)
--
-- Host: localhost    Database: datalogdb2
-- ------------------------------------------------------
-- Server version	10.6.4-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `bearings`
--

DROP TABLE IF EXISTS `bearings`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bearings` (
  `EID` int(11) NOT NULL AUTO_INCREMENT,
  `bearingName` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `ts` datetime DEFAULT NULL,
  `value0` float DEFAULT NULL,
  `value1` float DEFAULT NULL,
  `value2` float DEFAULT NULL,
  `value3` float DEFAULT NULL,
  `value4` float DEFAULT NULL,
  `datalog_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`EID`),
  KEY `datalog_id` (`datalog_id`),
  CONSTRAINT `bearings_ibfk_1` FOREIGN KEY (`datalog_id`) REFERENCES `datalog` (`CID`)
) ENGINE=InnoDB AUTO_INCREMENT=88000101 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `datalog`
--

DROP TABLE IF EXISTS `datalog`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `datalog` (
  `CID` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`CID`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `fans`
--

DROP TABLE IF EXISTS `fans`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `fans` (
  `EID` int(11) NOT NULL AUTO_INCREMENT,
  `fanName` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `ts` datetime DEFAULT NULL,
  `value0` float DEFAULT NULL,
  `value1` float DEFAULT NULL,
  `value2` float DEFAULT NULL,
  `value3` float DEFAULT NULL,
  `value4` float DEFAULT NULL,
  `datalog_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`EID`),
  KEY `datalog_id` (`datalog_id`),
  CONSTRAINT `fans_ibfk_1` FOREIGN KEY (`datalog_id`) REFERENCES `datalog` (`CID`)
) ENGINE=InnoDB AUTO_INCREMENT=87925078 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `motors`
--

DROP TABLE IF EXISTS `motors`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `motors` (
  `EID` int(11) NOT NULL AUTO_INCREMENT,
  `motorName` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `ts` datetime DEFAULT NULL,
  `value0` float DEFAULT NULL,
  `value1` float DEFAULT NULL,
  `value2` float DEFAULT NULL,
  `value3` float DEFAULT NULL,
  `value4` float DEFAULT NULL,
  `datalog_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`EID`),
  KEY `datalog_id` (`datalog_id`),
  CONSTRAINT `motors_ibfk_1` FOREIGN KEY (`datalog_id`) REFERENCES `datalog` (`CID`)
) ENGINE=InnoDB AUTO_INCREMENT=87900101 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-11-12 20:04:10
