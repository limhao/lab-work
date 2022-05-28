import os
pic_root = os.path.join(os.getcwd(), 'pic')
word_root = os.path.join(os.getcwd(), 'text')


def file_video_name(file_dir):
	File_Name = []
	for files in os.listdir(file_dir):
		if os.path.splitext(files)[1] == '.mp4':
			File_Name.append(files)
	return File_Name

def file_pic_name(file_dir):
	File_Name = []
	for files in os.listdir(file_dir):
		if os.path.splitext(files)[1] == '.png':
			File_Name.append(files)
	return File_Name

for files in os.listdir(pic_root):
	# 获得文件夹位置
	now_address = os.path.join(pic_root, files)
	now_word_address = os.path.join(word_root, files)
	print(now_word_address[:-4])
	pic_file_name = file_pic_name(now_address)
	for name in pic_file_name:
		pic_add = os.path.join(now_address, name)
		# 送图片 会结果 处理
		# print(name[:-4])
		# print(now_address)
		result_json = {
			"words_result": [
				{
					"words": "中国大学MOOC"
				},
				{
					"words": "深入理解Python语言"
				},
				{
					"words": "-计算机系统结构时代到人工智能时代的演进路线"
				},
				{
					"words": "-五种编程语言的初心和历史使命"
				},
				{
					"words": "-Python语言的通用性、简洁性和生态性"
				},
				{
					"words": "python"
				},
				{
					"words": "如"
				}
			],
			"words_result_num": 7,
			"log_id": 1526782073422385246
		}
		title = files[:-4] + name[:-4]
		# print(title)
		# print(files)
		# print(pic_add)
# now_address = os.path.join(pic_root, '[3.2.6]--单元小结.mp4')
# pic_file_name = file_pic_name(now_address)