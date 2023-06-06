-- Script to set up the MySQL database

DROP DATABASE IF EXISTS dolianet;
CREATE DATABASE IF NOT EXISTS dolianet;
CREATE USER IF NOT EXISTS 'dolianet_dev'@'localhost' IDENTIFIED BY 'senjuu';
GRANT ALL PRIVILEGES ON dolianet.* TO 'dolianet_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'dolianet_dev'@'localhost';
