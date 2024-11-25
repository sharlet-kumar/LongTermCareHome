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
INSERT INTO `food` VALUES ('A','Fruit',230,5,5),('Account','Dairy',267,2,14),('Act','Fruit',92,4,3),('Admit','Protein',86,11,4),('Agency','Dairy',132,9,6),('Agent','Fruit',94,12,7),('Allow','Grain',205,6,11),('Always','Vegetable',86,17,7),('American','Grain',249,9,9),('Arm','Fruit',71,19,17),('Attorney','Dairy',224,4,17),('Audience','Vegetable',286,11,10),('Back','Vegetable',117,19,19),('Bar','Dairy',269,8,1),('Base','Dairy',253,2,17),('Before','Vegetable',80,5,9),('Buy','Grain',124,14,15),('City','Dairy',50,20,17),('Claim','Fruit',228,18,2),('Cold','Fruit',101,12,15),('College','Vegetable',70,8,17),('Company','Protein',207,19,3),('Couple','Vegetable',278,6,7),('Crime','Fruit',194,18,7),('Day','Vegetable',199,11,15),('Decide','Fruit',225,11,10),('Decision','Vegetable',277,4,4),('Detail','Fruit',127,14,12),('Determine','Fruit',266,3,17),('Difference','Fruit',159,14,3),('Discuss','Grain',236,19,15),('Discussion','Dairy',128,19,7),('Drug','Fruit',274,12,9),('Easy','Vegetable',284,5,3),('Entire','Fruit',220,5,19),('Especially','Protein',208,3,16),('Exactly','Dairy',158,17,5),('Experience','Grain',134,15,9),('Fall','Dairy',238,2,4),('Father','Protein',140,9,0),('Find','Vegetable',180,11,12),('Finish','Protein',296,4,9),('Force','Dairy',101,1,15),('Form','Protein',295,9,15),('Half','Grain',195,20,17),('Happen','Fruit',258,11,1),('He','Dairy',97,16,10),('Her','Vegetable',91,18,17),('Home','Fruit',217,18,11),('Hour','Vegetable',161,13,1),('However','Dairy',123,5,13),('If','Protein',227,10,9),('Industry','Grain',288,4,17),('Itself','Vegetable',114,4,20),('Law','Protein',129,6,15),('Left','Protein',195,19,19),('Level','Grain',157,17,3),('Local','Grain',290,11,16),('Look','Dairy',96,14,2),('Lose','Dairy',247,6,6),('Make','Fruit',105,10,12),('Maybe','Fruit',50,18,9),('Medical','Fruit',138,6,0),('Member','Vegetable',81,1,10),('Mention','Vegetable',154,14,11),('Miss','Vegetable',133,9,3),('Model','Fruit',100,0,0),('Money','Fruit',58,18,19),('Morning','Dairy',110,10,5),('Necessary','Protein',184,11,7),('News','Protein',199,3,11),('Oil','Grain',169,12,14),('Order','Dairy',212,13,4),('Organization','Protein',192,20,20),('Owner','Dairy',101,1,17),('Place','Protein',195,0,18),('Police','Fruit',256,1,14),('Public','Dairy',102,17,3),('Ready','Vegetable',148,1,7),('Reflect','Protein',268,10,7),('Sense','Vegetable',122,8,3),('Similar','Dairy',110,7,17),('Sister','Vegetable',204,0,10),('Soon','Dairy',173,5,9),('Speak','Vegetable',282,15,7),('Structure','Dairy',204,1,6),('Stuff','Dairy',248,19,18),('Subject','Fruit',296,0,7),('Term','Protein',160,3,18),('The','Fruit',122,6,7),('Them','Fruit',213,4,9),('They','Fruit',59,10,5),('Thing','Grain',178,14,18),('Throughout','Vegetable',188,12,5),('Throw','Vegetable',236,4,19),('Travel','Grain',110,12,14),('War','Fruit',286,16,0),('Whether','Vegetable',208,1,16),('Wonder','Dairy',228,0,12),('Yard','Grain',166,0,5);
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

-- Dump completed on 2024-11-24 22:32:20
