import os
import json
# db = pymysql.connect(host="localhost",
#                      port=3306,
#                      user='root',
#                      charset='utf8',
#                      password='111111',
#                      db='db1'
#
# )
sql = """INSERT INTO myData(className ,main ,topic,
         content, startTime, endTime)
         VALUES ("python语言程序设计","[10.4.1]--单元开篇.mp4", "从Web解析到网络空间", "-Python,库之网络爬虫-Python,库之Web信息提取-Python库之Web网站开发-Python库之网络应用开发", "23.832", "34.2")"""
className = "python语言程序设计"
word_root = os.path.join(os.getcwd(), 'text')
classWordRoot = os.path.join(word_root, className)

if __name__ == '__main__':
	# 1. 拿到文件
	# 遍历目录
	# dir_path是当前遍历到的目录。dir_names是dir_path下的文件夹列表。file_names是是dir_path下的文件列表
	# 如果想实现目录白名单，将白名单目录从dir_names中去除即可
	for (dir_path, dir_names, file_names) in os.walk(classWordRoot):
		# print(dir_path)
		# print(dir_names)
		# print(file_names)
		for file_name in file_names:
			textRoot = os.path.join(dir_path, file_name)
			with open(textRoot, encoding='utf-8') as f:
				t = json.load(f)
				try:
					print(t[className])
				except:
					pass

