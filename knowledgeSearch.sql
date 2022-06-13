/*
 Navicat Premium Data Transfer

 Source Server         : warma
 Source Server Type    : MySQL
 Source Server Version : 80016
 Source Host           : localhost:3306
 Source Schema         : mtianyanSearch

 Target Server Type    : MySQL
 Target Server Version : 80016
 File Encoding         : 65001

 Date: 06/06/2022
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

DROP TABLE IF EXISTS `myData`;
CREATE TABLE myData (
  `className` TEXT,
  `main` TEXT,
  `topic` TEXT,
  `content` TEXT,
  `startTime` TEXT,
  `endTime` TEXT,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (id)
);


BEGIN;
INSERT INTO myData(className ,main ,topic,content, startTime, endTime) VALUES ("python语言程序设计","[10.4.1]--单元开篇.mp4", "从Web解析到网络空间", "-Python,库之网络爬虫-Python,库之Web信息提取-Python库之Web网站开发-Python库之网络应用开发", "23.832", "34.2");
COMMIT;
