-- Adminer 4.8.0 MySQL 5.5.5-10.3.31-MariaDB-1:10.3.31+maria~bionic dump

SET NAMES utf8;
SET time_zone = '+00:00';
SET foreign_key_checks = 0;
SET sql_mode = 'NO_AUTO_VALUE_ON_ZERO';

DROP TABLE IF EXISTS `jadwal_devices`;
CREATE TABLE `jadwal_devices` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `device_id` int(11) DEFAULT NULL,
  `level` int(11) DEFAULT NULL,
  `waktu_pengiriman` time DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

INSERT INTO `jadwal_devices` (`id`, `device_id`, `level`, `waktu_pengiriman`, `created_at`, `updated_at`) VALUES
(637,	2,	1,	'00:00:00',	'2021-09-21 06:26:27',	'2021-09-21 06:26:27'),
(638,	2,	1,	'01:00:00',	'2021-09-21 06:26:27',	'2021-09-21 06:26:27'),
(639,	2,	1,	'02:00:00',	'2021-09-21 06:26:27',	'2021-09-21 06:26:27'),
(640,	2,	1,	'03:00:00',	'2021-09-21 06:26:27',	'2021-09-21 06:26:27'),
(641,	2,	1,	'04:00:00',	'2021-09-21 06:26:27',	'2021-09-21 06:26:27'),
(642,	2,	1,	'05:00:00',	'2021-09-21 06:26:27',	'2021-09-21 06:26:27'),
(643,	2,	1,	'06:00:00',	'2021-09-21 06:26:27',	'2021-09-21 06:26:27'),
(644,	2,	1,	'07:00:00',	'2021-09-21 06:26:27',	'2021-09-21 06:26:27'),
(645,	2,	1,	'08:00:00',	'2021-09-21 06:26:27',	'2021-09-21 06:26:27'),
(646,	2,	1,	'09:00:00',	'2021-09-21 06:26:27',	'2021-09-21 06:26:27'),
(647,	2,	1,	'10:00:00',	'2021-09-21 06:26:27',	'2021-09-21 06:26:27'),
(648,	2,	1,	'11:00:00',	'2021-09-21 06:26:27',	'2021-09-21 06:26:27'),
(649,	2,	1,	'12:00:00',	'2021-09-21 06:26:27',	'2021-09-21 06:26:27'),
(650,	2,	1,	'13:00:00',	'2021-09-21 06:26:27',	'2021-09-21 06:26:27'),
(651,	2,	1,	'14:00:00',	'2021-09-21 06:26:27',	'2021-09-21 06:26:27'),
(652,	2,	1,	'15:00:00',	'2021-09-21 06:26:27',	'2021-09-21 06:26:27'),
(653,	2,	1,	'16:00:00',	'2021-09-21 06:26:27',	'2021-09-21 06:26:27'),
(654,	2,	1,	'17:00:00',	'2021-09-21 06:26:27',	'2021-09-21 06:26:27'),
(655,	2,	1,	'18:00:00',	'2021-09-21 06:26:27',	'2021-09-21 06:26:27'),
(656,	2,	1,	'19:00:00',	'2021-09-21 06:26:27',	'2021-09-21 06:26:27'),
(657,	2,	1,	'20:00:00',	'2021-09-21 06:26:27',	'2021-09-21 06:26:27'),
(658,	2,	1,	'21:00:00',	'2021-09-21 06:26:27',	'2021-09-21 06:26:27'),
(659,	2,	1,	'22:00:00',	'2021-09-21 06:26:27',	'2021-09-21 06:26:27'),
(660,	2,	1,	'23:00:00',	'2021-09-21 06:26:27',	'2021-09-21 06:26:27'),
(661,	2,	2,	'00:00:00',	'2021-09-21 06:26:27',	'2021-09-21 06:26:27'),
(662,	2,	2,	'01:00:00',	'2021-09-21 06:26:27',	'2021-09-21 06:26:27'),
(663,	2,	2,	'02:00:00',	'2021-09-21 06:26:27',	'2021-09-21 06:26:27'),
(664,	2,	2,	'03:00:00',	'2021-09-21 06:26:27',	'2021-09-21 06:26:27'),
(665,	2,	2,	'04:00:00',	'2021-09-21 06:26:27',	'2021-09-21 06:26:27'),
(666,	2,	2,	'05:00:00',	'2021-09-21 06:26:27',	'2021-09-21 06:26:27'),
(667,	2,	2,	'06:00:00',	'2021-09-21 06:26:27',	'2021-09-21 06:26:27'),
(668,	2,	2,	'07:00:00',	'2021-09-21 06:26:27',	'2021-09-21 06:26:27'),
(669,	2,	2,	'08:00:00',	'2021-09-21 06:26:27',	'2021-09-21 06:26:27'),
(670,	2,	2,	'09:00:00',	'2021-09-21 06:26:27',	'2021-09-21 06:26:27'),
(671,	2,	2,	'10:00:00',	'2021-09-21 06:26:27',	'2021-09-21 06:26:27'),
(672,	2,	2,	'11:00:00',	'2021-09-21 06:26:27',	'2021-09-21 06:26:27'),
(673,	2,	2,	'12:00:00',	'2021-09-21 06:26:27',	'2021-09-21 06:26:27'),
(674,	2,	2,	'13:00:00',	'2021-09-21 06:26:27',	'2021-09-21 06:26:27'),
(675,	2,	2,	'14:00:00',	'2021-09-21 06:26:27',	'2021-09-21 06:26:27'),
(676,	2,	2,	'15:00:00',	'2021-09-21 06:26:27',	'2021-09-21 06:26:27'),
(677,	2,	2,	'16:00:00',	'2021-09-21 06:26:27',	'2021-09-21 06:26:27'),
(678,	2,	2,	'17:00:00',	'2021-09-21 06:26:27',	'2021-09-21 06:26:27'),
(679,	2,	2,	'18:00:00',	'2021-09-21 06:26:27',	'2021-09-21 06:26:27'),
(680,	2,	2,	'19:00:00',	'2021-09-21 06:26:27',	'2021-09-21 06:26:27'),
(681,	2,	2,	'20:00:00',	'2021-09-21 06:26:27',	'2021-09-21 06:26:27'),
(682,	2,	2,	'21:00:00',	'2021-09-21 06:26:27',	'2021-09-21 06:26:27'),
(683,	2,	2,	'22:00:00',	'2021-09-21 06:26:27',	'2021-09-21 06:26:27'),
(684,	2,	2,	'23:00:00',	'2021-09-21 06:26:27',	'2021-09-21 06:26:27'),
(685,	2,	3,	'00:00:00',	'2021-09-21 06:26:27',	'2021-09-21 06:26:27'),
(686,	2,	3,	'01:00:00',	'2021-09-21 06:26:27',	'2021-09-21 06:26:27'),
(687,	2,	3,	'02:00:00',	'2021-09-21 06:26:27',	'2021-09-21 06:26:27'),
(688,	2,	3,	'03:00:00',	'2021-09-21 06:26:27',	'2021-09-21 06:26:27'),
(689,	2,	3,	'04:00:00',	'2021-09-21 06:26:27',	'2021-09-21 06:26:27'),
(690,	2,	3,	'05:00:00',	'2021-09-21 06:26:27',	'2021-09-21 06:26:27'),
(691,	2,	3,	'06:00:00',	'2021-09-21 06:26:27',	'2021-09-21 06:26:27'),
(692,	2,	3,	'07:00:00',	'2021-09-21 06:26:27',	'2021-09-21 06:26:27'),
(693,	2,	3,	'08:00:00',	'2021-09-21 06:26:27',	'2021-09-21 06:26:27'),
(694,	2,	3,	'09:00:00',	'2021-09-21 06:26:27',	'2021-09-21 06:26:27'),
(695,	2,	3,	'10:00:00',	'2021-09-21 06:26:27',	'2021-09-21 06:26:27'),
(696,	2,	3,	'11:00:00',	'2021-09-21 06:26:27',	'2021-09-21 06:26:27'),
(697,	2,	3,	'12:00:00',	'2021-09-21 06:26:27',	'2021-09-21 06:26:27'),
(698,	2,	3,	'13:00:00',	'2021-09-21 06:26:27',	'2021-09-21 06:26:27'),
(699,	2,	3,	'14:00:00',	'2021-09-21 06:26:27',	'2021-09-21 06:26:27'),
(700,	2,	3,	'15:00:00',	'2021-09-21 06:26:27',	'2021-09-21 06:26:27'),
(701,	2,	3,	'16:00:00',	'2021-09-21 06:26:27',	'2021-09-21 06:26:27'),
(702,	2,	3,	'17:00:00',	'2021-09-21 06:26:27',	'2021-09-21 06:26:27'),
(703,	2,	3,	'18:00:00',	'2021-09-21 06:26:27',	'2021-09-21 06:26:27'),
(704,	2,	3,	'19:00:00',	'2021-09-21 06:26:27',	'2021-09-21 06:26:27'),
(705,	2,	3,	'20:00:00',	'2021-09-21 06:26:27',	'2021-09-21 06:26:27'),
(706,	2,	3,	'21:00:00',	'2021-09-21 06:26:27',	'2021-09-21 06:26:27'),
(707,	2,	3,	'22:00:00',	'2021-09-21 06:26:27',	'2021-09-21 06:26:27'),
(708,	2,	3,	'23:00:00',	'2021-09-21 06:26:27',	'2021-09-21 06:26:27'),
(709,	2,	4,	'00:00:00',	'2021-09-21 06:26:27',	'2021-09-21 06:26:27'),
(710,	2,	4,	'06:00:00',	'2021-09-21 06:26:27',	'2021-09-21 06:26:27'),
(711,	2,	4,	'12:00:00',	'2021-09-21 06:26:27',	'2021-09-21 06:26:27'),
(712,	2,	4,	'18:00:00',	'2021-09-21 06:26:27',	'2021-09-21 06:26:27'),
(4625,	1,	1,	'00:00:00',	'2021-10-29 02:50:38',	'2021-10-29 02:50:38'),
(4626,	1,	1,	'00:15:00',	'2021-10-29 02:50:38',	'2021-10-29 02:50:38'),
(4627,	1,	1,	'00:30:00',	'2021-10-29 02:50:38',	'2021-10-29 02:50:38'),
(4628,	1,	1,	'00:45:00',	'2021-10-29 02:50:38',	'2021-10-29 02:50:38'),
(4629,	1,	1,	'01:00:00',	'2021-10-29 02:50:38',	'2021-10-29 02:50:38'),
(4630,	1,	1,	'01:15:00',	'2021-10-29 02:50:38',	'2021-10-29 02:50:38'),
(4631,	1,	1,	'01:30:00',	'2021-10-29 02:50:38',	'2021-10-29 02:50:38'),
(4632,	1,	1,	'01:45:00',	'2021-10-29 02:50:38',	'2021-10-29 02:50:38'),
(4633,	1,	1,	'02:00:00',	'2021-10-29 02:50:38',	'2021-10-29 02:50:38'),
(4634,	1,	1,	'02:15:00',	'2021-10-29 02:50:38',	'2021-10-29 02:50:38'),
(4635,	1,	1,	'02:30:00',	'2021-10-29 02:50:38',	'2021-10-29 02:50:38'),
(4636,	1,	1,	'02:45:00',	'2021-10-29 02:50:38',	'2021-10-29 02:50:38'),
(4637,	1,	1,	'03:00:00',	'2021-10-29 02:50:38',	'2021-10-29 02:50:38'),
(4638,	1,	1,	'03:15:00',	'2021-10-29 02:50:38',	'2021-10-29 02:50:38'),
(4639,	1,	1,	'03:30:00',	'2021-10-29 02:50:38',	'2021-10-29 02:50:38'),
(4640,	1,	1,	'03:45:00',	'2021-10-29 02:50:38',	'2021-10-29 02:50:38'),
(4641,	1,	1,	'04:00:00',	'2021-10-29 02:50:38',	'2021-10-29 02:50:38'),
(4642,	1,	1,	'04:15:00',	'2021-10-29 02:50:38',	'2021-10-29 02:50:38'),
(4643,	1,	1,	'04:30:00',	'2021-10-29 02:50:38',	'2021-10-29 02:50:38'),
(4644,	1,	1,	'04:45:00',	'2021-10-29 02:50:38',	'2021-10-29 02:50:38'),
(4645,	1,	1,	'05:00:00',	'2021-10-29 02:50:38',	'2021-10-29 02:50:38'),
(4646,	1,	1,	'05:15:00',	'2021-10-29 02:50:38',	'2021-10-29 02:50:38'),
(4647,	1,	1,	'05:30:00',	'2021-10-29 02:50:38',	'2021-10-29 02:50:38'),
(4648,	1,	1,	'05:45:00',	'2021-10-29 02:50:38',	'2021-10-29 02:50:38'),
(4649,	1,	1,	'06:00:00',	'2021-10-29 02:50:38',	'2021-10-29 02:50:38'),
(4650,	1,	1,	'06:15:00',	'2021-10-29 02:50:38',	'2021-10-29 02:50:38'),
(4651,	1,	1,	'06:30:00',	'2021-10-29 02:50:38',	'2021-10-29 02:50:38'),
(4652,	1,	1,	'06:45:00',	'2021-10-29 02:50:38',	'2021-10-29 02:50:38'),
(4653,	1,	1,	'07:00:00',	'2021-10-29 02:50:38',	'2021-10-29 02:50:38'),
(4654,	1,	1,	'07:15:00',	'2021-10-29 02:50:38',	'2021-10-29 02:50:38'),
(4655,	1,	1,	'07:30:00',	'2021-10-29 02:50:38',	'2021-10-29 02:50:38'),
(4656,	1,	1,	'07:45:00',	'2021-10-29 02:50:38',	'2021-10-29 02:50:38'),
(4657,	1,	1,	'08:00:00',	'2021-10-29 02:50:38',	'2021-10-29 02:50:38'),
(4658,	1,	1,	'08:15:00',	'2021-10-29 02:50:38',	'2021-10-29 02:50:38'),
(4659,	1,	1,	'08:30:00',	'2021-10-29 02:50:38',	'2021-10-29 02:50:38'),
(4660,	1,	1,	'08:45:00',	'2021-10-29 02:50:38',	'2021-10-29 02:50:38'),
(4661,	1,	1,	'09:00:00',	'2021-10-29 02:50:38',	'2021-10-29 02:50:38'),
(4662,	1,	1,	'09:30:00',	'2021-10-29 02:50:38',	'2021-10-29 02:50:38'),
(4663,	1,	1,	'09:45:00',	'2021-10-29 02:50:38',	'2021-10-29 02:50:38'),
(4664,	1,	1,	'10:00:00',	'2021-10-29 02:50:38',	'2021-10-29 02:50:38'),
(4665,	1,	1,	'20:00:00',	'2021-10-29 02:50:38',	'2021-10-29 02:50:38'),
(4666,	1,	1,	'20:30:00',	'2021-10-29 02:50:38',	'2021-10-29 02:50:38'),
(4667,	1,	1,	'21:00:00',	'2021-10-29 02:50:38',	'2021-10-29 02:50:38'),
(4668,	1,	1,	'21:30:00',	'2021-10-29 02:50:38',	'2021-10-29 02:50:38'),
(4669,	1,	1,	'22:00:00',	'2021-10-29 02:50:38',	'2021-10-29 02:50:38'),
(4670,	1,	1,	'22:30:00',	'2021-10-29 02:50:38',	'2021-10-29 02:50:38'),
(4671,	1,	1,	'23:00:00',	'2021-10-29 02:50:38',	'2021-10-29 02:50:38'),
(4672,	1,	1,	'23:30:00',	'2021-10-29 02:50:38',	'2021-10-29 02:50:38'),
(4673,	1,	2,	'00:30:00',	'2021-10-29 02:50:38',	'2021-10-29 02:50:38'),
(4674,	1,	2,	'01:00:00',	'2021-10-29 02:50:38',	'2021-10-29 02:50:38'),
(4675,	1,	2,	'01:30:00',	'2021-10-29 02:50:38',	'2021-10-29 02:50:38'),
(4676,	1,	2,	'02:00:00',	'2021-10-29 02:50:38',	'2021-10-29 02:50:38'),
(4677,	1,	2,	'02:30:00',	'2021-10-29 02:50:38',	'2021-10-29 02:50:38'),
(4678,	1,	2,	'03:00:00',	'2021-10-29 02:50:38',	'2021-10-29 02:50:38'),
(4679,	1,	2,	'03:30:00',	'2021-10-29 02:50:38',	'2021-10-29 02:50:38'),
(4680,	1,	2,	'04:00:00',	'2021-10-29 02:50:38',	'2021-10-29 02:50:38'),
(4681,	1,	2,	'04:30:00',	'2021-10-29 02:50:38',	'2021-10-29 02:50:38'),
(4682,	1,	2,	'05:00:00',	'2021-10-29 02:50:38',	'2021-10-29 02:50:38'),
(4683,	1,	2,	'05:30:00',	'2021-10-29 02:50:38',	'2021-10-29 02:50:38'),
(4684,	1,	2,	'06:00:00',	'2021-10-29 02:50:38',	'2021-10-29 02:50:38'),
(4685,	1,	2,	'06:30:00',	'2021-10-29 02:50:38',	'2021-10-29 02:50:38'),
(4686,	1,	2,	'07:00:00',	'2021-10-29 02:50:38',	'2021-10-29 02:50:38'),
(4687,	1,	2,	'07:30:00',	'2021-10-29 02:50:38',	'2021-10-29 02:50:38'),
(4688,	1,	2,	'08:00:00',	'2021-10-29 02:50:38',	'2021-10-29 02:50:38'),
(4689,	1,	2,	'08:30:00',	'2021-10-29 02:50:38',	'2021-10-29 02:50:38'),
(4690,	1,	2,	'09:00:00',	'2021-10-29 02:50:38',	'2021-10-29 02:50:38'),
(4691,	1,	2,	'09:30:00',	'2021-10-29 02:50:38',	'2021-10-29 02:50:38'),
(4692,	1,	2,	'10:00:00',	'2021-10-29 02:50:38',	'2021-10-29 02:50:38'),
(4693,	1,	2,	'10:30:00',	'2021-10-29 02:50:38',	'2021-10-29 02:50:38'),
(4694,	1,	2,	'11:00:00',	'2021-10-29 02:50:38',	'2021-10-29 02:50:38'),
(4695,	1,	2,	'11:30:00',	'2021-10-29 02:50:38',	'2021-10-29 02:50:38'),
(4696,	1,	2,	'12:00:00',	'2021-10-29 02:50:38',	'2021-10-29 02:50:38'),
(4697,	1,	2,	'12:30:00',	'2021-10-29 02:50:38',	'2021-10-29 02:50:38'),
(4698,	1,	2,	'13:00:00',	'2021-10-29 02:50:38',	'2021-10-29 02:50:38'),
(4699,	1,	2,	'13:30:00',	'2021-10-29 02:50:38',	'2021-10-29 02:50:38'),
(4700,	1,	2,	'14:00:00',	'2021-10-29 02:50:38',	'2021-10-29 02:50:38'),
(4701,	1,	2,	'14:30:00',	'2021-10-29 02:50:38',	'2021-10-29 02:50:38'),
(4702,	1,	2,	'15:00:00',	'2021-10-29 02:50:38',	'2021-10-29 02:50:38'),
(4703,	1,	2,	'15:30:00',	'2021-10-29 02:50:38',	'2021-10-29 02:50:38'),
(4704,	1,	2,	'16:00:00',	'2021-10-29 02:50:38',	'2021-10-29 02:50:38'),
(4705,	1,	2,	'16:30:00',	'2021-10-29 02:50:38',	'2021-10-29 02:50:38'),
(4706,	1,	2,	'17:00:00',	'2021-10-29 02:50:38',	'2021-10-29 02:50:38'),
(4707,	1,	2,	'17:30:00',	'2021-10-29 02:50:38',	'2021-10-29 02:50:38'),
(4708,	1,	2,	'18:00:00',	'2021-10-29 02:50:38',	'2021-10-29 02:50:38'),
(4709,	1,	2,	'18:30:00',	'2021-10-29 02:50:38',	'2021-10-29 02:50:38'),
(4710,	1,	2,	'19:00:00',	'2021-10-29 02:50:38',	'2021-10-29 02:50:38'),
(4711,	1,	2,	'19:30:00',	'2021-10-29 02:50:38',	'2021-10-29 02:50:38'),
(4712,	1,	2,	'20:00:00',	'2021-10-29 02:50:38',	'2021-10-29 02:50:38'),
(4713,	1,	2,	'20:30:00',	'2021-10-29 02:50:38',	'2021-10-29 02:50:38'),
(4714,	1,	2,	'21:00:00',	'2021-10-29 02:50:38',	'2021-10-29 02:50:38'),
(4715,	1,	2,	'21:30:00',	'2021-10-29 02:50:38',	'2021-10-29 02:50:38'),
(4716,	1,	2,	'22:00:00',	'2021-10-29 02:50:38',	'2021-10-29 02:50:38'),
(4717,	1,	2,	'22:30:00',	'2021-10-29 02:50:38',	'2021-10-29 02:50:38'),
(4718,	1,	2,	'23:00:00',	'2021-10-29 02:50:38',	'2021-10-29 02:50:38'),
(4719,	1,	2,	'23:30:00',	'2021-10-29 02:50:38',	'2021-10-29 02:50:38'),
(4720,	1,	2,	'00:00:00',	'2021-10-29 02:50:38',	'2021-10-29 02:50:38'),
(4721,	1,	3,	'01:00:00',	'2021-10-29 02:50:38',	'2021-10-29 02:50:38'),
(4722,	1,	3,	'02:00:00',	'2021-10-29 02:50:38',	'2021-10-29 02:50:38'),
(4723,	1,	3,	'03:00:00',	'2021-10-29 02:50:38',	'2021-10-29 02:50:38'),
(4724,	1,	3,	'04:00:00',	'2021-10-29 02:50:38',	'2021-10-29 02:50:38'),
(4725,	1,	3,	'05:00:00',	'2021-10-29 02:50:38',	'2021-10-29 02:50:38'),
(4726,	1,	3,	'06:00:00',	'2021-10-29 02:50:38',	'2021-10-29 02:50:38'),
(4727,	1,	3,	'07:00:00',	'2021-10-29 02:50:38',	'2021-10-29 02:50:38'),
(4728,	1,	3,	'08:00:00',	'2021-10-29 02:50:38',	'2021-10-29 02:50:38'),
(4729,	1,	3,	'09:00:00',	'2021-10-29 02:50:38',	'2021-10-29 02:50:38'),
(4730,	1,	3,	'10:00:00',	'2021-10-29 02:50:38',	'2021-10-29 02:50:38'),
(4731,	1,	3,	'11:00:00',	'2021-10-29 02:50:38',	'2021-10-29 02:50:38'),
(4732,	1,	3,	'12:00:00',	'2021-10-29 02:50:38',	'2021-10-29 02:50:38'),
(4733,	1,	3,	'13:00:00',	'2021-10-29 02:50:38',	'2021-10-29 02:50:38'),
(4734,	1,	3,	'14:00:00',	'2021-10-29 02:50:38',	'2021-10-29 02:50:38'),
(4735,	1,	3,	'15:00:00',	'2021-10-29 02:50:38',	'2021-10-29 02:50:38'),
(4736,	1,	3,	'16:00:00',	'2021-10-29 02:50:38',	'2021-10-29 02:50:38'),
(4737,	1,	3,	'17:00:00',	'2021-10-29 02:50:38',	'2021-10-29 02:50:38'),
(4738,	1,	3,	'18:00:00',	'2021-10-29 02:50:38',	'2021-10-29 02:50:38'),
(4739,	1,	3,	'19:00:00',	'2021-10-29 02:50:38',	'2021-10-29 02:50:38'),
(4740,	1,	3,	'20:00:00',	'2021-10-29 02:50:38',	'2021-10-29 02:50:38'),
(4741,	1,	3,	'21:00:00',	'2021-10-29 02:50:38',	'2021-10-29 02:50:38'),
(4742,	1,	3,	'22:00:00',	'2021-10-29 02:50:38',	'2021-10-29 02:50:38'),
(4743,	1,	3,	'23:00:00',	'2021-10-29 02:50:38',	'2021-10-29 02:50:38'),
(4744,	1,	3,	'00:00:00',	'2021-10-29 02:50:38',	'2021-10-29 02:50:38'),
(4745,	1,	4,	'03:00:00',	'2021-10-29 02:50:38',	'2021-10-29 02:50:38'),
(4746,	1,	4,	'06:00:00',	'2021-10-29 02:50:38',	'2021-10-29 02:50:38'),
(4747,	1,	4,	'09:00:00',	'2021-10-29 02:50:38',	'2021-10-29 02:50:38'),
(4748,	1,	4,	'12:00:00',	'2021-10-29 02:50:38',	'2021-10-29 02:50:38'),
(4749,	1,	4,	'15:00:00',	'2021-10-29 02:50:38',	'2021-10-29 02:50:38'),
(4750,	1,	4,	'18:00:00',	'2021-10-29 02:50:38',	'2021-10-29 02:50:38'),
(4751,	1,	4,	'21:00:00',	'2021-10-29 02:50:38',	'2021-10-29 02:50:38'),
(4752,	1,	4,	'00:00:00',	'2021-10-29 02:50:38',	'2021-10-29 02:50:38'),
(4753,	3,	1,	'00:15:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4754,	3,	1,	'00:30:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4755,	3,	1,	'00:45:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4756,	3,	1,	'01:00:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4757,	3,	1,	'01:15:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4758,	3,	1,	'01:30:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4759,	3,	1,	'01:45:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4760,	3,	1,	'02:00:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4761,	3,	1,	'02:15:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4762,	3,	1,	'02:30:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4763,	3,	1,	'02:45:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4764,	3,	1,	'03:00:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4765,	3,	1,	'03:15:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4766,	3,	1,	'03:30:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4767,	3,	1,	'03:45:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4768,	3,	1,	'04:00:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4769,	3,	1,	'04:15:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4770,	3,	1,	'04:30:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4771,	3,	1,	'04:45:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4772,	3,	1,	'05:00:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4773,	3,	1,	'05:15:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4774,	3,	1,	'05:30:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4775,	3,	1,	'05:45:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4776,	3,	1,	'06:00:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4777,	3,	1,	'06:15:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4778,	3,	1,	'06:30:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4779,	3,	1,	'06:45:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4780,	3,	1,	'07:00:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4781,	3,	1,	'07:15:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4782,	3,	1,	'07:30:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4783,	3,	1,	'07:45:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4784,	3,	1,	'08:00:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4785,	3,	1,	'08:15:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4786,	3,	1,	'08:30:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4787,	3,	1,	'08:45:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4788,	3,	1,	'09:00:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4789,	3,	1,	'09:15:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4790,	3,	1,	'09:30:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4791,	3,	1,	'09:45:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4792,	3,	1,	'10:00:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4793,	3,	1,	'10:15:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4794,	3,	1,	'10:30:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4795,	3,	1,	'10:45:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4796,	3,	1,	'11:00:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4797,	3,	1,	'11:15:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4798,	3,	1,	'11:30:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4799,	3,	1,	'11:45:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4800,	3,	1,	'12:00:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4801,	3,	1,	'12:15:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4802,	3,	1,	'12:30:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4803,	3,	1,	'12:45:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4804,	3,	1,	'13:00:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4805,	3,	1,	'13:15:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4806,	3,	1,	'13:30:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4807,	3,	1,	'13:45:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4808,	3,	1,	'14:00:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4809,	3,	1,	'14:15:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4810,	3,	1,	'14:30:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4811,	3,	1,	'14:45:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4812,	3,	1,	'15:00:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4813,	3,	1,	'15:15:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4814,	3,	1,	'15:30:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4815,	3,	1,	'15:45:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4816,	3,	1,	'16:00:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4817,	3,	1,	'16:15:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4818,	3,	1,	'16:30:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4819,	3,	1,	'16:45:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4820,	3,	1,	'17:00:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4821,	3,	1,	'17:15:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4822,	3,	1,	'17:30:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4823,	3,	1,	'17:45:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4824,	3,	1,	'18:00:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4825,	3,	1,	'18:15:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4826,	3,	1,	'18:30:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4827,	3,	1,	'18:45:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4828,	3,	1,	'19:00:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4829,	3,	1,	'19:15:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4830,	3,	1,	'19:30:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4831,	3,	1,	'19:45:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4832,	3,	1,	'20:00:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4833,	3,	1,	'20:15:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4834,	3,	1,	'20:30:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4835,	3,	1,	'20:45:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4836,	3,	1,	'21:00:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4837,	3,	1,	'21:15:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4838,	3,	1,	'21:30:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4839,	3,	1,	'21:45:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4840,	3,	1,	'22:00:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4841,	3,	1,	'22:15:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4842,	3,	1,	'22:30:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4843,	3,	1,	'22:45:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4844,	3,	1,	'23:00:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4845,	3,	1,	'23:15:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4846,	3,	1,	'23:30:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4847,	3,	1,	'23:45:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4848,	3,	1,	'00:00:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4849,	3,	2,	'00:30:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4850,	3,	2,	'01:00:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4851,	3,	2,	'01:30:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4852,	3,	2,	'02:00:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4853,	3,	2,	'02:30:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4854,	3,	2,	'03:00:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4855,	3,	2,	'03:30:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4856,	3,	2,	'04:00:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4857,	3,	2,	'04:30:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4858,	3,	2,	'05:00:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4859,	3,	2,	'05:30:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4860,	3,	2,	'06:00:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4861,	3,	2,	'06:30:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4862,	3,	2,	'07:00:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4863,	3,	2,	'07:30:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4864,	3,	2,	'08:00:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4865,	3,	2,	'08:30:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4866,	3,	2,	'09:00:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4867,	3,	2,	'09:30:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4868,	3,	2,	'10:00:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4869,	3,	2,	'10:30:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4870,	3,	2,	'11:00:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4871,	3,	2,	'11:30:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4872,	3,	2,	'12:00:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4873,	3,	2,	'12:30:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4874,	3,	2,	'13:00:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4875,	3,	2,	'13:30:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4876,	3,	2,	'14:00:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4877,	3,	2,	'14:30:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4878,	3,	2,	'15:00:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4879,	3,	2,	'15:30:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4880,	3,	2,	'16:00:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4881,	3,	2,	'16:30:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4882,	3,	2,	'17:00:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4883,	3,	2,	'17:30:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4884,	3,	2,	'18:00:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4885,	3,	2,	'18:30:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4886,	3,	2,	'19:00:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4887,	3,	2,	'19:30:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4888,	3,	2,	'20:00:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4889,	3,	2,	'20:30:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4890,	3,	2,	'21:00:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4891,	3,	2,	'21:30:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4892,	3,	2,	'22:00:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4893,	3,	2,	'22:30:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4894,	3,	2,	'23:00:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4895,	3,	2,	'23:30:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4896,	3,	2,	'00:00:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4897,	3,	3,	'01:00:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4898,	3,	3,	'02:00:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4899,	3,	3,	'03:00:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4900,	3,	3,	'04:00:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4901,	3,	3,	'05:00:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4902,	3,	3,	'06:00:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4903,	3,	3,	'07:00:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4904,	3,	3,	'08:00:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4905,	3,	3,	'09:00:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4906,	3,	3,	'10:00:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4907,	3,	3,	'11:00:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4908,	3,	3,	'12:00:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4909,	3,	3,	'13:00:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4910,	3,	3,	'14:00:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4911,	3,	3,	'15:00:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4912,	3,	3,	'16:00:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4913,	3,	3,	'17:00:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4914,	3,	3,	'18:00:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4915,	3,	3,	'19:00:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4916,	3,	3,	'20:00:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4917,	3,	3,	'21:00:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4918,	3,	3,	'22:00:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4919,	3,	3,	'23:00:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4920,	3,	3,	'00:00:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4921,	3,	4,	'03:00:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4922,	3,	4,	'06:00:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4923,	3,	4,	'09:00:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4924,	3,	4,	'12:00:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4925,	3,	4,	'15:00:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4926,	3,	4,	'18:00:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4927,	3,	4,	'21:00:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48'),
(4928,	3,	4,	'00:00:00',	'2021-10-29 02:51:48',	'2021-10-29 02:51:48');

-- 2021-10-29 03:09:48
