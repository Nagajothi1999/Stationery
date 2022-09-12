-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 23, 2022 at 05:28 AM
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
-- Database: `jeff`
--

-- --------------------------------------------------------

--
-- Table structure for table `addcustomer`
--

CREATE TABLE `addcustomer` (
  `id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `address` varchar(50) NOT NULL,
  `phone` int(11) NOT NULL,
  `purchase_amount` int(11) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(20) NOT NULL,
  `image` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `addcustomer`
--

INSERT INTO `addcustomer` (`id`, `name`, `address`, `phone`, `purchase_amount`, `username`, `password`, `image`) VALUES
(2, 'surya', 'venezula', 98989898, 35, 'surya111', '123', 'p5.jpg'),
(4, 'rahul', 'vellankanni', 2147483647, 1050, 'rahul333', '123', 'p2.jpg'),
(5, 'vaishnavi', 'kozhikood', 13211211, 0, 'vaish111', '123', 'p4.jpg'),
(8, 'joswa', 'vellayambalam', 898989087, 480, 'joswa123', '123', 'p6.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `addstaff`
--

CREATE TABLE `addstaff` (
  `staff_id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `address` varchar(50) NOT NULL,
  `dob` date NOT NULL,
  `phone` int(11) NOT NULL,
  `salary` int(11) NOT NULL,
  `status` int(11) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `image` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `addstaff`
--

INSERT INTO `addstaff` (`staff_id`, `name`, `address`, `dob`, `phone`, `salary`, `status`, `username`, `password`, `image`) VALUES
(1, 'antonson', 'vettukad', '2022-08-24', 2147483647, 30000, 1, 'abin123', '123', 'cat-1.jpg'),
(2, 'keerthi suresh', 'tamilnadu', '2004-06-22', 87689899, 25000, 0, 'keerthi96', '123', 'offer-1.png'),
(3, 'anoop', 'vellayambalam', '2022-08-24', 26132132, 20000, 1, 'anoop123', '123', 'p1.jpg'),
(6, 'krishna', 'marunthankuzhi', '2022-08-23', 12132131, 45000, 1, 'krishna222', '123', 'n3.jpg'),
(7, 'Revathy', 'vellarada', '1998-07-27', 2147483647, 30000, 1, 'rev123', '123', 'c1.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `addstock`
--

CREATE TABLE `addstock` (
  `id` int(11) NOT NULL,
  `cid` int(11) NOT NULL,
  `sub_id` int(11) NOT NULL,
  `company_id` int(11) NOT NULL,
  `qty` int(11) NOT NULL,
  `date` date NOT NULL,
  `purchase_amount` int(11) NOT NULL,
  `addby` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `addstock`
--

INSERT INTO `addstock` (`id`, `cid`, `sub_id`, `company_id`, `qty`, `date`, `purchase_amount`, `addby`) VALUES
(21, 28, 27, 5, 200, '2022-08-19', 9000, 'abin123'),
(22, 29, 30, 4, 25, '2022-08-21', 250, 'abin123'),
(23, 30, 31, 5, 50, '2022-08-21', 250, 'abin123'),
(24, 32, 32, 9, 100, '2022-08-21', 2500, 'abin123'),
(25, 34, 33, 11, 45, '2022-08-21', 2250, 'abin123'),
(26, 35, 34, 12, 30, '2022-08-21', 10500, 'abin123'),
(27, 29, 30, 4, 50, '2022-08-22', 500, 'abin123'),
(28, 30, 31, 5, 20, '2022-08-22', 100, 'abin123'),
(29, 34, 33, 11, 25, '2022-08-22', 1250, 'abin123');

-- --------------------------------------------------------

--
-- Table structure for table `bill`
--

CREATE TABLE `bill` (
  `bill_no` int(11) NOT NULL,
  `date` date NOT NULL,
  `cus_id` int(11) NOT NULL,
  `amount` int(11) NOT NULL,
  `status` int(11) NOT NULL,
  `addby` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `bill`
--

INSERT INTO `bill` (`bill_no`, `date`, `cus_id`, `amount`, `status`, `addby`) VALUES
(1068, '2022-08-21', 8, 480, 1, 'abin123'),
(1069, '2022-08-21', 4, 1050, 1, 'anoop123'),
(1070, '2022-08-21', 1, 120, 1, 'anoop123'),
(1071, '2022-08-22', 2, 35, 1, 'abin123');

-- --------------------------------------------------------

--
-- Table structure for table `category`
--

CREATE TABLE `category` (
  `cid` int(11) NOT NULL,
  `catname` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `category`
--

INSERT INTO `category` (`cid`, `catname`) VALUES
(29, 'pen'),
(30, 'pencil'),
(32, 'book'),
(34, 'geometry'),
(35, 'bag');

-- --------------------------------------------------------

--
-- Table structure for table `company`
--

CREATE TABLE `company` (
  `com_id` int(11) NOT NULL,
  `company` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `company`
--

INSERT INTO `company` (`com_id`, `company`) VALUES
(4, 'cello'),
(5, 'apsara'),
(9, 'classmate'),
(11, 'camlin'),
(12, 'kitex');

-- --------------------------------------------------------

--
-- Table structure for table `complaint`
--

CREATE TABLE `complaint` (
  `id` int(11) NOT NULL,
  `cus_id` int(11) NOT NULL,
  `date` date NOT NULL,
  `complaint` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `complaint`
--

INSERT INTO `complaint` (`id`, `cus_id`, `date`, `complaint`) VALUES
(2, 2, '2022-08-09', 'worst service\r\n');

-- --------------------------------------------------------

--
-- Table structure for table `data`
--

CREATE TABLE `data` (
  `id` int(11) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `type` varchar(50) NOT NULL,
  `status` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `data`
--

INSERT INTO `data` (`id`, `username`, `password`, `type`, `status`) VALUES
(1, 'admin', 'admin', 'admin', 1),
(2, 'abin123', '1243', 'staff', 1),
(3, 'keerthi96', '123', 'staff', 0),
(4, 'surya111', '123', 'user', 0),
(5, 'vj000', '123', 'user', 0),
(6, 'rahul333', '123', 'user', 0),
(7, 'anoop123', '123', 'staff', 1),
(8, 'anoop123', '123', 'staff', 1),
(9, 'anoop123', '123', 'staff', 1),
(10, 'krishna222', '123', 'staff', 1),
(11, 'vaish111', '123', 'user', 0),
(14, 'rev123', '123', 'staff', 1),
(15, 'rev123', '123', 'staff', 1),
(16, 'joswa123', '123', 'user', 0);

-- --------------------------------------------------------

--
-- Table structure for table `feedback`
--

CREATE TABLE `feedback` (
  `id` int(11) NOT NULL,
  `cus_id` int(11) NOT NULL,
  `date` date NOT NULL,
  `feedback` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `feedback`
--

INSERT INTO `feedback` (`id`, `cus_id`, `date`, `feedback`) VALUES
(2, 2, '2022-08-09', 'nice service\r\n'),
(3, 8, '2022-08-19', 'thank you');

-- --------------------------------------------------------

--
-- Table structure for table `leave_request`
--

CREATE TABLE `leave_request` (
  `id` int(11) NOT NULL,
  `staff_id` int(11) NOT NULL,
  `username` varchar(50) NOT NULL,
  `fromd` date NOT NULL,
  `tod` date NOT NULL,
  `days` int(11) NOT NULL,
  `reason` varchar(50) NOT NULL,
  `status` varchar(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `leave_request`
--

INSERT INTO `leave_request` (`id`, `staff_id`, `username`, `fromd`, `tod`, `days`, `reason`, `status`) VALUES
(4, 1, 'abin123', '2022-08-11', '2022-08-15', 4, 'marriage function', 'granted'),
(5, 1, 'abin123', '2022-08-01', '2022-08-08', 8, 'fever', 'granted'),
(6, 1, 'abin123', '2022-08-01', '2022-08-08', 8, 'fever', 'granted'),
(7, 1, 'abin123', '2022-08-13', '2022-08-14', 2, 'travel', 'granted'),
(8, 1, 'abin123', '2022-08-08', '2022-08-14', 7, 'headache', 'granted'),
(9, 2, 'keerthi96', '2022-08-17', '2022-08-21', 5, 'dhjsakhdjsakd', 'granted'),
(10, 1, 'abin123', '2022-08-08', '2022-08-17', 10, ',nd,nf,md', 'denied'),
(11, 1, 'abin123', '2022-08-15', '2022-08-19', 5, 'accident', 'granted'),
(12, 1, 'abin123', '2022-08-15', '2022-08-19', 5, 'accident', 'granted'),
(13, 1, 'abin123', '2022-08-01', '2022-08-19', 19, 'quit', 'granted'),
(14, 1, 'abin123', '2022-08-15', '2022-08-22', 8, 'marriage function', 'granted'),
(15, 2, 'keerthi96', '2022-08-15', '2022-08-23', 9, 'accident', 'denied'),
(16, 1, 'abin123', '2022-08-15', '2022-08-18', 4, 'health issues', 'granted');

-- --------------------------------------------------------

--
-- Table structure for table `log_status`
--

CREATE TABLE `log_status` (
  `id` int(11) NOT NULL,
  `username` varchar(50) NOT NULL,
  `date` varchar(50) NOT NULL,
  `login_time` varchar(50) NOT NULL,
  `log_out` time NOT NULL,
  `status` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `log_status`
--

INSERT INTO `log_status` (`id`, `username`, `date`, `login_time`, `log_out`, `status`) VALUES
(202, 'abin123', '2022-08-16', '15:08:32', '15:08:43', 1),
(203, 'abin123', '2022-08-17', '14:46:03', '14:49:23', 1),
(204, 'abin123', '2022-08-17', '14:50:06', '14:50:12', 1),
(205, 'abin123', '2022-08-17', '15:48:03', '15:51:36', 1),
(206, 'anoop123', '2022-08-19', '00:03:53', '00:03:56', 1),
(207, 'abin123', '2022-08-19', '08:45:40', '08:46:26', 1),
(208, 'abin123', '2022-08-19', '09:53:42', '09:54:34', 1),
(209, 'abin123', '2022-08-19', '11:02:05', '11:15:01', 1),
(210, 'rev123', '2022-08-20', '12:22:04', '12:22:06', 1),
(211, 'abin123', '2022-08-20', '12:22:50', '12:22:53', 1),
(212, 'abin123', '2022-08-20', '12:47:50', '12:48:44', 1),
(213, 'abin123', '2022-08-21', '13:38:07', '13:42:03', 1),
(214, 'abin123', '2022-08-21', '13:42:51', '13:45:05', 1),
(215, 'anoop123', '2022-08-21', '13:57:10', '13:58:08', 1),
(216, 'abin123', '2022-08-22', '11:31:47', '11:37:13', 1),
(217, 'abin123', '2022-08-22', '11:38:00', '11:50:52', 1),
(218, 'abin123', '2022-08-22', '11:53:29', '11:53:58', 1),
(219, 'abin123', '2022-08-22', '14:11:15', '14:14:10', 1),
(220, 'abin123', '2022-08-22', '14:36:38', '14:37:07', 1),
(221, 'anoop123', '2022-08-22', '14:42:52', '14:43:26', 1),
(222, 'anoop123', '2022-08-22', '14:44:26', '14:50:35', 1),
(223, 'anoop123', '2022-08-22', '15:34:12', '15:35:19', 1),
(224, 'anoop123', '2022-08-22', '15:44:06', '16:00:34', 1),
(225, 'anoop123', '2022-08-22', '16:01:54', '16:06:47', 1),
(226, 'abin123', '2022-08-22', '22:33:27', '22:36:48', 1),
(227, 'abin123', '2022-08-22', '22:36:16', '22:36:48', 1),
(228, 'abin123', '2022-08-22', '22:42:04', '23:19:29', 1),
(229, 'abin123', '2022-08-22', '23:05:27', '23:19:29', 1),
(230, 'abin123', '2022-08-22', '23:23:38', '23:24:25', 1);

-- --------------------------------------------------------

--
-- Table structure for table `password`
--

CREATE TABLE `password` (
  `id` int(11) NOT NULL,
  `cus_id` int(11) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `status` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `password`
--

INSERT INTO `password` (`id`, `cus_id`, `username`, `password`, `status`) VALUES
(4, 1, 'abin123', '1243', 1);

-- --------------------------------------------------------

--
-- Table structure for table `salary`
--

CREATE TABLE `salary` (
  `id` int(11) NOT NULL,
  `staff_id` int(11) NOT NULL,
  `date` date NOT NULL,
  `staff_name` varchar(50) NOT NULL,
  `message` varchar(50) NOT NULL,
  `month` varchar(10) NOT NULL,
  `amount` int(11) NOT NULL,
  `addby` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `salary`
--

INSERT INTO `salary` (`id`, `staff_id`, `date`, `staff_name`, `message`, `month`, `amount`, `addby`) VALUES
(16, 2, '2022-08-26', 'keerthi suresh', 'hello', '8', 25000, 'admin'),
(17, 1, '0000-00-00', 'antonson', '', 'None', 10000, 'ADMIN');

-- --------------------------------------------------------

--
-- Table structure for table `sale_table`
--

CREATE TABLE `sale_table` (
  `id` int(11) NOT NULL,
  `bill_no` int(11) NOT NULL,
  `date` date NOT NULL,
  `cat_id` int(11) NOT NULL,
  `sub_id` int(11) NOT NULL,
  `com_id` int(11) NOT NULL,
  `qty` int(11) NOT NULL,
  `amount` int(11) NOT NULL,
  `addby` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `sale_table`
--

INSERT INTO `sale_table` (`id`, `bill_no`, `date`, `cat_id`, `sub_id`, `com_id`, `qty`, `amount`, `addby`) VALUES
(68, 1068, '2022-08-21', 29, 30, 4, 3, 30, 'abin123'),
(69, 1068, '2022-08-21', 34, 33, 11, 2, 100, 'abin123'),
(70, 1068, '2022-08-21', 35, 34, 12, 1, 350, 'abin123'),
(71, 1069, '2022-08-21', 35, 34, 12, 3, 1050, 'anoop123'),
(72, 1070, '2022-08-21', 29, 30, 4, 12, 120, 'anoop123'),
(73, 1071, '2022-08-22', 29, 30, 4, 2, 20, 'abin123'),
(74, 1071, '2022-08-22', 30, 31, 5, 3, 15, 'abin123');

-- --------------------------------------------------------

--
-- Table structure for table `stock`
--

CREATE TABLE `stock` (
  `id` int(11) NOT NULL,
  `cid` int(11) NOT NULL,
  `sub_id` int(11) NOT NULL,
  `com_id` int(11) NOT NULL,
  `qty` int(11) NOT NULL,
  `amount` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `stock`
--

INSERT INTO `stock` (`id`, `cid`, `sub_id`, `com_id`, `qty`, `amount`) VALUES
(12, 29, 30, 4, 58, 10),
(13, 30, 31, 5, 67, 5),
(14, 32, 32, 9, 100, 25),
(15, 34, 33, 11, 68, 50),
(16, 35, 34, 12, 26, 350);

-- --------------------------------------------------------

--
-- Table structure for table `subcat`
--

CREATE TABLE `subcat` (
  `sub_id` int(11) NOT NULL,
  `cid` int(11) NOT NULL,
  `sub_cat` varchar(50) NOT NULL,
  `amount` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `subcat`
--

INSERT INTO `subcat` (`sub_id`, `cid`, `sub_cat`, `amount`) VALUES
(30, 29, 'blue ink pen', 10),
(31, 30, 'sharp drawning', 5),
(32, 32, 'college size', 25),
(33, 34, 'highschool', 50),
(34, 35, 'children school bag', 350);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `addcustomer`
--
ALTER TABLE `addcustomer`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `addstaff`
--
ALTER TABLE `addstaff`
  ADD PRIMARY KEY (`staff_id`);

--
-- Indexes for table `addstock`
--
ALTER TABLE `addstock`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `bill`
--
ALTER TABLE `bill`
  ADD PRIMARY KEY (`bill_no`);

--
-- Indexes for table `category`
--
ALTER TABLE `category`
  ADD PRIMARY KEY (`cid`);

--
-- Indexes for table `company`
--
ALTER TABLE `company`
  ADD PRIMARY KEY (`com_id`);

--
-- Indexes for table `complaint`
--
ALTER TABLE `complaint`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `data`
--
ALTER TABLE `data`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `feedback`
--
ALTER TABLE `feedback`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `leave_request`
--
ALTER TABLE `leave_request`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `log_status`
--
ALTER TABLE `log_status`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `password`
--
ALTER TABLE `password`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `salary`
--
ALTER TABLE `salary`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `sale_table`
--
ALTER TABLE `sale_table`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `stock`
--
ALTER TABLE `stock`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `subcat`
--
ALTER TABLE `subcat`
  ADD PRIMARY KEY (`sub_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `addcustomer`
--
ALTER TABLE `addcustomer`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `addstaff`
--
ALTER TABLE `addstaff`
  MODIFY `staff_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `addstock`
--
ALTER TABLE `addstock`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=30;

--
-- AUTO_INCREMENT for table `bill`
--
ALTER TABLE `bill`
  MODIFY `bill_no` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1073;

--
-- AUTO_INCREMENT for table `category`
--
ALTER TABLE `category`
  MODIFY `cid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=36;

--
-- AUTO_INCREMENT for table `company`
--
ALTER TABLE `company`
  MODIFY `com_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `complaint`
--
ALTER TABLE `complaint`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `data`
--
ALTER TABLE `data`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT for table `feedback`
--
ALTER TABLE `feedback`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `leave_request`
--
ALTER TABLE `leave_request`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT for table `log_status`
--
ALTER TABLE `log_status`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=231;

--
-- AUTO_INCREMENT for table `password`
--
ALTER TABLE `password`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `salary`
--
ALTER TABLE `salary`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT for table `sale_table`
--
ALTER TABLE `sale_table`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=75;

--
-- AUTO_INCREMENT for table `stock`
--
ALTER TABLE `stock`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT for table `subcat`
--
ALTER TABLE `subcat`
  MODIFY `sub_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=35;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
