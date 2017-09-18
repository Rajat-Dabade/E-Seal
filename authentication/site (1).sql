-- phpMyAdmin SQL Dump
-- version 4.7.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Sep 04, 2017 at 09:05 AM
-- Server version: 10.1.25-MariaDB
-- PHP Version: 5.6.31

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `site`
--

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `username` varchar(20) NOT NULL,
  `first_name` varchar(50) DEFAULT NULL,
  `last_name` varchar(50) DEFAULT NULL,
  `password` varchar(256) NOT NULL,
  `active` tinyint(1) NOT NULL,
  `active_hash` varchar(255) DEFAULT NULL,
  `recover_hash` varchar(255) DEFAULT NULL,
  `remember_identifier` varchar(255) DEFAULT NULL,
  `remember_token` varchar(255) DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NULL DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `username`, `first_name`, `last_name`, `password`, `active`, `active_hash`, `recover_hash`, `remember_identifier`, `remember_token`, `created_at`, `updated_at`, `email`) VALUES
(1, 'rajat', 'Rajat', 'Dabade', '$2y$10$BIMMo86GZiFbBEIQ3CcoXeKIn8KS2QW9EHEEseVgEJKs7WvyQnxai', 1, NULL, NULL, NULL, NULL, '2017-08-28 14:10:41', '2017-08-29 15:18:10', 'rajatdabade1997@gmail.com'),
(2, 'aniketbaad', NULL, NULL, '$2y$10$sCEKMS8OaJiP.Fc3B5Yxe.xRKMrw8L9qBBRbj5RrfYVu3KCNFmlDS', 1, NULL, NULL, NULL, NULL, '2017-08-29 13:54:56', '2017-08-29 13:57:31', 'aniketbaad@gmail.com'),
(4, 'qwerty', NULL, NULL, '$2y$10$n.xZifM4ENtGgGjC8j15M.OrM9Bz31kL1/hmvZRSBZykf642w0Xim', 1, NULL, NULL, NULL, NULL, '2017-08-31 13:55:26', '2017-08-31 13:55:45', 'atharwaadawadkar448@gmail.com');

-- --------------------------------------------------------

--
-- Table structure for table `users_permissions`
--

CREATE TABLE `users_permissions` (
  `id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `is_admin` tinyint(1) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `users_permissions`
--

INSERT INTO `users_permissions` (`id`, `user_id`, `is_admin`, `created_at`, `updated_at`) VALUES
(1, 1, 1, '2017-08-28 14:10:41', '2017-08-28 14:10:41'),
(2, 2, 0, '2017-08-29 13:54:56', '2017-08-29 13:54:56'),
(3, 3, 0, '2017-08-31 13:48:58', '2017-08-31 13:48:58'),
(4, 4, 0, '2017-08-31 13:55:26', '2017-08-31 13:55:26');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `users_permissions`
--
ALTER TABLE `users_permissions`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
--
-- AUTO_INCREMENT for table `users_permissions`
--
ALTER TABLE `users_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
