import os
import json

className = "python语言程序设计"
pic_root = os.path.join(os.getcwd(), 'pic')
word_root = os.path.join(os.getcwd(), 'text')
classPicRoot = os.path.join(pic_root, className)
classWordRoot = os.path.join(word_root, className)
for filepath, dirnames, filenames in os.walk(os.path.join(pic_root, className)):
	# 这里会响应一次 选择os.mkdir
	#print(filepath)
	# main 获取
	main = os.path.split(filepath)[-1]
	for filename in filenames:
		print(os.path.join(main, filename))