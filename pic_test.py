import operator
import os
import json

className = "python语言程序设计"
pic_root = os.path.join(os.getcwd(), 'pic')
word_root = os.path.join(os.getcwd(), 'text')
classPicRoot = os.path.join(pic_root, className)
classWordRoot = os.path.join(word_root, className)
# print(os.listdir(classWordRoot))

# for filepath, dirnames, filenames in os.walk(os.path.join(pic_root, className)):
# 	# 这里会响应一次 选择os.mkdir
# 	#print(filepath)
# 	# main 获取
# 	main = os.path.split(filepath)[-1]
# 	print(main)
# 	for filename in filenames:
# 		pass

# def topic_rechange(topic):
# 	illagle = ['.', ',', '"', '…']
# 	for word in illagle:
# 		topic = topic.replace(word, '')
# 	return topic
#
# topic = "实践、认识、再实践、再认识…"
#
# print(topic_rechange(topic))

topic = '己puthon'
print(operator.contains(topic, "己"))

