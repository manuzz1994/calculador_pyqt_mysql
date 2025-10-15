-- MySQL dump 10.13  Distrib 8.0.43, for Win64 (x86_64)
--
-- Host: localhost    Database: calculadora_costos
-- ------------------------------------------------------
-- Server version	8.0.43

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
-- Table structure for table `costos_fijos`
--

DROP TABLE IF EXISTS `costos_fijos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `costos_fijos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `concepto` varchar(100) NOT NULL,
  `precio` decimal(10,2) NOT NULL,
  `aplica_a` enum('todos','difusor','yeso','vela_refill') NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `costos_fijos`
--

LOCK TABLES `costos_fijos` WRITE;
/*!40000 ALTER TABLE `costos_fijos` DISABLE KEYS */;
INSERT INTO `costos_fijos` VALUES (1,'Bolsa',450.00,'todos'),(2,'Etiqueta',2500.00,'todos'),(3,'Pabilo',120.00,'vela_refill'),(4,'Varilla',850.00,'difusor');
/*!40000 ALTER TABLE `costos_fijos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `envases`
--

DROP TABLE IF EXISTS `envases`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `envases` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  `precio` decimal(10,2) NOT NULL,
  `tipo` enum('vela','difusor') NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `envases`
--

LOCK TABLES `envases` WRITE;
/*!40000 ALTER TABLE `envases` DISABLE KEYS */;
INSERT INTO `envases` VALUES (1,'Vaso Whisky',1600.00,'vela'),(2,'Vaso Copon',2500.00,'vela'),(3,'Media esfera',2700.00,'vela'),(4,'Vaso Imperial',1000.00,'vela'),(5,'Taza',1500.00,'vela'),(6,'Vaso Teness Color',1650.00,'vela'),(7,'Vaso Bruna',1500.00,'vela'),(8,'Vaso Imper Color',1100.00,'vela'),(9,'Difusor Auto',1700.00,'difusor'),(10,'Frasco 50',750.00,'difusor'),(11,'Frasco 100',1200.00,'difusor'),(12,'Frasco 125',700.00,'difusor'),(13,'Frasco 200',700.00,'difusor'),(14,'Frasco 200Tapa',2000.00,'difusor'),(15,'Petaca 200 ',1200.00,'difusor'),(16,'Frasco 250',800.00,'difusor');
/*!40000 ALTER TABLE `envases` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `materia_prima`
--

DROP TABLE IF EXISTS `materia_prima`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `materia_prima` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  `precio_por_gramo` decimal(10,2) NOT NULL,
  `tipo` enum('cera','aditivo','escencia','alcohol','yeso','pabilo','varilla','agua') NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `materia_prima`
--

LOCK TABLES `materia_prima` WRITE;
/*!40000 ALTER TABLE `materia_prima` DISABLE KEYS */;
INSERT INTO `materia_prima` VALUES (1,'Cera de soja',5.00,'cera'),(2,'Aditivo',22.50,'aditivo'),(3,'Escencia',70.00,'escencia'),(4,'Alcohol',4.00,'alcohol'),(5,'Yeso',4.50,'yeso'),(6,'Agua',100.00,'agua');
/*!40000 ALTER TABLE `materia_prima` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `receta_ingredientes`
--

DROP TABLE IF EXISTS `receta_ingredientes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `receta_ingredientes` (
  `id` int NOT NULL AUTO_INCREMENT,
  `receta_id` int DEFAULT NULL,
  `materia_prima_id` int DEFAULT NULL,
  `porcentaje` decimal(5,2) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `receta_id` (`receta_id`),
  KEY `materia_prima_id` (`materia_prima_id`),
  CONSTRAINT `receta_ingredientes_ibfk_1` FOREIGN KEY (`receta_id`) REFERENCES `recetas` (`id`) ON DELETE CASCADE,
  CONSTRAINT `receta_ingredientes_ibfk_2` FOREIGN KEY (`materia_prima_id`) REFERENCES `materia_prima` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `receta_ingredientes`
--

LOCK TABLES `receta_ingredientes` WRITE;
/*!40000 ALTER TABLE `receta_ingredientes` DISABLE KEYS */;
INSERT INTO `receta_ingredientes` VALUES (1,1,1,82.00),(2,1,2,8.00),(3,1,3,10.00),(4,3,4,75.00),(5,3,3,25.00),(6,2,1,82.00),(7,2,2,8.00),(8,2,3,10.00);
/*!40000 ALTER TABLE `receta_ingredientes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `recetas`
--

DROP TABLE IF EXISTS `recetas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `recetas` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  `tipo` enum('vela','refill','difusor','yeso') NOT NULL,
  `densidad` decimal(3,2) DEFAULT '1.00',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `recetas`
--

LOCK TABLES `recetas` WRITE;
/*!40000 ALTER TABLE `recetas` DISABLE KEYS */;
INSERT INTO `recetas` VALUES (1,'Vela','vela',0.90),(2,'Refill','refill',0.90),(3,'Difusor','difusor',1.00),(4,'Molde Yeso','yeso',1.00);
/*!40000 ALTER TABLE `recetas` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-10-15  0:14:45
