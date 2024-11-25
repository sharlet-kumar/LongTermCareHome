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
-- Table structure for table `foodallergyconflict`
--

DROP TABLE IF EXISTS `foodallergyconflict`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `foodallergyconflict` (
  `foodname` varchar(50) NOT NULL,
  `allergyName` varchar(20) NOT NULL,
  `ConflictCheck` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`foodname`,`allergyName`),
  KEY `FoodAllergyConflict` (`allergyName`),
  CONSTRAINT `foodallergyconflict_ibfk_1` FOREIGN KEY (`foodname`) REFERENCES `food` (`foodname`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `foodallergyconflict_ibfk_2` FOREIGN KEY (`allergyName`) REFERENCES `allergy` (`allergyName`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `foodallergyconflict`
--

LOCK TABLES `foodallergyconflict` WRITE;
/*!40000 ALTER TABLE `foodallergyconflict` DISABLE KEYS */;
INSERT INTO `foodallergyconflict` VALUES ('A','Dust',1),('A','Peanuts',1),('Account','Pollen',1),('Act','Mold',1),('Act','Peanuts',1),('Act','Pollen',1),('Admit','Latex',1),('Admit','Peanuts',1),('Agent','Mold',1),('Agent','Pollen',1),('Allow','Latex',1),('Allow','Shellfish',1),('Always','Latex',1),('Always','Mold',1),('Always','Peanuts',1),('American','Pollen',1),('Arm','Shellfish',1),('Attorney','Mold',1),('Attorney','Pollen',1),('Attorney','Shellfish',1),('Back','Dust',1),('Bar','Pollen',1),('Bar','Shellfish',1),('Before','Latex',1),('Before','Mold',1),('Before','Peanuts',1),('Before','Pollen',1),('Before','Shellfish',1),('Buy','Mold',1),('City','Latex',1),('City','Peanuts',1),('City','Pollen',1),('Claim','Dust',1),('Claim','Latex',1),('Claim','Pollen',1),('Cold','Dust',1),('Cold','Latex',1),('College','Dust',1),('College','Latex',1),('College','Pollen',1),('Company','Mold',1),('Couple','Mold',1),('Couple','Peanuts',1),('Couple','Pollen',1),('Crime','Latex',1),('Crime','Mold',1),('Crime','Peanuts',1),('Decide','Latex',1),('Decide','Shellfish',1),('Decision','Mold',1),('Decision','Peanuts',1),('Decision','Pollen',1),('Detail','Peanuts',1),('Detail','Pollen',1),('Determine','Mold',1),('Difference','Dust',1),('Difference','Mold',1),('Discuss','Latex',1),('Discuss','Mold',1),('Discuss','Pollen',1),('Discuss','Shellfish',1),('Discussion','Pollen',1),('Drug','Mold',1),('Drug','Pollen',1),('Drug','Shellfish',1),('Easy','Pollen',1),('Entire','Shellfish',1),('Especially','Shellfish',1),('Exactly','Dust',1),('Exactly','Mold',1),('Exactly','Pollen',1),('Experience','Dust',1),('Fall','Mold',1),('Father','Dust',1),('Father','Peanuts',1),('Find','Pollen',1),('Finish','Dust',1),('Force','Dust',1),('Force','Pollen',1),('Form','Dust',1),('Form','Latex',1),('Form','Peanuts',1),('Half','Pollen',1),('He','Dust',1),('He','Mold',1),('He','Shellfish',1),('Home','Dust',1),('Home','Latex',1),('Hour','Peanuts',1),('Hour','Pollen',1),('However','Dust',1),('However','Latex',1),('However','Mold',1),('However','Peanuts',1),('If','Latex',1),('If','Pollen',1),('Industry','Dust',1),('Industry','Mold',1),('Industry','Pollen',1),('Itself','Latex',1),('Law','Mold',1),('Left','Dust',1),('Left','Mold',1),('Level','Peanuts',1),('Level','Pollen',1),('Local','Dust',1),('Local','Shellfish',1),('Lose','Dust',1),('Lose','Latex',1),('Lose','Mold',1),('Make','Mold',1),('Make','Peanuts',1),('Make','Pollen',1),('Maybe','Pollen',1),('Maybe','Shellfish',1),('Medical','Dust',1),('Medical','Latex',1),('Medical','Mold',1),('Medical','Pollen',1),('Medical','Shellfish',1),('Member','Dust',1),('Member','Latex',1),('Member','Peanuts',1),('Mention','Mold',1),('Mention','Shellfish',1),('Model','Dust',1),('Money','Mold',1),('Morning','Mold',1),('Morning','Shellfish',1),('Necessary','Dust',1),('Necessary','Peanuts',1),('Necessary','Shellfish',1),('News','Dust',1),('News','Latex',1),('News','Shellfish',1),('Oil','Latex',1),('Order','Dust',1),('Order','Latex',1),('Organization','Latex',1),('Organization','Pollen',1),('Organization','Shellfish',1),('Owner','Latex',1),('Owner','Mold',1),('Place','Dust',1),('Police','Latex',1),('Police','Mold',1),('Police','Shellfish',1),('Public','Dust',1),('Public','Latex',1),('Public','Mold',1),('Ready','Latex',1),('Ready','Mold',1),('Ready','Shellfish',1),('Reflect','Dust',1),('Reflect','Mold',1),('Reflect','Shellfish',1),('Similar','Dust',1),('Similar','Latex',1),('Similar','Mold',1),('Similar','Peanuts',1),('Similar','Pollen',1),('Similar','Shellfish',1),('Sister','Dust',1),('Soon','Dust',1),('Soon','Peanuts',1),('Speak','Dust',1),('Speak','Mold',1),('Structure','Latex',1),('Structure','Peanuts',1),('Structure','Pollen',1),('Stuff','Dust',1),('Stuff','Mold',1),('Stuff','Pollen',1),('Term','Pollen',1),('The','Latex',1),('The','Mold',1),('Them','Latex',1),('Them','Pollen',1),('Them','Shellfish',1),('They','Peanuts',1),('Thing','Latex',1),('Thing','Peanuts',1),('Throughout','Dust',1),('Throughout','Mold',1),('Throughout','Peanuts',1),('Throughout','Shellfish',1),('Throw','Dust',1),('Throw','Latex',1),('Throw','Pollen',1),('Travel','Latex',1),('Travel','Pollen',1),('War','Mold',1),('Whether','Latex',1),('Whether','Mold',1),('Wonder','Dust',1),('Wonder','Peanuts',1),('Wonder','Pollen',1),('Yard','Mold',1),('Yard','Peanuts',1),('Yard','Shellfish',1);
/*!40000 ALTER TABLE `foodallergyconflict` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-11-24 22:32:21
