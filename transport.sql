-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 20, 2022 at 08:42 PM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 8.1.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `transport`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `transport_air`
--

CREATE TABLE `transport_air` (
  `id` bigint(20) NOT NULL,
  `air_name` varchar(30) NOT NULL,
  `From` varchar(20) NOT NULL,
  `To` varchar(20) NOT NULL,
  `Class` varchar(20) NOT NULL,
  `nos` decimal(2,0) NOT NULL,
  `rem` decimal(2,0) NOT NULL,
  `price` decimal(6,2) NOT NULL,
  `date` date NOT NULL,
  `time` time(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `transport_air_book`
--

CREATE TABLE `transport_air_book` (
  `id` bigint(20) NOT NULL,
  `email` varchar(254) NOT NULL,
  `name` varchar(30) NOT NULL,
  `userid` decimal(2,0) NOT NULL,
  `airid` decimal(2,0) NOT NULL,
  `air_name` varchar(30) NOT NULL,
  `From` varchar(30) NOT NULL,
  `To` varchar(30) NOT NULL,
  `nos` decimal(2,0) NOT NULL,
  `price` decimal(6,2) NOT NULL,
  `date` date NOT NULL,
  `created` datetime(6) NOT NULL,
  `time` time(6) NOT NULL,
  `status` varchar(11) NOT NULL,
  `paymentstatus` varchar(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `transport_bike`
--

CREATE TABLE `transport_bike` (
  `id` bigint(20) NOT NULL,
  `email` varchar(254) NOT NULL,
  `name` varchar(30) NOT NULL,
  `userid` decimal(2,0) NOT NULL,
  `From` varchar(20) NOT NULL,
  `To` varchar(20) NOT NULL,
  `date` date NOT NULL,
  `time` time(6) NOT NULL,
  `price` decimal(6,2) NOT NULL,
  `status` varchar(11) NOT NULL,
  `paymentstatus` varchar(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `transport_bus`
--

CREATE TABLE `transport_bus` (
  `id` bigint(20) NOT NULL,
  `bus_name` varchar(30) NOT NULL,
  `From` varchar(20) NOT NULL,
  `To` varchar(20) NOT NULL,
  `Class` varchar(20) NOT NULL,
  `nos` decimal(2,0) NOT NULL,
  `rem` decimal(2,0) NOT NULL,
  `price` decimal(6,2) NOT NULL,
  `date` date NOT NULL,
  `time` time(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `transport_bus_book`
--

CREATE TABLE `transport_bus_book` (
  `id` bigint(20) NOT NULL,
  `email` varchar(254) NOT NULL,
  `name` varchar(30) NOT NULL,
  `userid` decimal(2,0) NOT NULL,
  `busid` decimal(2,0) NOT NULL,
  `bus_name` varchar(30) NOT NULL,
  `From` varchar(30) NOT NULL,
  `To` varchar(30) NOT NULL,
  `nos` decimal(2,0) NOT NULL,
  `price` decimal(6,2) NOT NULL,
  `date` date NOT NULL,
  `time` time(6) NOT NULL,
  `status` varchar(11) NOT NULL,
  `paymentstatus` varchar(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `transport_car`
--

CREATE TABLE `transport_car` (
  `id` bigint(20) NOT NULL,
  `email` varchar(254) NOT NULL,
  `name` varchar(30) NOT NULL,
  `userid` decimal(2,0) NOT NULL,
  `From` varchar(20) NOT NULL,
  `To` varchar(20) NOT NULL,
  `date` date NOT NULL,
  `time` time(6) NOT NULL,
  `price` decimal(6,2) NOT NULL,
  `status` varchar(11) NOT NULL,
  `paymentstatus` varchar(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `transport_cng`
--

CREATE TABLE `transport_cng` (
  `id` bigint(20) NOT NULL,
  `email` varchar(254) NOT NULL,
  `name` varchar(30) NOT NULL,
  `userid` decimal(2,0) NOT NULL,
  `From` varchar(20) NOT NULL,
  `To` varchar(20) NOT NULL,
  `date` date NOT NULL,
  `time` time(6) NOT NULL,
  `price` decimal(6,2) NOT NULL,
  `status` varchar(11) NOT NULL,
  `paymentstatus` varchar(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `transport_contact`
--

CREATE TABLE `transport_contact` (
  `id` bigint(20) NOT NULL,
  `name` varchar(122) NOT NULL,
  `phone` varchar(12) NOT NULL,
  `email` varchar(122) NOT NULL,
  `message` longtext NOT NULL,
  `date` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `transport_launch`
--

CREATE TABLE `transport_launch` (
  `id` bigint(20) NOT NULL,
  `launch_name` varchar(30) NOT NULL,
  `From` varchar(20) NOT NULL,
  `To` varchar(20) NOT NULL,
  `Class` varchar(20) NOT NULL,
  `nos` decimal(2,0) NOT NULL,
  `rem` decimal(2,0) NOT NULL,
  `price` decimal(6,2) NOT NULL,
  `date` date NOT NULL,
  `time` time(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `transport_launch_book`
--

CREATE TABLE `transport_launch_book` (
  `id` bigint(20) NOT NULL,
  `email` varchar(254) NOT NULL,
  `name` varchar(30) NOT NULL,
  `userid` decimal(2,0) NOT NULL,
  `launchid` decimal(2,0) NOT NULL,
  `launch_name` varchar(30) NOT NULL,
  `From` varchar(30) NOT NULL,
  `To` varchar(30) NOT NULL,
  `nos` decimal(2,0) NOT NULL,
  `price` decimal(6,2) NOT NULL,
  `date` date NOT NULL,
  `time` time(6) NOT NULL,
  `status` varchar(11) NOT NULL,
  `paymentstatus` varchar(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `transport_measurement`
--

CREATE TABLE `transport_measurement` (
  `id` bigint(20) NOT NULL,
  `location` varchar(200) NOT NULL,
  `destination` varchar(200) NOT NULL,
  `distance` decimal(10,2) NOT NULL,
  `created` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `transport_microbus`
--

CREATE TABLE `transport_microbus` (
  `id` bigint(20) NOT NULL,
  `email` varchar(254) NOT NULL,
  `name` varchar(30) NOT NULL,
  `userid` decimal(2,0) NOT NULL,
  `From` varchar(20) NOT NULL,
  `To` varchar(20) NOT NULL,
  `date` date NOT NULL,
  `time` time(6) NOT NULL,
  `price` decimal(6,2) NOT NULL,
  `status` varchar(11) NOT NULL,
  `paymentstatus` varchar(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `transport_pay`
--

CREATE TABLE `transport_pay` (
  `id` bigint(20) NOT NULL,
  `username` varchar(122) NOT NULL,
  `phone` varchar(12) NOT NULL,
  `transection` varchar(122) NOT NULL,
  `vehicle` varchar(12) NOT NULL,
  `pmethod` varchar(12) NOT NULL,
  `datesent` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `transport_resetpass`
--

CREATE TABLE `transport_resetpass` (
  `id` bigint(20) NOT NULL,
  `username` varchar(122) NOT NULL,
  `phone` varchar(12) NOT NULL,
  `email` varchar(122) NOT NULL,
  `history` varchar(12) NOT NULL,
  `dateused` date DEFAULT NULL,
  `created` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `transport_rider`
--

CREATE TABLE `transport_rider` (
  `id` bigint(20) NOT NULL,
  `name` varchar(200) DEFAULT NULL,
  `fname` varchar(200) DEFAULT NULL,
  `lname` varchar(200) DEFAULT NULL,
  `email` varchar(200) DEFAULT NULL,
  `phone` varchar(13) DEFAULT NULL,
  `address` varchar(200) DEFAULT NULL,
  `profile_pic` varchar(100) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `transport_train`
--

CREATE TABLE `transport_train` (
  `id` bigint(20) NOT NULL,
  `train_name` varchar(30) NOT NULL,
  `From` varchar(20) NOT NULL,
  `To` varchar(20) NOT NULL,
  `Class` varchar(20) NOT NULL,
  `nos` decimal(2,0) NOT NULL,
  `rem` decimal(2,0) NOT NULL,
  `price` decimal(6,2) NOT NULL,
  `date` date NOT NULL,
  `time` time(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `transport_train_book`
--

CREATE TABLE `transport_train_book` (
  `id` bigint(20) NOT NULL,
  `email` varchar(254) NOT NULL,
  `name` varchar(30) NOT NULL,
  `userid` decimal(2,0) NOT NULL,
  `trainid` decimal(2,0) NOT NULL,
  `train_name` varchar(30) NOT NULL,
  `From` varchar(30) NOT NULL,
  `To` varchar(30) NOT NULL,
  `nos` decimal(2,0) NOT NULL,
  `price` decimal(6,2) NOT NULL,
  `date` date NOT NULL,
  `time` time(6) NOT NULL,
  `status` varchar(11) NOT NULL,
  `paymentstatus` varchar(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `transport_air`
--
ALTER TABLE `transport_air`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `transport_air_book`
--
ALTER TABLE `transport_air_book`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `transport_bike`
--
ALTER TABLE `transport_bike`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `transport_bus`
--
ALTER TABLE `transport_bus`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `transport_bus_book`
--
ALTER TABLE `transport_bus_book`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `transport_car`
--
ALTER TABLE `transport_car`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `transport_cng`
--
ALTER TABLE `transport_cng`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `transport_contact`
--
ALTER TABLE `transport_contact`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `transport_launch`
--
ALTER TABLE `transport_launch`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `transport_launch_book`
--
ALTER TABLE `transport_launch_book`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `transport_measurement`
--
ALTER TABLE `transport_measurement`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `transport_microbus`
--
ALTER TABLE `transport_microbus`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `transport_pay`
--
ALTER TABLE `transport_pay`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `transport_resetpass`
--
ALTER TABLE `transport_resetpass`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `transport_rider`
--
ALTER TABLE `transport_rider`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `user_id` (`user_id`);

--
-- Indexes for table `transport_train`
--
ALTER TABLE `transport_train`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `transport_train_book`
--
ALTER TABLE `transport_train_book`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `transport_air`
--
ALTER TABLE `transport_air`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `transport_air_book`
--
ALTER TABLE `transport_air_book`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `transport_bike`
--
ALTER TABLE `transport_bike`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `transport_bus`
--
ALTER TABLE `transport_bus`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `transport_bus_book`
--
ALTER TABLE `transport_bus_book`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `transport_car`
--
ALTER TABLE `transport_car`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `transport_cng`
--
ALTER TABLE `transport_cng`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `transport_contact`
--
ALTER TABLE `transport_contact`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `transport_launch`
--
ALTER TABLE `transport_launch`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `transport_launch_book`
--
ALTER TABLE `transport_launch_book`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `transport_measurement`
--
ALTER TABLE `transport_measurement`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `transport_microbus`
--
ALTER TABLE `transport_microbus`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `transport_pay`
--
ALTER TABLE `transport_pay`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `transport_resetpass`
--
ALTER TABLE `transport_resetpass`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `transport_rider`
--
ALTER TABLE `transport_rider`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `transport_train`
--
ALTER TABLE `transport_train`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `transport_train_book`
--
ALTER TABLE `transport_train_book`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `transport_rider`
--
ALTER TABLE `transport_rider`
  ADD CONSTRAINT `transport_rider_user_id_d90b297c_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
