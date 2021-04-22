--
-- Table structure for table `Customers`
--
USE adoptionproject;
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

<<<<<<< HEAD
INSERT INTO adoptionproject.Customers (email, password) VALUES ('admin@oregonstate.edu', '1234');

--
-- Table structure for table `Pets`
--
USE adoptionproject;
DROP TABLE IF EXISTS `Pets`;
CREATE TABLE `Pets` (
	`petsID` int(11) NOT NULL AUTO_INCREMENT,
	`type` varchar(255), 
	`name` varchar(255) NOT NULL,
	`img` LONGBLOB NOT NULL,
	`breed` varchar(255),
	`age` int(11),
	`size` varchar(255),
	`gender` varchar(255) NOT NULL,
	`goodWithKids` BOOLEAN,
	`goodWithDogs` BOOLEAN,
	`goodWithCats` BOOLEAN,
	`mustBeLeashed` BOOLEAN,
	`availability` varchar(255) NOT NULL,
	PRIMARY KEY (`petsID`)
) ENGINE=InnoDB AUTO_INCREMENT=201 DEFAULT CHARSET=utf8;
=======

>>>>>>> implement the add new pet page for admin
