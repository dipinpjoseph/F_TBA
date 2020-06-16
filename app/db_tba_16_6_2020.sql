-- MySQL dump 10.17  Distrib 10.3.22-MariaDB, for debian-linux-gnueabihf (armv8l)
--
-- Host: localhost    Database: db_tba
-- ------------------------------------------------------
-- Server version	10.3.22-MariaDB-0+deb10u1

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
-- Table structure for table `e_list`
--

DROP TABLE IF EXISTS `e_list`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `e_list` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `topic` varchar(1000) DEFAULT NULL,
  `sol` varchar(1000) DEFAULT NULL,
  `comment` varchar(1000) DEFAULT NULL,
  `cat` varchar(200) DEFAULT NULL,
  `votes` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `e_list`
--

LOCK TABLES `e_list` WRITE;
/*!40000 ALTER TABLE `e_list` DISABLE KEYS */;
INSERT INTO `e_list` VALUES (1,'How to replace Column Value in SQL?','update table_name set column = \'newvalue\' where column = \'some thing\' ','The command \'set\' fills new value based on condition given in \'where\'','SQL',0),(2,'Create bootable USB using \'dd\' command.','sudo dd bs=4M if=path/to/input.iso of=/dev/sd conv=fdatasync status=progress ','Replace input file path and drive letter(sda/b/c). Use \'lsblk\' if confused. <br>Source - https://askubuntu.com/a/377561','Linux',0),(3,'Install .deb file in Linux.','sudo dpkg -i /path/a.deb','Use \'sudo apt install -f\' for any missing dependencies. <br>Source - https://unix.stackexchange.com/a/159114','Linux',0),(4,'Display the first few words of a file in Linux.','head -c 100 filename','Prints first 100 bytes of the file. <br>Source - https://unix.stackexchange.com/a/167816','Linux',0),(5,'Display last few words of a file in Linux.','tail -c 100 filename ','Prints last 100 bytes of the file. <br>Source - https://unix.stackexchange.com/a/167816','Linux',0),(6,'Append words to the end of the file in Linux.','echo \'input\' >> filename','Attachs the input to the file. <br>Source - https://www.cyberciti.biz/faq/linux-append-text-to-end-of-file/','Linux',0),(7,'Insert text into the begining of a file in Linux.','sed -i \'1s/^/abcde /\' filename','Attachs the input to the file beginning. <br>Source - https://stackoverflow.com/a/9533736/6903724','Linux',0),(8,'Search and Replace a word in the file using Python','# Read and save file content <br>with open(\'file.txt\', \'r\') as file : <br>filedata = file.read() <br># Replace words with new ones. <br>filedata = filedata.replace(\'abc\', \'def\') <br># Overwrite the file with new contents <br>with open(\'file.txt\', \'w\') as file: <br>file.write(filedata)','Open and read the file and replace the necessary words. Later write modified content to the same file. <br>Source-https://stackoverflow.com/a/17141572/6903724','Python',0),(9,'Install virtualenv for Python3','sudo apt-get install python3-pip <br>sudo pip3 install virtualenv <br>virtualenv -p python3 myenv <br>source venv/bin/activate ','Source-https://gist.github.com/Geoyi/d9fab4f609e9f75941946be45000632b','Python',0),(11,'Kill a linux process by its name.','kill -9 $(ps -ef | grep \"name\" | grep -o \"[0-9]*\" | head -1)','\'ps -ef\' will display all process, by using series of \'grep\' and \'head\' the PID of the corresponding process is obtained and later fed to kill command. \'kill -9\' command cannot be blocked.','Linux',0),(12,'Filter rows by column value in PySpark.','# Showing non-empty rows; <br>df.where(F.col(\"col_name\").like(\"% %\") == False).show()','Filtering out rows with column value spaces(\"    \").','Spark',0),(13,'Create new column in Spark Dataframe from existing column using withColumn method.','df = df.withColumn(\'new_col\', df.old_col[1:2])','A new column \'new_col\' is added to dataframe \'df\' containing first two characters of column \'old_col\'.','Spark',0),(14,'Groupby and aggregate example in PySpark.','df.groupby(\"col\").agg(F.min(\'agg_col\').alias(\'agg\')).orderBy(\'col\', ascending=True)','Here, rows in \'df\' are grouped by \'col\' column values and minimum value of \'agg_col\' is found out for each group. ','Spark',0),(15,'Save Spark Dataframe as Apache Parquet storage in HDFS.','df.write.parquet(\"hdfs:///user/abc123/outputs/df.parquet\")','Above statement will save dataframe \'df\' to given HDFS location in parquet format.','Spark',0),(16,'Load Fixed Width Text file as Dataframe in PySpark.','df = spark.read.text(\"hdfs:///path/to/dir\") <br>df = df.select( <br>    df.value.substr(1,2).alias(\'ID\'), <br>    df.value.substr(4,57).alias(\'NAME\') )','Using \'spark.read\' the file is loaded as undefined Spark Dataframe . Later using substr() data is split and assigned to two columns. (4,57) implies 57 characters starting from 4th position.','Spark',0),(17,'How to change resolution of VNC server in Raspberry Pi using Terminal?','vncserver -randr=800x600','Next login onwards the resolution will be changed to 800x600.','Raspberry-Pi',0),(18,'How to backup MySQL database?','mysqldump -u user_name –p db_name > backup.sql;','Executing this command will prompt for your mysql password and upon completion a backup file named \'backup.sql\' will be generated. <br>Source - https://support.hostway.com/hc/en-us/articles/360000220190-How-to-backup-and-restore-MySQL-databases-on-Linux','SQL',0),(19,'Train and Test split in R','# Males - Dataset <br># 70% of the sample size <br>smp_size <- floor(0.7 * nrow(Males)) <br># Train and Test Split <br>train_int <- sample(seq_len(nrow(Males)), size = smp_size) <br># 70% training data <br>tr <- Males[train_int, ] <br># 30% test data te <- Males[-train_int, ]','First, Get the number of rows of dataset and randomly spit to required ratio(0.7 here). Then create two dataframes using extracted row numbers.','R',0),(21,'Generate Density Plot in Plotly | R','de_b <- density(Males$exper) <br>de_b <- data.frame(x = de_b$x, y = de_b$y) <br>before <- plot_ly(data = de_b, x = ~ x, y = ~ y) <br>layout(add_lines(before), title = \"Density plot of non-transformed variable\")','Density of the variable was found by density() method and fed data to plotly line graph. Output is avaliable at <a href=\"https://photos.app.goo.gl/7m7BzPFkFzRHY9xk6\">Density Plot</a>','R',0),(22,'Scatter Plot with custom hover text in Plotly | R','# Males - Dataset <br>h_dat = paste(\"Obs No :\", rownames(Males)) <br>sc <- <br>  plot_ly( <br>    data = Males, <br>    x = ~school, <br>    y = ~exper, <br>    hover_data = \'text\', <br>    text = h_dat <br>  ) <br>layout(sc, <br>       yaxis = list(title = \"school\"), <br>       xaxis = list(title = \"exper\") <br>)','Just specify columns for x and y axis. The output figure is available at <a href=\"https://photos.app.goo.gl/SJaWnDcoFbwN3bqH9\">Scatter Plot</a>','R',0);
/*!40000 ALTER TABLE `e_list` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-06-16  2:02:55
