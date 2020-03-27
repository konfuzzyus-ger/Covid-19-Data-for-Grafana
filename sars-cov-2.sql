-- phpMyAdmin SQL Dump
-- version 5.0.1
-- https://www.phpmyadmin.net/
--
-- Host: 10.150.1.49
-- Erstellungszeit: 27. Mrz 2020 um 01:30
-- Server-Version: 10.3.22-MariaDB-0+deb10u1
-- PHP-Version: 7.4.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Datenbank: `sars-cov-2`
--

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `2020_originalData`
--

CREATE TABLE `2020_originalData` (
  `id` int(11) NOT NULL,
  `datetime` date NOT NULL,
  `cases` int(11) NOT NULL,
  `country` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `2020_percentage1d`
--

CREATE TABLE `2020_percentage1d` (
  `id` int(11) NOT NULL,
  `date` date NOT NULL,
  `percentage` float NOT NULL,
  `country` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `2020_percentage3d`
--

CREATE TABLE `2020_percentage3d` (
  `id` int(11) NOT NULL,
  `date` date NOT NULL,
  `percentage` float NOT NULL,
  `country` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `2020_percentage5d`
--

CREATE TABLE `2020_percentage5d` (
  `id` int(11) NOT NULL,
  `date` date NOT NULL,
  `percentage` float NOT NULL,
  `country` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `2020_percentage7d`
--

CREATE TABLE `2020_percentage7d` (
  `id` int(11) NOT NULL,
  `date` date NOT NULL,
  `percentage` float NOT NULL,
  `country` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indizes der exportierten Tabellen
--

--
-- Indizes für die Tabelle `2020_originalData`
--
ALTER TABLE `2020_originalData`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `datetime-country-index` (`datetime`,`country`);

--
-- Indizes für die Tabelle `2020_percentage1d`
--
ALTER TABLE `2020_percentage1d`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `date-country.index` (`date`,`country`) USING BTREE;

--
-- Indizes für die Tabelle `2020_percentage3d`
--
ALTER TABLE `2020_percentage3d`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `date-country.index` (`date`,`country`) USING BTREE;

--
-- Indizes für die Tabelle `2020_percentage5d`
--
ALTER TABLE `2020_percentage5d`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `date-country.index` (`date`,`country`) USING BTREE;

--
-- Indizes für die Tabelle `2020_percentage7d`
--
ALTER TABLE `2020_percentage7d`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `date-country.index` (`date`,`country`) USING BTREE;

--
-- AUTO_INCREMENT für exportierte Tabellen
--

--
-- AUTO_INCREMENT für Tabelle `2020_originalData`
--
ALTER TABLE `2020_originalData`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT für Tabelle `2020_percentage1d`
--
ALTER TABLE `2020_percentage1d`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT für Tabelle `2020_percentage3d`
--
ALTER TABLE `2020_percentage3d`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT für Tabelle `2020_percentage5d`
--
ALTER TABLE `2020_percentage5d`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT für Tabelle `2020_percentage7d`
--
ALTER TABLE `2020_percentage7d`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
