import os
from collections import Counter

video_src = os.path.join(os.getcwd(), 'video')
video_des = os.path.join(os.getcwd(), 'pic')

# attention 你需要填入的信息
# 课程名称
dir_video_src = os.path.join(video_src, 'python语言程序设计')
# os.getcwd() 获得当前地址
# 存入的图片的地址
dir_video_des = os.path.join(video_des, 'python语言程序设计')
os.mkdir(dir_video_des)
'''
描述： 下面这一个代码 是获得目标文件夹内的所有视频文件 并且存成list 存储

'''
import av
import os
import warnings
import shutil

warnings.filterwarnings("ignore", category=DeprecationWarning)


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

