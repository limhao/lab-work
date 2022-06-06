import pymysql

db = pymysql.connect(host="localhost",
                     port=3306,
                     user='root',
                     charset='utf8',
                     password='111111',
                     db='db1'

)
cursor = db.cursor()
# # 这一行是插入 信息
# # 启动 mysql 定义表项
# up_mysql = """
# CREATE TABLE myData (
#   `main` TEXT,
#   `topic` TEXT,
#   `content` TEXT,
#   `startTime` TEXT,
#   `endTime` TEXT,
#   `id` int(11) NOT NULL AUTO_INCREMENT,
#   PRIMARY KEY (id)
# );
# """
# cursor.execute(up_mysql)
# db.commit()
# db.close()
sql = """INSERT INTO myData(main ,topic,
         content, startTime, endTime)
         VALUES ("[10.4.1]--单元开篇.mp4", "从Web解析到网络空间", "-Python,库之网络爬虫-Python,库之Web信息提取-Python库之Web网站开发-Python库之网络应用开发", "23.832", "34.2")"""
try:
	cursor.execute(sql)
	db.commit()
except Exception as e:
	print('出错')
	db.rollback()
	print(e)
db.close()