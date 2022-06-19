import os
import json
# db = pymysql.connect(host="localhost",
#                      port=3306,
#                      user='root',
#                      charset='utf8',
#                      password='111111',
#                      db='db1'
#
#
className = "python语言程序设计"
word_root = os.path.join(os.getcwd(), 'text')
classWordRoot = os.path.join(word_root, className)
sqlRoot = os.path.join(os.getcwd(), 'knowledgeSearch.sql')
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
				# 这里的key 需要加'' 否则 回报keyerror 错误
				# 是'' 不是 ""
				sql = """INSERT INTO myData(className ,main ,topic, content, startTime, endTime) VALUES ('{}','{}','{}', '{}', '{}','{}');""".format(t['className'], t['main'], t['topic'], t['content'], t['startTime'], t['endTime'])
				# sql语句写入
				print(sql)
				with open(sqlRoot, 'a', encoding='utf-8') as t:
					t.write(sql)
					t.write('\n')



