-- MySQL dump 10.13  Distrib 8.0.41, for Win64 (x86_64)
--
-- Host: localhost    Database: mental_health
-- ------------------------------------------------------
-- Server version	8.0.41

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `answers`
--

DROP TABLE IF EXISTS `answers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `answers` (
  `answer_id` int NOT NULL AUTO_INCREMENT,
  `question_id` int DEFAULT NULL,
  `answer_text` varchar(100) NOT NULL,
  `score` int NOT NULL,
  PRIMARY KEY (`answer_id`),
  KEY `question_id` (`question_id`),
  CONSTRAINT `answers_ibfk_1` FOREIGN KEY (`question_id`) REFERENCES `questions` (`question_id`)
) ENGINE=InnoDB AUTO_INCREMENT=236 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `answers`
--

LOCK TABLES `answers` WRITE;
/*!40000 ALTER TABLE `answers` DISABLE KEYS */;
INSERT INTO `answers` VALUES (1,1,'Never',0),(2,1,'Rarely',1),(3,1,'Sometimes',2),(4,1,'Often',3),(5,1,'Always',4),(6,2,'Never',0),(7,2,'Rarely',1),(8,2,'Sometimes',2),(9,2,'Often',3),(10,2,'Always',4),(11,3,'Never',0),(12,3,'Rarely',1),(13,3,'Sometimes',2),(14,3,'Often',3),(15,3,'Always',4),(16,4,'Never',0),(17,4,'Rarely',1),(18,4,'Sometimes',2),(19,4,'Often',3),(20,4,'Always',4),(21,5,'Never',0),(22,5,'Rarely',1),(23,5,'Sometimes',2),(24,5,'Often',3),(25,5,'Always',4),(26,6,'Never',0),(27,6,'Rarely',1),(28,6,'Sometimes',2),(29,6,'Often',3),(30,6,'Always',4),(31,7,'Never',0),(32,7,'Rarely',1),(33,7,'Sometimes',2),(34,7,'Often',3),(35,7,'Always',4),(36,8,'Never',0),(37,8,'Rarely',1),(38,8,'Sometimes',2),(39,8,'Often',3),(40,8,'Always',4),(41,9,'Never',0),(42,9,'Rarely',1),(43,9,'Sometimes',2),(44,9,'Often',3),(45,9,'Always',4),(46,10,'Never',0),(47,10,'Rarely',1),(48,10,'Sometimes',2),(49,10,'Often',3),(50,10,'Always',4),(51,11,'Never',0),(52,11,'Rarely',1),(53,11,'Sometimes',2),(54,11,'Often',3),(55,11,'Always',4),(56,12,'Never',0),(57,12,'Rarely',1),(58,12,'Sometimes',2),(59,12,'Often',3),(60,12,'Always',4),(61,13,'Never',0),(62,13,'Rarely',1),(63,13,'Sometimes',2),(64,13,'Often',3),(65,13,'Always',4),(66,14,'Never',0),(67,14,'Rarely',1),(68,14,'Sometimes',2),(69,14,'Often',3),(70,14,'Always',4),(71,15,'Never',0),(72,15,'Rarely',1),(73,15,'Sometimes',2),(74,15,'Often',3),(75,15,'Always',4),(76,16,'Never',0),(77,16,'Rarely',1),(78,16,'Sometimes',2),(79,16,'Often',3),(80,16,'Always',4),(81,17,'Never',0),(82,17,'Rarely',1),(83,17,'Sometimes',2),(84,17,'Often',3),(85,17,'Always',4),(86,18,'Never',0),(87,18,'Rarely',1),(88,18,'Sometimes',2),(89,18,'Often',3),(90,18,'Always',4),(91,19,'Never',0),(92,19,'Rarely',1),(93,19,'Sometimes',2),(94,19,'Often',3),(95,19,'Always',4),(96,20,'Never',0),(97,20,'Rarely',1),(98,20,'Sometimes',2),(99,20,'Often',3),(100,20,'Always',4),(101,21,'Never',0),(102,21,'Rarely',1),(103,21,'Sometimes',2),(104,21,'Often',3),(105,21,'Always',4),(106,22,'Never',0),(107,22,'Rarely',1),(108,22,'Sometimes',2),(109,22,'Often',3),(110,22,'Always',4),(111,23,'Never',0),(112,23,'Rarely',1),(113,23,'Sometimes',2),(114,23,'Often',3),(115,23,'Always',4),(116,24,'Never',0),(117,24,'Rarely',1),(118,24,'Sometimes',2),(119,24,'Often',3),(120,24,'Always',4),(121,25,'Never',0),(122,25,'Rarely',1),(123,25,'Sometimes',2),(124,25,'Often',3),(125,25,'Always',4),(126,26,'Never',0),(127,26,'Rarely',1),(128,26,'Sometimes',2),(129,26,'Often',3),(130,26,'Always',4),(131,27,'Never',0),(132,27,'Rarely',1),(133,27,'Sometimes',2),(134,27,'Often',3),(135,27,'Always',4),(136,28,'Never',0),(137,28,'Rarely',1),(138,28,'Sometimes',2),(139,28,'Often',3),(140,28,'Always',4),(141,29,'Never',0),(142,29,'Rarely',1),(143,29,'Sometimes',2),(144,29,'Often',3),(145,29,'Always',4),(146,30,'Never',0),(147,30,'Rarely',1),(148,30,'Sometimes',2),(149,30,'Often',3),(150,30,'Always',4),(151,31,'Never',0),(152,31,'Rarely',1),(153,31,'Sometimes',2),(154,31,'Often',3),(155,31,'Always',4),(156,32,'Never',0),(157,32,'Rarely',1),(158,32,'Sometimes',2),(159,32,'Often',3),(160,32,'Always',4),(161,33,'Never',0),(162,33,'Rarely',1),(163,33,'Sometimes',2),(164,33,'Often',3),(165,33,'Always',4),(166,34,'Never',0),(167,34,'Rarely',1),(168,34,'Sometimes',2),(169,34,'Often',3),(170,34,'Always',4),(171,35,'Never',0),(172,35,'Rarely',1),(173,35,'Sometimes',2),(174,35,'Often',3),(175,35,'Always',4),(176,36,'Never',0),(177,36,'Rarely',1),(178,36,'Sometimes',2),(179,36,'Often',3),(180,36,'Always',4),(181,37,'Never',0),(182,37,'Rarely',1),(183,37,'Sometimes',2),(184,37,'Often',3),(185,37,'Always',4),(186,38,'Never',0),(187,38,'Rarely',1),(188,38,'Sometimes',2),(189,38,'Often',3),(190,38,'Always',4),(191,39,'Never',0),(192,39,'Rarely',1),(193,39,'Sometimes',2),(194,39,'Often',3),(195,39,'Always',4),(196,40,'Never',0),(197,40,'Rarely',1),(198,40,'Sometimes',2),(199,40,'Often',3),(200,40,'Always',4),(201,41,'Never',0),(202,41,'Rarely',1),(203,41,'Sometimes',2),(204,41,'Often',3),(205,41,'Always',4),(226,46,'Never',0),(227,46,'Rarely',1),(228,46,'Sometimes',2),(229,46,'Often',3),(230,46,'Always',4),(231,47,'Never',0),(232,47,'Rarely',1),(233,47,'Sometimes',2),(234,47,'Often',3),(235,47,'Always',4);
/*!40000 ALTER TABLE `answers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `disorder_scores`
--

DROP TABLE IF EXISTS `disorder_scores`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `disorder_scores` (
  `player_id` int NOT NULL,
  `disorder_id` int NOT NULL,
  `total_score` int NOT NULL,
  PRIMARY KEY (`player_id`,`disorder_id`),
  KEY `disorder_id` (`disorder_id`),
  CONSTRAINT `disorder_scores_ibfk_1` FOREIGN KEY (`disorder_id`) REFERENCES `disorders` (`disorder_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `disorder_scores`
--

LOCK TABLES `disorder_scores` WRITE;
/*!40000 ALTER TABLE `disorder_scores` DISABLE KEYS */;
/*!40000 ALTER TABLE `disorder_scores` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `disorders`
--

DROP TABLE IF EXISTS `disorders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `disorders` (
  `disorder_id` int NOT NULL AUTO_INCREMENT,
  `disorder_name` varchar(100) NOT NULL,
  PRIMARY KEY (`disorder_id`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `disorders`
--

LOCK TABLES `disorders` WRITE;
/*!40000 ALTER TABLE `disorders` DISABLE KEYS */;
INSERT INTO `disorders` VALUES (1,'Dysgraphia'),(2,'ADHD'),(3,'Executive Function Disorder (EFD)'),(4,'Intellectual Disabilities'),(5,'Nonverbal Learning Disorder (NVLD)'),(6,'Dyspraxia'),(7,'Sensory Processing Disorder (SPD)'),(8,'Auditory Processing Disorder (APD)'),(9,'Memory-related Disorders'),(10,'Language Processing Disorder (LPD)'),(11,'Global Developmental Delay (GDD)'),(12,'Emotional & Social Learning Disorders'),(13,'Processing Speed Deficits'),(14,'Dyslexia'),(15,'Dyscalculia'),(16,'Visual Processing Disorder'),(17,'Neurocognitive Disorders'),(18,'Mood Disorders'),(19,'Trauma and Stress Disorders'),(20,'Anxiety Disorders'),(21,'Neurodevelopmental Disorders'),(22,'Obsessive-Compulsive Disorder (OCD)'),(23,'Eating Disorders'),(24,'Personality Disorders'),(25,'Substance Use Disorders');
/*!40000 ALTER TABLE `disorders` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `player_responses`
--

DROP TABLE IF EXISTS `player_responses`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `player_responses` (
  `player_id` int NOT NULL,
  `question_id` int NOT NULL,
  `answer_id` int DEFAULT NULL,
  PRIMARY KEY (`player_id`,`question_id`),
  KEY `question_id` (`question_id`),
  KEY `answer_id` (`answer_id`),
  CONSTRAINT `player_responses_ibfk_1` FOREIGN KEY (`question_id`) REFERENCES `questions` (`question_id`),
  CONSTRAINT `player_responses_ibfk_2` FOREIGN KEY (`answer_id`) REFERENCES `answers` (`answer_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `player_responses`
--

LOCK TABLES `player_responses` WRITE;
/*!40000 ALTER TABLE `player_responses` DISABLE KEYS */;
/*!40000 ALTER TABLE `player_responses` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `questions`
--

DROP TABLE IF EXISTS `questions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `questions` (
  `question_id` int NOT NULL AUTO_INCREMENT,
  `question_text` varchar(255) NOT NULL,
  `disorder_id` int DEFAULT NULL,
  PRIMARY KEY (`question_id`),
  KEY `disorder_id` (`disorder_id`),
  CONSTRAINT `questions_ibfk_1` FOREIGN KEY (`disorder_id`) REFERENCES `disorders` (`disorder_id`)
) ENGINE=InnoDB AUTO_INCREMENT=48 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `questions`
--

LOCK TABLES `questions` WRITE;
/*!40000 ALTER TABLE `questions` DISABLE KEYS */;
INSERT INTO `questions` VALUES (1,'Do you struggle to organize your thoughts or ideas clearly when writing, even though you can explain them verbally?',1),(2,'Do you often find it difficult to stay focused on tasks or follow through with plans?',2),(3,'Do you have trouble organizing tasks or managing time effectively, even with reminders?',3),(4,'Do you find it challenging to plan or break down tasks into smaller, manageable steps?',4),(5,'Do you struggle with understanding or judging distances, like when trying to park a car or judge how far away something is?',5),(6,'Do you have difficulty with physical coordination, such as running, catching a ball, or tying your shoes?',6),(7,'Do you feel overwhelmed or disoriented by certain physical activities, like moving quickly or participating in sports?',7),(8,'Do you often struggle to understand spoken instructions, especially in noisy or busy environments?',8),(9,'Do you find it hard to stay focused and remember details when someone gives you multiple instructions at once?',2),(10,'Do you forget instructions or details shortly after they are given to you?',9),(11,'Do you find it difficult to follow spoken directions because the words or sentences feel confusing?',10),(12,'Did you or your child take significantly longer than others to reach milestones like talking or walking?',11),(13,'Do you struggle with coordination tasks, like tying shoelaces, using utensils, or catching a ball?',6),(14,'Do you find it harder than others to learn new skills or process information?',4),(15,'Do you find it difficult to understand body language, facial expressions, or social cues in conversations?',5),(16,'Do you struggle to form or maintain friendships because social interactions feel confusing or overwhelming?',12),(17,'Do you often take longer than others to complete tasks, even when you understand them?',13),(18,'Do you struggle with reading or writing because it takes you longer to process words and sentences?',14),(19,'Do you often get distracted or lose focus, making it hard to finish tasks quickly?',2),(20,'Do you find it challenging to understand complex ideas or solve problems that require critical thinking?',4),(21,'Do you struggle with solving math problems or understanding numerical concepts, even with practice?',15),(22,'Do you have trouble planning steps to solve a problem or figuring out the best way to approach a task?',3),(23,'Do you have difficulty judging distances, tracking moving objects, or coordinating hand-eye movements?',16),(24,'Do certain textures, movements, or physical activities feel overwhelming or uncomfortable for you?',7),(25,'Do you often forget recent conversations, events, or important details, even when you try to remember them?',17),(26,'Do you frequently forget instructions, tasks, or where you placed things, even when trying to stay organized?',2),(27,'Do you struggle to remember and apply information when working on tasks that require multiple steps?',3),(28,'Do you often have trouble falling or staying asleep, even when you feel exhausted?',18),(29,'Do you frequently have nightmares or wake up feeling on edge due to past stressful experiences?',19),(30,'Do you often feel restless or notice your hands or body trembling when you\'re nervous or stressed?',20),(31,'Do you ever experience sudden restlessness or shaking when reminded of a past stressful or traumatic event?',19),(32,'Do you often experience a racing heart or sweating, even in situations that aren’t physically demanding?',20),(33,'Do you ever feel your heart pounding or start sweating suddenly when reminded of a past stressful or traumatic event?',19),(34,'Do you experience sudden mood swings or emotional outbursts that feel difficult to control?',18),(35,'Do certain situations or memories trigger intense emotional reactions that feel overwhelming?',19),(36,'Do you often forget recent events or struggle to recall familiar names, places, or conversations?',17),(37,'Do you frequently forget instructions, tasks, or where you placed things, even when trying to stay organized?',21),(38,'Do you feel the need to perform certain actions, like washing your hands or checking things repeatedly, even when you don’t want to?',22),(39,'Do you often think about food, calories, or body image, even when you\'re not eating or feeling hungry?',23),(40,'Do you often feel uninterested in activities you once enjoyed, like hobbies or spending time with others?',18),(41,'Do you avoid certain places or activities because they remind you of a painful or stressful experience?',19),(46,'Do you often act on impulse without thinking about the possible consequences, even if it risks your well-being or others\'?',24),(47,'Do you sometimes engage in risky behavior, like driving under the influence or using substances in unsafe situations?',25);
/*!40000 ALTER TABLE `questions` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-02-17 16:29:42
