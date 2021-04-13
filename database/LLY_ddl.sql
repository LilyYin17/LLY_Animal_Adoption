--
-- Table structure for table `Customers`
--

DROP TABLE IF EXISTS `Customers`;
CREATE TABLE `Customers` (
	`customerID` int(11) NOT NULL AUTO_INCREMENT,
	`firstName` varchar(255) NOT NULL,
	`lastName` varchar(255) NOT NULL,
	`customerPhone` varchar(255),
	`email` varchar(255) NOT NULL,
	`passwordHash` varchar(255) NOT NULL,
	PRIMARY KEY (`customerID`),
	CONSTRAINT `full_name` UNIQUE (`firstName`, `lastName`),
	CONSTRAINT `email` UNIQUE (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=201 DEFAULT CHARSET=utf8;