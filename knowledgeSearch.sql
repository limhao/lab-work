
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
CREATE TABLE `myData` (
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
INSERT INTO myData(className ,main ,topic, content, startTime, endTime) VALUES ('python语言程序设计','[10.4.1]--单元开篇.mp4','从Web解析到网络空间', '-Python,库之网络爬虫-Python,库之Web信息提取-Python库之Web网站开发-Python库之网络应用开发', '23.832','34.2');
INSERT INTO myData(className ,main ,topic, content, startTime, endTime) VALUES ('python语言程序设计','[3.2.6]--单元小结.mp4','深入理解Python语言', '-计算机系统结构时代到人工智能时代的演进路线-五种编程语言的初心和历史使命-Python语言的通用性、简洁性和生态性-Pythoni语言的通用性、简洁性和生态性-Python:是以计算生态为标志的"超级语言"', '19.188','46.188');
INSERT INTO myData(className ,main ,topic, content, startTime, endTime) VALUES ('python语言程序设计','[4.2.3]--浮点数类型.mp4','数字类型及操作', '与数学中实数的概念一致-带有小数点及小数的数字-浮点数取值范围和小数精度都存在限制，但常规计算可忽略-取值范围数量级约-1030至10308，精度数量级10-16浮点数间运算存在不确定尾数，不是bug>>>0.1+0.3>>>0.1+0.20.3000000600000004浮点数间运算存在不确定尾数，不是bug', '108.396','124.272');
INSERT INTO myData(className ,main ,topic, content, startTime, endTime) VALUES ('python语言程序设计','[4.2.3]--浮点数类型.mp4','浮点数类型', '与数学中实数的概念一致-带有小数点及小数的数字-浮点数取值范围和小数精度都存在限制，但常规计算可忽略-取值范围数量级约-1030至10308，精度数量级10-16浮点数间运算存在不确定尾数，不是bug>>>0.1+0.3>>>0.1+0.20.3000000600000004浮点数间运算存在不确定尾数，不是bug53位二进制表示小数部分，约1日1653位二进制表示小数部分，约100.00011001100110011001100110011001100110011001100110011010(二进制表示)0.1000000000000000055511151231257827021181583404541015625(十进制表示)二进制表示小数，可以无限接近，但不完全相同pyho心0.1+0.2结果无限接近0.3，但可能存在尾数浮点数间运算存在不确定尾数>>>0.1+0.2==0.3False>>>round(0.1+0.2,1)==0.3True-round(X,d):对x四舍五入，d是小数截取位数', '124.272','280.44');
INSERT INTO myData(className ,main ,topic, content, startTime, endTime) VALUES ('python语言程序设计','[4.2.3]--浮点数类型.mp4','浮点类型', '与数学中实数的概念一致-带有小数点及小数的数字-浮点数取值范围和小数精度都存在限制，但常规计算可忽略-取值范围数量级约-1030至10308，精度数量级10-16浮点数间运算存在不确定尾数，不是bug>>>0.1+0.3>>>0.1+0.20.3000000600000004浮点数间运算存在不确定尾数，不是bug53位二进制表示小数部分，约1日1653位二进制表示小数部分，约100.00011001100110011001100110011001100110011001100110011010(二进制表示)0.1000000000000000055511151231257827021181583404541015625(十进制表示)二进制表示小数，可以无限接近，但不完全相同pyho心0.1+0.2结果无限接近0.3，但可能存在尾数浮点数间运算存在不确定尾数>>>0.1+0.2==0.3False>>>round(0.1+0.2,1)==0.3True-round(X,d):对x四舍五入，d是小数截取位数-round(x,d):对x四舍五入，d是小数截取位数-浮点数间运算及比较用round0函数辅助-不确定尾数一般发生在1016左右，round0十分有效浮点数可以采用科学计数法表示-使用字母或E作为幂的符号，以10为基数，格式如下：<a>e<b>表示a*10b-例如：4.3e-3值为0.00439.6E5值为960000.0关于Python浮点数，需要知道多些取值范围和精度基本无限制运算存在不确定尾数round0', '280.44','417.492');
COMMIT;