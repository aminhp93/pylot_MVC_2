-- MySQL dump 10.13  Distrib 5.7.12, for osx10.9 (x86_64)
--
-- Host: 127.0.0.1    Database: belt_exam
-- ------------------------------------------------------
-- Server version	5.6.28

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `books`
--

DROP TABLE IF EXISTS `books`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `books` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) DEFAULT NULL,
  `author` varchar(255) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `books`
--

LOCK TABLES `books` WRITE;
/*!40000 ALTER TABLE `books` DISABLE KEYS */;
INSERT INTO `books` VALUES (16,'Book1','Stephen King 1','2016-09-20 14:16:18',11),(17,'Book2','Stephen King 2','2016-09-20 14:22:19',11),(18,'book3','Stephen King 2','2016-09-20 16:12:35',12),(19,'Book4','Author 4','2016-09-20 16:33:47',13),(20,'fads','Stephen King 1','2016-09-20 18:01:48',12),(21,'fsdf','Stephen King 1','2016-09-20 18:09:35',NULL),(22,'Book6','Author 6','2016-09-20 19:03:28',12),(23,'Use of Weapons','Iain M. Banks','2016-09-20 19:12:28',15),(24,'staff','Stephen King 1','2016-09-20 20:12:05',12);
/*!40000 ALTER TABLE `books` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reviews`
--

DROP TABLE IF EXISTS `reviews`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `reviews` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `review` varchar(255) DEFAULT NULL,
  `rating` int(11) DEFAULT NULL,
  `book_id` int(11) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reviews`
--

LOCK TABLES `reviews` WRITE;
/*!40000 ALTER TABLE `reviews` DISABLE KEYS */;
INSERT INTO `reviews` VALUES (1,'Review 1',2,16,11,'2016-09-20 14:17:51'),(2,'Review2',3,17,11,'2016-09-20 14:22:19'),(3,'Review11',3,16,11,'2016-09-20 14:24:42'),(4,'Review23',1,16,11,'2016-09-20 14:53:06'),(5,'GTS damn',1,16,11,'2016-09-20 14:53:18'),(6,'review for book3',3,18,12,'2016-09-20 16:12:35'),(7,'This is a first review of book 3',1,18,12,'2016-09-20 16:14:44'),(8,'this is my review',1,17,12,'2016-09-20 16:15:17'),(9,'this is my review',1,17,12,'2016-09-20 16:15:49'),(10,'hi guyes',1,16,12,'2016-09-20 16:18:27'),(11,'Review 4',3,19,12,'2016-09-20 16:33:47'),(12,'Review from minh4',1,17,13,'2016-09-20 17:01:34'),(13,'I love SK!',1,16,14,'2016-09-20 17:03:52'),(14,'that is bad',1,16,13,'2016-09-20 18:11:53'),(15,'super bad',1,16,13,'2016-09-20 18:13:29'),(16,'sofas',1,16,12,'2016-09-20 19:02:36'),(17,'Review 6',4,22,12,'2016-09-20 19:03:28'),(18,'hi guyes',1,16,12,'2016-09-20 19:04:14'),(19,'his aksjdf;lkjsadflkjasdlkfjals;kdjfl;aksdjf;ajsdfl;kjsad;lfkjasl;dkfj',1,16,12,'2016-09-20 19:04:50'),(20,'This is an awesome Book!',1,23,15,'2016-09-20 19:12:28'),(21,'Bad book',1,19,15,'2016-09-20 19:15:30'),(22,'This is even better!',1,23,15,'2016-09-20 19:16:51'),(23,'Thesis the wrong book!',2,23,15,'2016-09-20 19:17:31');
/*!40000 ALTER TABLE `reviews` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `alias` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (11,'Minh1','Minh1234','minh1@gmail.com','$2b$12$eETA3VybpdngHHAdusYD2e7/s9ZheA3AQOijN1imZqBHGXYRB3uHO','2016-09-20 13:40:31'),(12,'minh3','Minh1234','minh3@gmail.com','$2b$12$As3iNQvSk7oAoCDl9KNAWOaaGBJB4OXUh2r2/GN1fPFkVs.9D9ys.','2016-09-20 16:11:31'),(13,'minh4@gmail.com','Minh1234','minh4@gmail.com','$2b$12$l1lzWQkHltxKVU0Bo5tvwewvlGBlXSK9klgeEoZ5pwMzs80HskN96','2016-09-20 16:55:33'),(14,'happy','gogolucky','123@gmail.com','$2b$12$HAjovftvgBvgmWw4UM3aceQUhjwI8J1VY6k9TIllfcLaiFeEymtoe','2016-09-20 17:03:17'),(15,'Harvey Chui','Mel','c@c.com','$2b$12$YAALrHfTmsh3WCcPKFXa1emL/hDUpzk0t4iOQbFA0QEDhM1.REq/u','2016-09-20 19:10:59');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-09-22 12:25:07
