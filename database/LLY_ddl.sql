--
-- Table structure for table `Customers`
--

DROP TABLE IF EXISTS `Customers`;
CREATE TABLE `Customers` (
	`customerID` int(11) NOT NULL AUTO_INCREMENT,
	`firstName` varchar(255),
	`lastName` varchar(255),
	`customerPhone` varchar(255),
	`email` varchar(255) NOT NULL,
	`password` varchar(255) NOT NULL,
	PRIMARY KEY (`customerID`),
	CONSTRAINT `email` UNIQUE (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=201 DEFAULT CHARSET=utf8;