-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 08, 2026 at 10:20 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `flask_project`
--

-- --------------------------------------------------------

--
-- Table structure for table `balloon_scores`
--

CREATE TABLE `balloon_scores` (
  `id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `score` int(11) DEFAULT NULL,
  `correct_words` int(11) DEFAULT NULL,
  `wrong_words` int(11) DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `balloon_scores`
--

INSERT INTO `balloon_scores` (`id`, `user_id`, `score`, `correct_words`, `wrong_words`, `created_at`) VALUES
(1, NULL, 5, 3, 5, '2026-09-27 12:57:11'),
(2, 6, -15, 1, 5, '2026-09-27 13:05:25'),
(3, 8, 35, 6, 5, '2026-09-27 19:07:14'),
(4, 8, 35, 6, 5, '2026-09-27 19:08:27'),
(5, 8, 35, 6, 5, '2026-09-27 19:14:20'),
(6, 9, 65, 9, 5, '2026-09-28 06:16:33'),
(7, 9, 45, 7, 5, '2026-09-28 06:48:52'),
(8, 10, 75, 10, 5, '2026-09-28 07:08:12'),
(9, 11, 75, 10, 5, '2026-09-28 07:22:13'),
(10, 12, 5, 3, 5, '2026-09-29 18:12:11'),
(11, 15, 35, 6, 5, '2026-10-08 07:16:26');

-- --------------------------------------------------------

--
-- Table structure for table `result`
--

CREATE TABLE `result` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `total_words` int(11) NOT NULL,
  `correct_words` int(11) NOT NULL,
  `wrong_words` int(11) NOT NULL,
  `wpm` decimal(10,2) NOT NULL,
  `accuracy` decimal(5,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `result`
--

INSERT INTO `result` (`id`, `user_id`, `total_words`, `correct_words`, `wrong_words`, `wpm`, `accuracy`) VALUES
(1, 2, 25, 22, 3, 22.00, 88.00),
(2, 2, 25, 22, 3, 22.00, 88.00),
(3, 2, 25, 18, 7, 18.00, 72.00),
(4, 2, 117, 42, 75, 42.00, 35.90),
(5, 1, 104, 18, 86, 18.00, 17.31),
(6, 4, 46, 5, 41, 5.00, 10.87),
(7, 5, 46, 20, 26, 20.00, 43.48),
(8, 5, 25, 0, 25, 0.00, 0.00),
(9, 8, 46, 6, 40, 6.00, 13.04),
(10, 8, 46, 0, 46, 0.00, 0.00),
(11, 8, 46, 0, 46, 0.00, 0.00),
(12, 9, 25, 22, 3, 22.00, 88.00),
(13, 9, 25, 0, 25, 0.00, 0.00),
(14, 9, 46, 5, 41, 5.00, 10.87),
(15, 10, 25, 10, 15, 10.00, 40.00),
(16, 11, 46, 18, 28, 18.00, 39.13),
(17, 12, 25, 13, 12, 13.00, 52.00),
(18, 12, 46, 8, 38, 8.00, 17.39),
(19, 15, 46, 4, 42, 4.00, 8.70);

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `email` varchar(150) NOT NULL,
  `password` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `name`, `email`, `password`) VALUES
(1, 'aaaaaaaaa', 'amee@gmail.com', '123456'),
(2, 'aayushi', 'aayu@gmail.com', '147852'),
(3, 'rose', 'rose23@gmail.com', '789456'),
(4, 'jacpson jayesh', 'jp@gmail.com', '784512'),
(5, 'mdsfsdf', 'm@gmail.com', '124421'),
(6, 'john', 'john2@gmail.com', '123456'),
(7, 'rosy', 'rosy2@gmail.com', '789456'),
(8, 'rosyyyy', 'rosy22@gmail.com', '456123'),
(9, 'test', 'test@gmail.com', '123456'),
(10, 'Reetu Tejvani', 'rt@gmail.com', 'RT'),
(11, 'Amee Buddh1', 'ameebuddh@gmail.com', '123456'),
(12, 'harvi 7 mi fail', 'harvi2@gmail.com', '123456'),
(13, 'bhumika', 'bhumi12@gmail.com', '1234'),
(14, 'bhumika', 'bhumi12@gmail.com', '1234'),
(15, 'mahek', 'mahek12@gmail.com', '1234');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `balloon_scores`
--
ALTER TABLE `balloon_scores`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `result`
--
ALTER TABLE `result`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `balloon_scores`
--
ALTER TABLE `balloon_scores`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `result`
--
ALTER TABLE `result`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `balloon_scores`
--
ALTER TABLE `balloon_scores`
  ADD CONSTRAINT `balloon_scores_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);

--
-- Constraints for table `result`
--
ALTER TABLE `result`
  ADD CONSTRAINT `result_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
