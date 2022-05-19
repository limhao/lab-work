# coding=utf-8

import sys
import json
import base64

# 保证兼容python2以及python3
IS_PY3 = 3
from urllib.request import urlopen
from urllib.request import Request
from urllib.error import URLError
from urllib.parse import urlencode

# 防止https证书校验不正确
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

API_KEY = 'ZOYegMvX3fVYGcn1zf13suG2'

SECRET_KEY = '6HjW4xdUWw9MXoaVT2jqTrfZGmOPWpZw'

OCR_URL = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic"

"""  TOKEN start """
TOKEN_URL = 'https://aip.baidubce.com/oauth/2.0/token'

"""
    获取token
"""
# 定义垃圾词
rubbish_word = ['中国大学MOOC', 'python', '2']


def fetch_token():
	params = {'grant_type': 'client_credentials',
	          'client_id': API_KEY,
	          'client_secret': SECRET_KEY}
	post_data = urlencode(params)
	if (IS_PY3):
		post_data = post_data.encode('utf-8')
	req = Request(TOKEN_URL, post_data)
	try:
		f = urlopen(req, timeout=5)
		result_str = f.read()
	except URLError as err:
		print(err)
	if (IS_PY3):
		result_str = result_str.decode()

	result = json.loads(result_str)

	if ('access_token' in result.keys() and 'scope' in result.keys()):
		if not 'brain_all_scope' in result['scope'].split(' '):
			print('please ensure has check the  ability')
			exit()
		return result['access_token']
	else:
		print('please overwrite the correct API_KEY and SECRET_KEY')
		exit()


"""
    读取文件
"""


def read_file(image_path):
	f = None
	try:
		f = open(image_path, 'rb')
		return f.read()
	except:
		print('read image file fail')
		return None
	finally:
		if f:
			f.close()


"""
    调用远程服务
"""


def request(url, data):
	req = Request(url, data.encode('utf-8'))
	has_error = False
	try:
		f = urlopen(req)
		result_str = f.read()
		if (IS_PY3):
			result_str = result_str.decode()
		return result_str
	except  URLError as err:
		print(err)


def file_video_name(file_dir):
	File_Name = []
	for files in os.listdir(file_dir):
		if os.path.splitext(files)[1] == '.mp4':
			File_Name.append(files)
	return File_Name


import os


def file_pic_name(file_dir):
	File_Name = []
	for files in os.listdir(file_dir):
		if os.path.splitext(files)[1] == '.png':
			File_Name.append(files)
	return File_Name


pic_root = os.path.join(os.getcwd(), 'pic')
word_root = os.path.join(os.getcwd(), 'word')
if __name__ == '__main__':

	# 获取access token
	token = fetch_token()

	# 拼接通用文字识别高精度url
	image_url = OCR_URL + "?access_token=" + token

	text = ""

	# 读取测试图片
	# file_content = read_file('frame.2847600.png')

	# 调用文字识别服务
	# result = request(image_url, urlencode({'image': base64.b64encode(file_content)}))

	# 解析返回结果
	# result_json = json.loads(result)
	# for words_result in result_json["words_result"]:
	# 	text = text + words_result["words"]

	# 打印文字
	# print(text)

	# 打印json

	# print(result_json)

	# 试着去读一个文件夹
	#
	now_address = os.path.join(pic_root, '[3.2.6]--单元小结.mp4')
	pic_file_name = file_pic_name(now_address)
	# print(pic_file_name)
	for name in pic_file_name:
		# 前后顺序很重要
		pic_add = os.path.join(now_address, name)
		# print(pic_add)
		pic_content = read_file(pic_add)
		result = request(image_url, urlencode({'image': base64.b64encode(pic_content)}))
		result_json = json.loads(result)
		# 我拿到json了
		# print(result_json)
		new_json = {

		}
		text = ''
		target = ''
		if result_json['words_result_num'] < 3:
			continue
		else:
			for i in range(len(result_json['words_result']) - 1):
				# print(i)
				try:
					if result_json['words_result'][i]['words'] in rubbish_word:
						del result_json['words_result'][i]
					if len(result_json['words_result'][i]['words']) <= 3:
						del result_json['words_result'][i]
				except Exception as e:
					print(e)
			new_json['topic'] = result_json['words_result'][0]['words']
			# print(len(result_json['words_result']))
			for i in range(1, len(result_json['words_result'])):
				text += result_json['words_result'][i]['words']
			new_json['content'] = text
			new_json['time'] = name[:-4]

		print(new_json)
