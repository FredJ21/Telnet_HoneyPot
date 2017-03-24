DROP DATABASE IF EXISTS honey;
DROP USER IF EXISTS 'honey_user'@'localhost';


CREATE DATABASE honey;


CREATE USER 'honey_user'@'localhost' IDENTIFIED BY 'honey_pass';
GRANT ALL ON honey.* TO 'honey_user'@'localhost';
FLUSH PRIVILEGES;

USE honey;
DROP TABLE IF EXISTS `telnet`;
CREATE TABLE `telnet` (
  `date` datetime NOT NULL,
  `ip` varchar(15) NOT NULL,
  `login` varchar(30) NOT NULL,
  `pass` varchar(30) NOT NULL,
  `timeout` tinyint(1) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


