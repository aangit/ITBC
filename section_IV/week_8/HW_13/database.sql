-- phpMyAdmin SQL Dump
-- version 4.5.1
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: Sep 15, 2019 at 03:16 PM
-- Server version: 10.1.9-MariaDB
-- PHP Version: 5.6.15

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `it350ispit`
--

-- --------------------------------------------------------

--
-- Table structure for table `aircraft`
--

CREATE TABLE `aircraft` (
  `AircraftID` smallint(4) UNSIGNED NOT NULL,
  `AircraftTypeID` smallint(4) UNSIGNED NOT NULL,
  `RegNum` char(6) NOT NULL,
  `LastMaintEnd` date NOT NULL,
  `NextMaintBegin` date NOT NULL,
  `NextMaintEnd` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `aircraft`
--

INSERT INTO `aircraft` (`AircraftID`, `AircraftTypeID`, `RegNum`, `LastMaintEnd`, `NextMaintBegin`, `NextMaintEnd`) VALUES
(3125, 617, 'ZX1386', '2019-02-12', '2019-02-01', '2019-02-22'),
(3128, 617, 'ZX7634', '2019-01-07', '2019-05-07', '2019-05-18'),
(3130, 618, 'ZX7391', '2019-02-15', '2019-04-15', '2019-05-15'),
(3145, 503, 'ZX5731', '2019-02-17', '2019-12-20', '2019-12-30'),
(3189, 616, 'ZX5823', '2019-03-07', '2019-11-05', '2019-11-12'),
(3201, 617, 'ZX7472', '2019-02-15', '2019-10-15', '2019-10-27'),
(3223, 618, 'ZX1037', '2019-03-06', '2019-09-16', '2019-09-30'),
(3425, 504, 'ZX6821', '2019-02-22', '2019-05-25', '2019-06-04'),
(3427, 616, 'ZX5921', '2019-02-01', '2019-03-02', '2019-04-02'),
(3451, 503, 'ZX6488', '2019-01-01', '2019-06-23', '2019-06-30'),
(3452, 617, 'ZX5464', '2019-01-04', '2019-01-03', '2019-01-21'),
(3465, 503, 'ZX5373', '2019-12-15', '2020-12-14', '2019-05-21'),
(3467, 616, 'ZX7283', '2019-02-05', '2019-12-02', '2019-10-09'),
(3469, 616, 'ZX5382', '2019-01-16', '2019-04-08', '2019-04-18'),
(3470, 616, 'ZX5173', '2019-04-20', '2019-10-05', '2019-10-15'),
(3565, 504, 'ZX5830', '2019-01-19', '2019-11-15', '2019-12-15'),
(4130, 619, 'XX7391', '2019-02-15', '2019-04-15', '2019-05-15'),
(4201, 619, 'XX7472', '2019-02-15', '2019-10-15', '2019-10-27'),
(4223, 505, 'XX1037', '2019-03-06', '2019-09-16', '2019-09-30'),
(4565, 505, 'XX5830', '2019-01-19', '2019-11-15', '2019-12-15');

-- --------------------------------------------------------

--
-- Table structure for table `aircrafttype`
--

CREATE TABLE `aircrafttype` (
  `AircraftTypeID` smallint(4) UNSIGNED NOT NULL,
  `AircraftName` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `aircrafttype`
--

INSERT INTO `aircrafttype` (`AircraftTypeID`, `AircraftName`) VALUES
(503, 'Boeing 747'),
(504, 'Boeing 767'),
(505, 'Boeing 777'),
(615, 'Airbus A300SW/310SM'),
(616, 'Airbus A330'),
(617, 'Airbus A340SW'),
(618, 'Airbus A380SM'),
(619, 'Airbus A380SW');

-- --------------------------------------------------------

--
-- Table structure for table `airport`
--

CREATE TABLE `airport` (
  `AirportID` smallint(5) UNSIGNED NOT NULL,
  `AirportCode` char(3) NOT NULL,
  `AirportName` varchar(255) NOT NULL,
  `CityName` varchar(255) NOT NULL,
  `CountryCode` char(2) NOT NULL,
  `NumRunways` tinyint(1) UNSIGNED NOT NULL,
  `NumTerminals` tinyint(1) UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `airport`
--

INSERT INTO `airport` (`AirportID`, `AirportCode`, `AirportName`, `CityName`, `CountryCode`, `NumRunways`, `NumTerminals`) VALUES
(34, 'ORY', 'Orly Airport', 'Paris', 'FR', 3, 2),
(48, 'LGW', 'Gatwick Airport', 'London', 'UK', 2, 2),
(56, 'LHR', 'Heathrow Airport', 'London', 'UK', 2, 5),
(59, 'CIA', 'Rome Ciampino Airport', 'Rome', 'IT', 1, 1),
(62, 'AMS', 'Schiphol Airport', 'Amsterdam', 'NL', 6, 1),
(72, 'BCN', 'Barcelona International Airport', 'Barcelona', 'ES', 3, 3),
(74, 'MUC', 'Franz Josef Strauss Airport', 'Munich', 'DE', 3, 2),
(83, 'LIS', 'Lisbon Airport', 'Lisbon', 'PT', 2, 2),
(87, 'BUD', 'Budapest Ferihegy International Airport', 'Budapest', 'HU', 2, 2),
(92, 'ZRH', 'Zurich Airport ', 'Zurich', 'CH', 3, 1),
(126, 'BOM', 'Chhatrapati Shivaji International Airport ', 'Bombay', 'IN', 2, 2),
(129, 'BRS', 'Bristol International Airport', 'Bristol', 'UK', 1, 1),
(132, 'MAD', 'Barajas Airport', 'Madrid', 'ES', 4, 4),
(165, 'NCE', 'Nice Côte d''Azur Airport ', 'Nice', 'FR', 2, 2),
(201, 'SIN', 'Changi Airport', 'Singapore', 'SG', 3, 3);

-- --------------------------------------------------------

--
-- Table structure for table `class`
--

CREATE TABLE `class` (
  `ClassID` int(11) NOT NULL,
  `ClassName` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `class`
--

INSERT INTO `class` (`ClassID`, `ClassName`) VALUES
(1, 'Platinum'),
(2, 'Gold'),
(3, 'Silver'),
(4, 'Reular');

-- --------------------------------------------------------

--
-- Table structure for table `flight`
--

CREATE TABLE `flight` (
  `FlightID` smallint(4) UNSIGNED NOT NULL,
  `RouteID` smallint(4) UNSIGNED NOT NULL,
  `AircraftID` smallint(4) UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `flight`
--

INSERT INTO `flight` (`FlightID`, `RouteID`, `AircraftID`) VALUES
(345, 1003, 3452),
(535, 1005, 3451),
(589, 1097, 3467),
(652, 1018, 3465),
(662, 1018, 3465),
(663, 1009, 3427),
(671, 1169, 3201),
(672, 1169, 3223),
(674, 1165, 3427),
(675, 1023, 3451),
(681, 1123, 3189),
(685, 1180, 3470),
(687, 1191, 3128),
(688, 1139, 3130),
(689, 1140, 3130),
(702, 1008, 3469),
(708, 1006, 3469),
(724, 1193, 3125),
(725, 1192, 3125),
(765, 1133, 3425),
(812, 1190, 3565),
(826, 1209, 3469),
(833, 1061, 3469),
(857, 1059, 3565),
(871, 1173, 3201),
(872, 1173, 3223),
(876, 1175, 3467),
(877, 1176, 3467),
(896, 1141, 3145),
(897, 1142, 3145),
(898, 1141, 3145),
(899, 1142, 3145);

-- --------------------------------------------------------

--
-- Table structure for table `flightclass`
--

CREATE TABLE `flightclass` (
  `FlightID` smallint(6) NOT NULL,
  `ClassID` char(1) NOT NULL,
  `MaxSeats` smallint(6) NOT NULL,
  `BasePrice` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `flightclass`
--

INSERT INTO `flightclass` (`FlightID`, `ClassID`, `MaxSeats`, `BasePrice`) VALUES
(535, '2', 50, 200),
(535, '3', 150, 50),
(876, '2', 85, 250),
(876, '3', 100, 35),
(876, '1', 10, 300),
(652, '2', 10, 200),
(652, '3', 20, 50);

-- --------------------------------------------------------

--
-- Table structure for table `flightdep`
--

CREATE TABLE `flightdep` (
  `FlightID` smallint(6) NOT NULL,
  `DepDay` tinyint(4) NOT NULL,
  `DepTime` time NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `flightdep`
--

INSERT INTO `flightdep` (`FlightID`, `DepDay`, `DepTime`) VALUES
(345, 1, '21:30:00'),
(345, 2, '21:30:00'),
(345, 3, '21:30:00'),
(345, 4, '21:30:00'),
(345, 5, '21:30:00'),
(345, 6, '21:30:00'),
(345, 7, '21:30:00'),
(535, 2, '15:30:00'),
(535, 4, '15:30:00'),
(589, 6, '20:05:00'),
(589, 7, '20:05:00'),
(652, 1, '14:10:00'),
(652, 2, '14:10:00'),
(652, 3, '14:10:00'),
(652, 4, '14:10:00'),
(652, 5, '14:10:00'),
(662, 6, '17:45:00'),
(662, 7, '17:45:00'),
(663, 1, '09:10:00'),
(663, 2, '09:10:00'),
(663, 3, '09:10:00'),
(663, 4, '09:10:00'),
(663, 5, '09:10:00'),
(671, 1, '16:55:00'),
(671, 3, '16:55:00'),
(671, 5, '16:55:00'),
(672, 2, '16:55:00'),
(672, 4, '16:55:00'),
(672, 6, '16:55:00'),
(672, 7, '16:55:00'),
(674, 1, '14:25:00'),
(674, 2, '14:25:00'),
(674, 3, '14:25:00'),
(674, 4, '14:25:00'),
(675, 1, '07:30:00'),
(675, 3, '07:30:00'),
(675, 5, '07:30:00'),
(681, 1, '08:15:00'),
(685, 1, '21:45:00'),
(685, 2, '21:45:00'),
(685, 3, '21:45:00'),
(687, 2, '19:35:00'),
(687, 3, '19:35:00'),
(687, 4, '19:35:00'),
(688, 3, '13:45:00'),
(688, 4, '13:45:00'),
(688, 5, '13:45:00'),
(688, 6, '13:45:00'),
(689, 3, '19:00:00'),
(689, 4, '19:00:00'),
(689, 5, '19:00:00'),
(689, 6, '19:00:00'),
(702, 5, '09:30:00'),
(702, 6, '09:30:00'),
(702, 7, '09:30:00'),
(708, 5, '12:45:00'),
(708, 6, '12:45:00'),
(708, 7, '12:45:00'),
(724, 3, '23:30:00'),
(724, 7, '23:30:00'),
(725, 1, '17:30:00'),
(725, 4, '17:30:00'),
(765, 2, '01:45:00'),
(765, 4, '01:45:00'),
(765, 6, '01:45:00'),
(812, 1, '14:30:00'),
(812, 2, '14:30:00'),
(812, 3, '14:30:00'),
(812, 4, '14:30:00'),
(812, 5, '14:30:00'),
(826, 2, '13:45:00'),
(833, 3, '07:00:00'),
(857, 1, '19:30:00'),
(857, 2, '19:30:00'),
(857, 3, '19:30:00'),
(857, 4, '19:30:00'),
(857, 5, '19:30:00'),
(871, 1, '12:50:00'),
(871, 3, '12:50:00'),
(871, 5, '12:50:00'),
(872, 2, '12:50:00'),
(872, 4, '12:50:00'),
(872, 6, '12:50:00'),
(872, 7, '12:50:00'),
(876, 1, '07:10:00'),
(876, 2, '07:10:00'),
(876, 3, '07:10:00'),
(876, 4, '07:10:00'),
(876, 5, '07:10:00'),
(877, 1, '20:30:00'),
(877, 2, '20:30:00'),
(877, 3, '20:30:00'),
(877, 4, '20:30:00'),
(877, 5, '20:30:00'),
(896, 1, '00:30:00'),
(896, 2, '00:30:00'),
(896, 3, '00:30:00'),
(896, 6, '00:30:00'),
(896, 7, '00:30:00'),
(897, 1, '20:15:00'),
(897, 2, '20:15:00'),
(897, 3, '20:15:00'),
(897, 6, '20:15:00'),
(897, 7, '20:15:00'),
(898, 4, '00:10:00'),
(898, 5, '00:10:00'),
(899, 4, '21:15:00'),
(899, 5, '21:15:00');

-- --------------------------------------------------------

--
-- Table structure for table `pax`
--

CREATE TABLE `pax` (
  `RecordID` int(11) UNSIGNED NOT NULL,
  `FlightID` int(11) NOT NULL,
  `FlightDate` date NOT NULL,
  `ClassID` int(11) NOT NULL,
  `PaxName` varchar(255) NOT NULL,
  `PaxRef` varchar(255) DEFAULT NULL,
  `Note` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `pax`
--

INSERT INTO `pax` (`RecordID`, `FlightID`, `FlightDate`, `ClassID`, `PaxName`, `PaxRef`, `Note`) VALUES
(197, 652, '2019-06-22', 2, 'Henry Rabbit', 'TG75850303', ''),
(198, 652, '2019-06-22', 3, 'Harry Hippo', 'TG75847493', ''),
(199, 652, '2019-06-22', 3, 'Henrietta Hippo', 'TG75847493', '');

-- --------------------------------------------------------

--
-- Stand-in structure for view `rasporedletova`
--
CREATE TABLE `rasporedletova` (
`DepDay` tinyint(4)
,`FlightID` smallint(4) unsigned
,`RouteID` smallint(4) unsigned
,`AircraftID` smallint(4) unsigned
,`DepTime` time
);

-- --------------------------------------------------------

--
-- Table structure for table `route`
--

CREATE TABLE `route` (
  `RouteID` smallint(4) UNSIGNED NOT NULL,
  `FromAirport` smallint(4) UNSIGNED NOT NULL,
  `ToAirport` smallint(4) UNSIGNED NOT NULL,
  `Distance` smallint(4) UNSIGNED NOT NULL,
  `Duration` smallint(4) UNSIGNED NOT NULL,
  `Status` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `route`
--

INSERT INTO `route` (`RouteID`, `FromAirport`, `ToAirport`, `Distance`, `Duration`, `Status`) VALUES
(1003, 126, 56, 7200, 550, 1),
(1005, 34, 48, 343, 85, 1),
(1006, 165, 132, 974, 125, 1),
(1008, 34, 165, 686, 60, 1),
(1009, 34, 92, 489, 70, 1),
(1018, 34, 87, 1248, 135, 1),
(1023, 48, 59, 1434, 150, 1),
(1059, 165, 62, 978, 130, 1),
(1061, 48, 87, 1452, 155, 1),
(1071, 132, 72, 505, 65, 0),
(1097, 129, 165, 1134, 120, 1),
(1123, 92, 48, 777, 60, 1),
(1133, 74, 126, 6336, 470, 1),
(1139, 83, 87, 2474, 150, 1),
(1140, 87, 83, 2474, 150, 1),
(1141, 126, 201, 3913, 320, 1),
(1142, 201, 126, 3915, 320, 1),
(1165, 92, 59, 683, 50, 1),
(1167, 92, 56, 777, 70, 0),
(1169, 62, 92, 612, 120, 1),
(1173, 72, 62, 1237, 130, 1),
(1175, 132, 56, 1267, 150, 1),
(1176, 56, 132, 1267, 150, 1),
(1180, 201, 56, 10863, 815, 1),
(1190, 72, 165, 488, 80, 1),
(1191, 74, 83, 1966, 190, 1),
(1192, 92, 201, 10310, 760, 0),
(1193, 201, 92, 10310, 760, 1),
(1209, 56, 59, 1434, 150, 1);

-- --------------------------------------------------------

--
-- Table structure for table `stats`
--

CREATE TABLE `stats` (
  `FlightID` int(11) NOT NULL,
  `FlightDate` date NOT NULL,
  `ClassID` int(11) NOT NULL,
  `CurrSeats` int(11) NOT NULL,
  `CurrPrice` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `stats`
--

INSERT INTO `stats` (`FlightID`, `FlightDate`, `ClassID`, `CurrSeats`, `CurrPrice`) VALUES
(652, '2019-06-20', 2, 9, 200),
(652, '2019-06-20', 3, 17, 50),
(876, '2019-07-23', 1, 10, 300),
(876, '2019-06-30', 2, 85, 250),
(876, '2019-06-24', 3, 100, 35),
(876, '2019-07-18', 1, 3, 300),
(876, '2019-07-08', 2, 3, 250),
(876, '2019-03-08', 3, 3, 35);

-- --------------------------------------------------------

--
-- Structure for view `rasporedletova`
--
DROP TABLE IF EXISTS `rasporedletova`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `rasporedletova`  AS  select `flightdep`.`DepDay` AS `DepDay`,`flight`.`FlightID` AS `FlightID`,`flight`.`RouteID` AS `RouteID`,`flight`.`AircraftID` AS `AircraftID`,`flightdep`.`DepTime` AS `DepTime` from (`flight` join `flightdep` on((`flight`.`FlightID` = `flightdep`.`FlightID`))) order by `flightdep`.`DepDay`,`flightdep`.`DepTime` ;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `aircraft`
--
ALTER TABLE `aircraft`
  ADD PRIMARY KEY (`AircraftID`),
  ADD UNIQUE KEY `RegNum` (`RegNum`);

--
-- Indexes for table `aircrafttype`
--
ALTER TABLE `aircrafttype`
  ADD PRIMARY KEY (`AircraftTypeID`);

--
-- Indexes for table `airport`
--
ALTER TABLE `airport`
  ADD PRIMARY KEY (`AirportID`),
  ADD UNIQUE KEY `AirportCode_2` (`AirportCode`),
  ADD KEY `AirportCode` (`AirportCode`),
  ADD KEY `CountryCode` (`CountryCode`);

--
-- Indexes for table `class`
--
ALTER TABLE `class`
  ADD PRIMARY KEY (`ClassID`);

--
-- Indexes for table `flight`
--
ALTER TABLE `flight`
  ADD PRIMARY KEY (`FlightID`),
  ADD KEY `AircraftID` (`AircraftID`);

--
-- Indexes for table `flightclass`
--
ALTER TABLE `flightclass`
  ADD KEY `ClassID` (`ClassID`);

--
-- Indexes for table `flightdep`
--
ALTER TABLE `flightdep`
  ADD PRIMARY KEY (`FlightID`,`DepDay`,`DepTime`),
  ADD KEY `DepDay` (`DepDay`,`DepTime`);

--
-- Indexes for table `pax`
--
ALTER TABLE `pax`
  ADD PRIMARY KEY (`RecordID`),
  ADD KEY `ClassID` (`ClassID`);

--
-- Indexes for table `route`
--
ALTER TABLE `route`
  ADD PRIMARY KEY (`RouteID`),
  ADD KEY `Duration` (`Duration`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `aircraft`
--
ALTER TABLE `aircraft`
  MODIFY `AircraftID` smallint(4) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4566;
--
-- AUTO_INCREMENT for table `aircrafttype`
--
ALTER TABLE `aircrafttype`
  MODIFY `AircraftTypeID` smallint(4) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=620;
--
-- AUTO_INCREMENT for table `class`
--
ALTER TABLE `class`
  MODIFY `ClassID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
--
-- AUTO_INCREMENT for table `flight`
--
ALTER TABLE `flight`
  MODIFY `FlightID` smallint(4) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=900;
--
-- AUTO_INCREMENT for table `pax`
--
ALTER TABLE `pax`
  MODIFY `RecordID` int(11) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=200;
--
-- AUTO_INCREMENT for table `route`
--
ALTER TABLE `route`
  MODIFY `RouteID` smallint(4) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1210;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
