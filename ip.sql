# Host: localhost  (Version: 5.5.53)
# Date: 2020-08-01 18:00:24
# Generator: MySQL-Front 5.3  (Build 4.234)

/*!40101 SET NAMES utf8 */;

#
# Structure for table "ip"
#

DROP TABLE IF EXISTS `ip`;
CREATE TABLE `ip` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ip` varchar(255) DEFAULT NULL,
  `port` int(11) DEFAULT NULL,
  `ok` int(11) NOT NULL DEFAULT '0' COMMENT '-1未知 0可以 1不可用',
  `time` varchar(255) DEFAULT NULL COMMENT '当ok为-1则为获取时间 为0则为验证时间',
  `come` varchar(255) DEFAULT NULL COMMENT '来源',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=0 DEFAULT CHARSET=utf8;

#
# Data for table "ip"
#

/*!40000 ALTER TABLE `ip` DISABLE KEYS */;
/*!40000 ALTER TABLE `ip` ENABLE KEYS */;
