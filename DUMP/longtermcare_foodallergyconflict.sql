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
INSERT INTO `foodallergyconflict` VALUES ('Able','Dust',1),('Able','Peanuts',1),('Above','Dust',1),('Above','Latex',1),('Above','Mold',1),('Above','Shellfish',1),('Act','Latex',1),('Act','Shellfish',1),('Action','Dust',1),('Action','Peanuts',1),('Action','Shellfish',1),('Analysis','Dust',1),('Apply','Latex',1),('Apply','Pollen',1),('Apply','Shellfish',1),('Arm','Latex',1),('Arm','Peanuts',1),('Art','Dust',1),('Attack','Dust',1),('Attack','Latex',1),('Attack','Pollen',1),('Attention','Dust',1),('Attention','Mold',1),('Audience','Mold',1),('Author','Dust',1),('Back','Dust',1),('Back','Pollen',1),('Bar','Latex',1),('Bar','Pollen',1),('Billion','Mold',1),('Billion','Pollen',1),('Billion','Shellfish',1),('Blue','Latex',1),('Blue','Mold',1),('Blue','Peanuts',1),('Blue','Shellfish',1),('Born','Dust',1),('Born','Mold',1),('Break','Latex',1),('Break','Pollen',1),('Break','Shellfish',1),('Bring','Mold',1),('Bring','Peanuts',1),('Bring','Shellfish',1),('Build','Dust',1),('Business','Shellfish',1),('Buy','Shellfish',1),('Call','Dust',1),('Call','Latex',1),('Call','Mold',1),('Capital','Dust',1),('Capital','Latex',1),('Cell','Mold',1),('Cell','Pollen',1),('Central','Dust',1),('Central','Latex',1),('Central','Peanuts',1),('Central','Shellfish',1),('Child','Latex',1),('Child','Shellfish',1),('Class','Mold',1),('Class','Peanuts',1),('Class','Pollen',1),('Class','Shellfish',1),('Clearly','Mold',1),('Clearly','Peanuts',1),('Clearly','Pollen',1),('Coach','Dust',1),('Coach','Shellfish',1),('Cold','Latex',1),('Cold','Peanuts',1),('Cold','Shellfish',1),('Color','Shellfish',1),('Commercial','Pollen',1),('Condition','Latex',1),('Condition','Pollen',1),('Conference','Dust',1),('Conference','Peanuts',1),('Conference','Shellfish',1),('Control','Peanuts',1),('Couple','Dust',1),('Couple','Latex',1),('Couple','Mold',1),('Couple','Shellfish',1),('Culture','Pollen',1),('Dark','Latex',1),('Decide','Latex',1),('Deep','Pollen',1),('Degree','Peanuts',1),('Degree','Pollen',1),('Development','Latex',1),('Development','Mold',1),('Development','Shellfish',1),('Difficult','Mold',1),('Difficult','Shellfish',1),('Direction','Latex',1),('Direction','Mold',1),('Direction','Shellfish',1),('Drive','Shellfish',1),('Drop','Dust',1),('Drop','Peanuts',1),('Drop','Shellfish',1),('Early','Dust',1),('Early','Shellfish',1),('Easy','Dust',1),('Easy','Latex',1),('Easy','Mold',1),('Easy','Pollen',1),('Easy','Shellfish',1),('Economy','Mold',1),('Economy','Peanuts',1),('Economy','Pollen',1),('Edge','Peanuts',1),('Edge','Pollen',1),('Edge','Shellfish',1),('Education','Mold',1),('Education','Peanuts',1),('Effect','Dust',1),('Effect','Latex',1),('Energy','Shellfish',1),('Environment','Peanuts',1),('Evening','Latex',1),('Every','Latex',1),('Every','Mold',1),('Everything','Peanuts',1),('Everything','Pollen',1),('Exist','Mold',1),('Exist','Peanuts',1),('Exist','Shellfish',1),('Family','Peanuts',1),('Feeling','Peanuts',1),('Feeling','Pollen',1),('Field','Latex',1),('Field','Peanuts',1),('Field','Pollen',1),('Finish','Latex',1),('Fire','Latex',1),('Fire','Peanuts',1),('Fire','Pollen',1),('Fire','Shellfish',1),('Food','Pollen',1),('Food','Shellfish',1),('Former','Latex',1),('Former','Mold',1),('Free','Mold',1),('Free','Peanuts',1),('Free','Pollen',1),('Free','Shellfish',1),('Fund','Latex',1),('Fund','Peanuts',1),('Future','Dust',1),('Future','Shellfish',1),('General','Shellfish',1),('Get','Pollen',1),('Get','Shellfish',1),('Goal','Dust',1),('Goal','Mold',1),('Goal','Shellfish',1),('Great','Dust',1),('Great','Peanuts',1),('Great','Pollen',1),('Green','Latex',1),('Green','Mold',1),('Group','Latex',1),('Group','Mold',1),('Group','Pollen',1),('Happen','Shellfish',1),('Herself','Mold',1),('High','Dust',1),('High','Latex',1),('High','Peanuts',1),('High','Pollen',1),('His','Shellfish',1),('Individual','Dust',1),('Information','Dust',1),('Information','Pollen',1),('Inside','Shellfish',1),('Issue','Dust',1),('Issue','Latex',1),('Issue','Mold',1),('Issue','Shellfish',1),('Itself','Dust',1),('Itself','Latex',1),('Itself','Mold',1),('Itself','Pollen',1),('Itself','Shellfish',1),('Key','Latex',1),('Key','Peanuts',1),('Key','Pollen',1),('Letter','Latex',1),('Letter','Pollen',1),('Level','Peanuts',1),('Level','Shellfish',1),('List','Dust',1),('List','Latex',1),('List','Mold',1),('Listen','Peanuts',1),('Listen','Shellfish',1),('Loss','Dust',1),('Loss','Latex',1),('Loss','Peanuts',1),('Low','Mold',1),('Low','Peanuts',1),('Market','Dust',1),('Market','Peanuts',1),('Maybe','Latex',1),('Member','Latex',1),('Member','Peanuts',1),('Million','Latex',1),('Million','Mold',1),('Million','Peanuts',1),('Minute','Dust',1),('Minute','Peanuts',1),('Miss','Dust',1),('Miss','Shellfish',1),('Movement','Dust',1),('Movement','Latex',1),('Mrs','Dust',1),('Mrs','Latex',1),('Music','Latex',1),('Music','Pollen',1),('Nation','Peanuts',1),('Nation','Pollen',1),('National','Dust',1),('National','Mold',1),('Need','Peanuts',1),('Newspaper','Latex',1),('Newspaper','Mold',1),('Newspaper','Pollen',1),('Night','Pollen',1),('None','Mold',1),('None','Shellfish',1),('Of','Peanuts',1),('Offer','Mold',1),('Offer','Peanuts',1),('Official','Mold',1),('Official','Pollen',1),('Oil','Mold',1),('Oil','Peanuts',1),('Oil','Pollen',1),('Oil','Shellfish',1),('Order','Dust',1),('Order','Mold',1),('Order','Pollen',1),('Order','Shellfish',1),('Out','Pollen',1),('Out','Shellfish',1),('Outside','Dust',1),('Outside','Latex',1),('Outside','Peanuts',1),('Outside','Pollen',1),('Own','Mold',1),('Own','Pollen',1),('Owner','Latex',1),('Owner','Mold',1),('Painting','Dust',1),('Painting','Latex',1),('Painting','Shellfish',1),('Party','Peanuts',1),('Party','Shellfish',1),('Pass','Dust',1),('Pass','Mold',1),('Pass','Peanuts',1),('Pass','Pollen',1),('Per','Mold',1),('Per','Shellfish',1),('Point','Peanuts',1),('Police','Dust',1),('Police','Peanuts',1),('Police','Pollen',1),('Practice','Dust',1),('Practice','Latex',1),('Practice','Mold',1),('Practice','Peanuts',1),('Practice','Pollen',1),('Practice','Shellfish',1),('Prevent','Dust',1),('Prevent','Mold',1),('Prevent','Pollen',1),('Probably','Latex',1),('Professor','Dust',1),('Professor','Pollen',1),('Purpose','Dust',1),('Purpose','Peanuts',1),('Purpose','Pollen',1),('Rate','Pollen',1),('Rather','Mold',1),('Rather','Peanuts',1),('Rather','Pollen',1),('Reality','Mold',1),('Reality','Peanuts',1),('Reason','Pollen',1),('Report','Dust',1),('Reveal','Latex',1),('Reveal','Mold',1),('Reveal','Shellfish',1),('Rich','Dust',1),('Rich','Peanuts',1),('Rich','Shellfish',1),('Road','Latex',1),('Road','Mold',1),('Road','Shellfish',1),('Same','Latex',1),('Same','Peanuts',1),('Same','Pollen',1),('Same','Shellfish',1),('Scene','Latex',1),('Scene','Peanuts',1),('School','Dust',1),('School','Latex',1),('Second','Dust',1),('Second','Latex',1),('Second','Shellfish',1),('Seem','Mold',1),('Seem','Peanuts',1),('Seem','Pollen',1),('Senior','Peanuts',1),('Serious','Shellfish',1),('Several','Latex',1),('Several','Peanuts',1),('Several','Pollen',1),('Share','Dust',1),('Share','Peanuts',1),('Single','Pollen',1),('Six','Dust',1),('Six','Latex',1),('Six','Mold',1),('Six','Shellfish',1),('Skin','Dust',1),('Skin','Mold',1),('Skin','Shellfish',1),('Small','Mold',1),('Someone','Latex',1),('Someone','Mold',1),('Someone','Peanuts',1),('Source','Latex',1),('Sport','Latex',1),('Sport','Peanuts',1),('Sport','Pollen',1),('Spring','Mold',1),('Spring','Peanuts',1),('Spring','Pollen',1),('Stage','Dust',1),('Stage','Mold',1),('Stage','Peanuts',1),('Statement','Dust',1),('Statement','Mold',1),('Stay','Peanuts',1),('Street','Shellfish',1),('Subject','Pollen',1),('Suddenly','Latex',1),('Support','Dust',1),('Support','Pollen',1),('Support','Shellfish',1),('Sure','Latex',1),('Sure','Mold',1),('Sure','Shellfish',1),('Table','Dust',1),('Table','Peanuts',1),('Television','Dust',1),('Television','Latex',1),('Television','Pollen',1),('Television','Shellfish',1),('The','Latex',1),('The','Shellfish',1),('They','Latex',1),('They','Mold',1),('Through','Peanuts',1),('Together','Pollen',1),('Top','Latex',1),('Top','Mold',1),('Top','Peanuts',1),('Try','Peanuts',1),('Under','Latex',1),('Under','Mold',1),('Under','Peanuts',1),('Usually','Shellfish',1),('Vote','Dust',1),('Vote','Latex',1),('Vote','Pollen',1),('War','Peanuts',1),('Week','Dust',1),('Week','Mold',1),('Week','Peanuts',1),('Week','Pollen',1),('Which','Peanuts',1),('Why','Pollen',1),('Why','Shellfish',1),('With','Dust',1),('With','Mold',1),('With','Pollen',1),('Without','Latex',1),('Without','Pollen',1),('Would','Latex',1),('Would','Shellfish',1),('Writer','Mold',1),('Writer','Peanuts',1),('Young','Dust',1),('Young','Mold',1),('Young','Shellfish',1);
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

-- Dump completed on 2024-11-24  2:26:22
