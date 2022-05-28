# result_json = {'topic': '深入理解Python语言', 'content': '-计算机系统结构时代到人工智能时代的演进路线-五种编程语言的初心和历史使命-Python语言的通用性、简洁性和生态性-Python是以计算生态为标志的"超级语言”', 'time': '46.188'}
# import json
# file = r"C:\\Users\\warma\\Desktop\\get_point\\text\\[9.7.1]--练习与作业.mp4\\1.json"
#
# with open(file, 'w', encoding='utf-8') as f:
# 	json.dump(result_json, f)
# 	print('我写好了')
# # import os
# # time = "45664.45654" + ".json"
# # json_address = os.path.join("C:\\Users\\warma\\Desktop\\get_point\\text\\[9.7.1]--练习与作业.mp4", time)
# # print(json_address)
#
#
# with open(file, 'r', encoding='utf-8') as f:
#     data = json.load(file)
#     #<class 'dict'>,JSON文件读入到内存以后，就是一个Python中的字典。
#     # 字典是支持嵌套的，
#     print(data)
# import os
# import json
# ilgal_word = {':', ''}
# new_dict = {}
# new_dict['content'] = '111'
# new_dict['startTime'] = '111'
# new_dict['endTime'] = '111'
# new_dict['topic'] = '111'
# text_address = r'C:\\Users\\warma\\Desktop\\get_point\\text\\[3.2.6]--单元小结.mp4'
# topic = 'Q:为什么要学习计算机编程？.json'
# json_add = os.path.join(text_address, topic)
# print(new_dict)
# with open(json_add, 'w', encoding='utf-8') as f:
# 	json.dump(new_dict, f)
# 	print('处理好了')
# 转list
# list = ['1.332.png', '100.836.png', '104.616.png', '113.616.png', '122.616.png', '131.616.png', '140.616.png', '147.888.png', '15.12.png', '156.888.png', '165.888.png', '174.888.png', '183.888.png', '191.196.png', '24.12.png', '33.12.png', '42.12.png', '51.048.png', '6.12.png', '60.048.png', '69.048.png', '73.836.png', '82.836.png', '91.836.png']
# new = []
# for i in list:
# 	i = i[:-4]
# 	# print(i)
# 	i = float(i)
# 	new.append(i)
# new.sort()
# for i in new:
# 	i = str(i) + '.png'
# 	print(i)
# rubbish_word = ['中国大学MOOC', 'python', '2', 'bdryou', 'pythoni', 'baryoul']
# result_json = {'words_result': [{'words': '中国大学MOOC'}], 'words_result_num': 5, 'log_id': 1527938013406145728}
# # {'words': 'Q:为什么要学习计算机编程？'},{'words': 'baryoul'}, {'words': '2'}, {'words': 'A:因为编程是件很有趣的事儿！'},  {'words': 'pythoni'}
# restart = True
# while restart:
# 	restart = False
# 	exam = len(result_json['words_result'])
# 	for k in range(exam):
# 		# print(i)
# 		try:
# 			if result_json['words_result'][k]['words'] in rubbish_word:
# 				del result_json['words_result'][k]
# 				restart = True
# 			elif len(result_json['words_result'][k]['words']) <= 3:
# 				del result_json['words_result'][k]
# 				restart = True
# 			elif k == (exam - 1):
# 				restart = False
# 		except Exception as e:
# 			print(e)
# print(result_json)

# 试着遍历pic 文件夹
import os
def file_pic_name(file_dir):
	File_Name = []
	for files in os.listdir(file_dir):
		if os.path.splitext(files)[1] == '.png':
			File_Name.append(files)
	return File_Name
pic_root = os.path.join(os.getcwd(), 'pic')
def file_video_name(file_dir):
	File_Name = []
	for files in os.listdir(file_dir):
		if os.path.splitext(files)[1] == '.mp4':
			File_Name.append(files)
	return File_Name
name = file_video_name(pic_root)
#print(name)
print(name[1])
for filepath, dirnames, filenames in os.walk(os.path.join(pic_root, name[2])):
	# 这里会响应一次 选择os.mkdir
	print(filepath)
	for filename in filenames:

		print(os.path.join(filepath, filename))
	# print(dirnames)