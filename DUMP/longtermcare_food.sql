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
-- Table structure for table `food`
--

DROP TABLE IF EXISTS `food`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `food` (
  `foodname` varchar(50) NOT NULL,
  `foodgroup` varchar(20) DEFAULT NULL,
  `calories` int DEFAULT NULL,
  `protein` int DEFAULT NULL,
  `fats` int DEFAULT NULL,
  PRIMARY KEY (`foodname`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `food`
--

LOCK TABLES `food` WRITE;
/*!40000 ALTER TABLE `food` DISABLE KEYS */;
INSERT INTO `food` VALUES ('Able','<class \'type\'>',177,8,13),('Above','<class \'type\'>',166,4,10),('Act','<class \'type\'>',173,12,19),('Action','<class \'type\'>',120,4,15),('Activity','<class \'type\'>',262,15,13),('Analysis','<class \'type\'>',248,18,15),('And','<class \'type\'>',215,17,3),('Apply','<class \'type\'>',196,18,7),('Arm','<class \'type\'>',112,7,2),('Art','<class \'type\'>',82,19,14),('Ask','<class \'type\'>',285,2,2),('Attack','<class \'type\'>',162,6,13),('Attention','<class \'type\'>',286,15,0),('Audience','<class \'type\'>',271,20,16),('Author','<class \'type\'>',249,15,9),('Back','<class \'type\'>',297,7,5),('Bar','<class \'type\'>',225,10,18),('Bed','<class \'type\'>',225,11,15),('Better','<class \'type\'>',163,11,17),('Billion','<class \'type\'>',276,9,17),('Blue','<class \'type\'>',149,5,15),('Born','<class \'type\'>',288,2,2),('Break','<class \'type\'>',259,13,2),('Bring','<class \'type\'>',263,17,20),('Build','<class \'type\'>',100,16,1),('Business','<class \'type\'>',108,9,3),('Buy','<class \'type\'>',163,19,17),('Call','<class \'type\'>',297,13,17),('Capital','<class \'type\'>',126,8,6),('Cell','<class \'type\'>',275,19,17),('Central','<class \'type\'>',87,16,14),('Child','<class \'type\'>',51,8,1),('Class','<class \'type\'>',164,6,5),('Clearly','<class \'type\'>',102,18,20),('Coach','<class \'type\'>',69,10,11),('Cold','<class \'type\'>',199,11,11),('Color','<class \'type\'>',207,1,16),('Commercial','<class \'type\'>',60,20,16),('Condition','<class \'type\'>',182,3,12),('Conference','<class \'type\'>',240,3,14),('Control','<class \'type\'>',116,0,7),('Couple','<class \'type\'>',68,10,0),('Crime','<class \'type\'>',268,6,16),('Culture','<class \'type\'>',180,11,14),('Dark','<class \'type\'>',178,6,8),('Decide','<class \'type\'>',118,18,8),('Deep','<class \'type\'>',264,4,5),('Degree','<class \'type\'>',192,6,6),('Democrat','<class \'type\'>',261,15,19),('Development','<class \'type\'>',115,3,2),('Difficult','<class \'type\'>',94,10,14),('Direction','<class \'type\'>',235,3,1),('Drive','<class \'type\'>',177,6,8),('Drop','<class \'type\'>',167,16,9),('Early','<class \'type\'>',163,18,13),('Easy','<class \'type\'>',119,11,18),('Economy','<class \'type\'>',154,17,1),('Edge','<class \'type\'>',205,12,7),('Education','<class \'type\'>',66,16,20),('Effect','<class \'type\'>',293,19,18),('Energy','<class \'type\'>',200,3,18),('Environment','<class \'type\'>',270,12,14),('Evening','<class \'type\'>',74,3,7),('Every','<class \'type\'>',149,15,4),('Everything','<class \'type\'>',230,1,3),('Exist','<class \'type\'>',179,1,9),('Family','<class \'type\'>',62,3,6),('Feeling','<class \'type\'>',53,3,6),('Field','<class \'type\'>',62,19,0),('Fine','<class \'type\'>',220,1,5),('Finish','<class \'type\'>',276,8,2),('Fire','<class \'type\'>',104,4,3),('Food','<class \'type\'>',85,8,11),('Former','<class \'type\'>',151,2,14),('Free','<class \'type\'>',166,0,2),('Fund','<class \'type\'>',216,16,13),('Future','<class \'type\'>',286,11,12),('General','<class \'type\'>',178,16,15),('Get','<class \'type\'>',211,6,16),('Goal','<class \'type\'>',297,10,15),('Great','<class \'type\'>',74,2,19),('Green','<class \'type\'>',194,1,20),('Group','<class \'type\'>',149,12,3),('Gun','<class \'type\'>',162,13,4),('Happen','<class \'type\'>',220,14,16),('Herself','<class \'type\'>',118,19,12),('High','<class \'type\'>',232,20,5),('His','<class \'type\'>',55,5,0),('Hospital','<class \'type\'>',254,14,17),('Including','<class \'type\'>',141,0,3),('Individual','<class \'type\'>',287,20,8),('Information','<class \'type\'>',61,4,9),('Inside','<class \'type\'>',160,10,0),('Interest','<class \'type\'>',296,4,17),('Issue','<class \'type\'>',88,0,10),('Itself','<class \'type\'>',266,1,17),('Key','<class \'type\'>',255,12,6),('Letter','<class \'type\'>',286,15,11),('Level','<class \'type\'>',189,8,19),('List','<class \'type\'>',193,12,9),('Listen','<class \'type\'>',233,7,2),('Loss','<class \'type\'>',240,11,7),('Low','<class \'type\'>',247,4,5),('Market','<class \'type\'>',119,20,10),('Maybe','<class \'type\'>',69,1,4),('Member','<class \'type\'>',156,4,14),('Million','<class \'type\'>',213,0,5),('Minute','<class \'type\'>',258,2,16),('Miss','<class \'type\'>',233,3,7),('Movement','<class \'type\'>',200,15,10),('Mrs','<class \'type\'>',208,20,8),('Music','<class \'type\'>',165,3,4),('Nation','<class \'type\'>',290,0,18),('National','<class \'type\'>',246,15,1),('Need','<class \'type\'>',237,15,0),('Newspaper','<class \'type\'>',108,6,18),('Night','<class \'type\'>',146,0,2),('None','<class \'type\'>',205,15,0),('Nor','<class \'type\'>',224,7,9),('Of','<class \'type\'>',204,16,7),('Offer','<class \'type\'>',160,2,8),('Official','<class \'type\'>',183,18,14),('Oil','<class \'type\'>',148,4,10),('Order','<class \'type\'>',213,7,13),('Out','<class \'type\'>',110,19,15),('Outside','<class \'type\'>',132,0,10),('Own','<class \'type\'>',230,3,14),('Owner','<class \'type\'>',212,13,19),('Painting','<class \'type\'>',61,19,2),('Party','<class \'type\'>',291,1,2),('Pass','<class \'type\'>',206,14,13),('Per','<class \'type\'>',152,13,19),('Pm','<class \'type\'>',214,2,0),('Point','<class \'type\'>',201,12,18),('Police','<class \'type\'>',162,13,12),('Practice','<class \'type\'>',86,15,18),('Prevent','<class \'type\'>',86,11,20),('Probably','<class \'type\'>',233,18,6),('Professor','<class \'type\'>',82,1,9),('Purpose','<class \'type\'>',75,5,16),('Rate','<class \'type\'>',85,7,5),('Rather','<class \'type\'>',220,15,19),('Real','<class \'type\'>',102,19,19),('Reality','<class \'type\'>',185,8,4),('Reason','<class \'type\'>',120,19,1),('Region','<class \'type\'>',52,5,3),('Report','<class \'type\'>',173,9,6),('Reveal','<class \'type\'>',212,0,12),('Rich','<class \'type\'>',227,8,6),('Road','<class \'type\'>',184,5,6),('Same','<class \'type\'>',242,3,13),('Scene','<class \'type\'>',205,16,2),('School','<class \'type\'>',173,20,9),('Season','<class \'type\'>',267,14,6),('Second','<class \'type\'>',274,6,9),('Seem','<class \'type\'>',107,3,19),('Senior','<class \'type\'>',219,13,17),('Serious','<class \'type\'>',253,4,9),('Several','<class \'type\'>',271,5,19),('Share','<class \'type\'>',235,13,0),('Short','<class \'type\'>',116,3,6),('Single','<class \'type\'>',251,13,18),('Six','<class \'type\'>',193,5,9),('Skin','<class \'type\'>',80,6,0),('Small','<class \'type\'>',132,3,6),('Somebody','<class \'type\'>',72,13,17),('Someone','<class \'type\'>',246,8,3),('Sound','<class \'type\'>',200,11,0),('Source','<class \'type\'>',299,12,11),('Sport','<class \'type\'>',152,12,5),('Spring','<class \'type\'>',196,7,9),('Stage','<class \'type\'>',211,4,1),('Statement','<class \'type\'>',172,6,1),('Stay','<class \'type\'>',87,13,7),('Street','<class \'type\'>',143,4,1),('Subject','<class \'type\'>',77,13,1),('Suddenly','<class \'type\'>',142,19,10),('Support','<class \'type\'>',254,4,16),('Sure','<class \'type\'>',159,16,15),('Table','<class \'type\'>',155,4,6),('Television','<class \'type\'>',265,18,18),('The','<class \'type\'>',263,13,1),('Them','<class \'type\'>',52,0,4),('They','<class \'type\'>',117,11,7),('Through','<class \'type\'>',192,10,16),('Together','<class \'type\'>',288,19,10),('Top','<class \'type\'>',118,11,6),('Try','<class \'type\'>',96,5,12),('Under','<class \'type\'>',118,3,4),('Usually','<class \'type\'>',224,0,1),('Vote','<class \'type\'>',209,10,0),('War','<class \'type\'>',90,1,20),('Week','<class \'type\'>',139,10,19),('Which','<class \'type\'>',250,17,17),('Why','<class \'type\'>',216,2,12),('With','<class \'type\'>',108,4,14),('Without','<class \'type\'>',210,12,4),('Would','<class \'type\'>',265,12,10),('Writer','<class \'type\'>',281,2,17),('Young','<class \'type\'>',68,4,14);
/*!40000 ALTER TABLE `food` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-11-24  2:26:23
