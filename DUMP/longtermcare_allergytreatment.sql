-- MySQL dump 10.13  Distrib 8.0.40, for Win64 (x86_64)
--
-- Host: localhost    Database: longtermcare
-- ------------------------------------------------------
-- Server version	8.0.40

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `allergytreatment`
--

DROP TABLE IF EXISTS `allergytreatment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `allergytreatment` (
  `allergyName` varchar(20) NOT NULL,
  `treatment` varchar(160) NOT NULL,
  `considerations` varchar(160) DEFAULT NULL,
  PRIMARY KEY (`allergyName`,`treatment`),
  CONSTRAINT `allergytreatment_ibfk_1` FOREIGN KEY (`allergyName`) REFERENCES `allergy` (`allergyName`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `allergytreatment`
--

LOCK TABLES `allergytreatment` WRITE;
/*!40000 ALTER TABLE `allergytreatment` DISABLE KEYS */;
INSERT INTO `allergytreatment` VALUES ('Dust','Man your face government lay add difference.','Parent reflect begin shake hair.'),('Latex','Always season want against none occur only.','Recently leave course space force station thing.'),('Mold','Address affect throw them event walk.','Perform meet letter.'),('Peanuts','No idea avoid share option fire.','Should rock guess wind us kitchen community.'),('Pollen','Structure reflect gun anything.','Shoulder capital against loss thing.'),('Shellfish','Visit product resource pretty.','Recent capital entire general total pull.');
/*!40000 ALTER TABLE `allergytreatment` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-11-24  2:26:21
