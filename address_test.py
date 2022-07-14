import os

pic_root = os.path.join(os.getcwd(), 'pic')
word_root = os.path.join(os.getcwd(), 'word')


# 这个代码是获得文件夹内的文件


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


# 拿到文件地址
video_file_name = file_video_name(pic_root)
now_address = os.path.join(pic_root, '[3.2.6]--单元小结.mp4')
pic_file_name = file_pic_name(now_address)
# 成了没
print(pic_file_name)
# print(video_file_name)
rubbish_word = ['中国大学MOOC', 'python', '2']

from pic_word import read_file, fetch_token, request


