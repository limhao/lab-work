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
CREATE TABLE generic (
  `main` TEXT,
  `topic` TEXT,
  `content` TEXT,
  `startTime` TEXT,
  `endTime` TEXT,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (id)
);


BEGIN;
