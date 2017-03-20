DROP TABLE IF EXISTS `telnet`;
CREATE TABLE `telnet` (
  `date` datetime NOT NULL,
  `ip` varchar(15) NOT NULL,
  `login` varchar(30) NOT NULL,
  `pass` varchar(30) NOT NULL,
  `timeout` tinyint(1) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


