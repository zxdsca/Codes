CREATE TABLE `customer` (
    `customerId` int(11) NOT NULL AUTO_INCREMENT,
    `name` varchar(255) DEFAULT NULL,
    `email` varchar(100) DEFAULT NULL,
    `phoneNumber` varchar(15) DEFAULT NULL,
    `password` varchar(100) DEFAULT NULL,
    PRIMARY KEY (`customerId`),
    UNIQUE KEY `email` (`email`)
) 

CREATE TABLE `medicine` (
    `medicineId` int(11) NOT NULL AUTO_INCREMENT,
    `pharmacyId` int(11) DEFAULT NULL,
    `name` varchar(100) DEFAULT NULL,
    `price` double DEFAULT NULL,
    `description` varchar(100) DEFAULT NULL,
    `availableQuantity` int(11) DEFAULT NULL,
    PRIMARY KEY (`medicineId`),
    KEY `pharmacyId` (`pharmacyId`),
    CONSTRAINT `medicine_ibfk_1` FOREIGN KEY (`pharmacyId`) REFERENCES `pharmacy` (`pharmacyId`)
) 

CREATE TABLE `order` (
    `orderId` int(11) NOT NULL AUTO_INCREMENT,
    `customerId` int(11) DEFAULT NULL,
    `pharmacyId` int(11) DEFAULT NULL,
    `orderStatus` varchar(20) DEFAULT NULL,
    `totalPrice` double DEFAULT NULL,
    `deliveryAddress` varchar(50) DEFAULT NULL,
    PRIMARY KEY (`orderId`),
    KEY `customerId` (`customerId`),
    KEY `pharmacyId` (`pharmacyId`),
    CONSTRAINT `order_ibfk_1` FOREIGN KEY (`customerId`) REFERENCES `customer` (`customerId`),
    CONSTRAINT `order_ibfk_2` FOREIGN KEY (`pharmacyId`) REFERENCES `pharmacy` (`pharmacyId`)
) 
CREATE TABLE `orderItem` (
    `orderItem` int(11) NOT NULL AUTO_INCREMENT,
    `orderId` int(11) DEFAULT NULL,
    `medicineId` int(11) DEFAULT NULL,
    `quantity` int(11) DEFAULT NULL,
    PRIMARY KEY (`orderItem`),
    KEY `orderId` (`orderId`),
    KEY `medicineId` (`medicineId`),
    CONSTRAINT `orderItem_ibfk_1` FOREIGN KEY (`orderId`) REFERENCES `order` (`orderId`),
    CONSTRAINT `orderItem_ibfk_2` FOREIGN KEY (`medicineId`) REFERENCES `medicine` (`medicineId`)
) 

CREATE TABLE `payment` (
    `paymentId` int(11) NOT NULL AUTO_INCREMENT,
    `orderId` int(11) DEFAULT NULL,
    `amountPaid` double DEFAULT NULL,
    `paymentDate` date DEFAULT NULL,
    `paymentStatus` varchar(50) DEFAULT NULL,
    PRIMARY KEY (`paymentId`),
    KEY `orderId` (`orderId`),
    CONSTRAINT `payment_ibfk_1` FOREIGN KEY (`orderId`) REFERENCES `order` (`orderId`)
) 

CREATE TABLE `pharmacy` (
    `pharmacyId` int(11) NOT NULL AUTO_INCREMENT,
    `name` varchar(100) DEFAULT NULL,
    `address` varchar(255) DEFAULT NULL,
    `licenseNumber` varchar(25) DEFAULT NULL,
    `contactNumber` varchar(25) DEFAULT NULL,
    PRIMARY KEY (`pharmacyId`)
) 

