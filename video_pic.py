import os
from collections import Counter

dir_video_src = os.path.join(os.getcwd(), 'video')

# 这个代码是获得文件夹内的文件
# def file_name(file_dir):
# 	File_Name = []
# 	for files in os.listdir(file_dir):
# 		if os.path.splitext(files)[1] == '.mp4':
# 			File_Name.append(files)
# 	return File_Name
#
#
# txt_file_name = file_name(dir_video_src)
# print(txt_file_name)

# os.getcwd() 获得当前地址

'''
描述： 下面这一个代码 是获得目标文件夹内的所有视频文件 并且存成list 存储

'''
import av
import os
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)

dir_video_des = os.path.join(os.getcwd(), 'pic')


def extract_video(filename):
	container = av.open(filename)
	# Signal that we only want to look at keyframes.
	stream = container.streams.video[0]
	stream.codec_context.skip_frame = 'NONKEY'
	# default 不能用
	# stream.codec_context.skip_frame = 'DEFAULT'
	for frame in container.decode(stream):
		# 这里应该能管到时间戳
		frame.to_image().save(
			'{}.png'.format((frame.pts/100000), '.1f'),
			quality=80,
		)


import shutil

list_vid = []

for filepath, dirnames, filenames in os.walk(dir_video_src):
	for filename in filenames:
		# 文件地址
		# 筛选好文件名了
		if os.path.splitext(filename)[1] == '.mp4':
			# list_vid.append(filepath)
			# print(filename)
			# 存图片的地址
			file_dir_desc = os.path.join(dir_video_des, filename)
			if not os.path.exists(file_dir_desc):
				os.mkdir(file_dir_desc)
				print("创建文件夹 ", file_dir_desc)
			else:
				print("合并后的目录已存在")
			extract_video(os.path.join(filepath, filename))
			for filename_png in os.listdir(os.getcwd()):
				if ".png" in filename_png:
					# shutil.move(filename_png, file_dir_desc)
					shutil.copy2(filename_png, file_dir_desc)
					os.remove(filename_png)
	# 对于地址进行判断
	# 对filename 是可以完成筛选的

	# print(file)
	# print(filepath)
