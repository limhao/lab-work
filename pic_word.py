# coding=utf-8

import sys
import json
import base64

# 保证兼容python2以及python3
import time

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

OCR_URL = 'https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic'

"""  TOKEN start """
TOKEN_URL = 'https://aip.baidubce.com/oauth/2.0/token'

"""
    获取token
"""
# 定义垃圾词
rubbish_word = ['己utho', 'bnmou', 'pyho如', '知中国大学MOOC', '中国大学MOOC', 'python', '2', 'bdryou', 'pythoni', 'baryoul',
                'barpou', 'bdrpou', "python'", '和中国大学MOOC', 'pythom', 'pyhQ心', 'pyho或', 'bAmou', 'pyhQ吸', 'bao则',
                'bpo网']


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


def sort_string_list(string_list):
	new = []
	for i in string_list:
		new.append(float(i[:-4]))
	new.sort()
	return new


def rubbish_word_fun(result_json, rubbish_word):
	restart = True
	while restart:
		restart = False
		word_num = len(result_json['words_result'])
		for k in range(word_num):
			try:
				if result_json['words_result'][k]['words'] in rubbish_word:
					del result_json['words_result'][k]
					restart = True
				elif len(result_json['words_result'][k]['words']) <= 3:
					del result_json['words_result'][k]
					restart = True
				elif k == (word_num - 1):
					restart = False
			except Exception as e:
				print(e)
		return result


className = "python语言程序设计"
pic_root = os.path.join(os.getcwd(), 'pic')
word_root = os.path.join(os.getcwd(), 'text')
classPicRoot = os.path.join(pic_root, className)
classWordRoot = os.path.join(word_root, className)


if __name__ == '__main__':

	# 获取access token
	token = fetch_token()

	# 拼接通用文字识别高精度url
	image_url = OCR_URL + "?access_token=" + token

	text = ""
	topic = ""
	main = '[3.2.6]--单元小结.mp4'
	now_address = os.path.join(classPicRoot, main)
	pic_file_name = file_pic_name(now_address)
	sort_pic_file = sort_string_list(pic_file_name)
	# print(pic_file_name)
	# 记得到时候激活
	# os.mkdir(os.path.join(word_root, '[9.7.1]--练习与作业.mp4'))
	text_address = os.path.join(classWordRoot, main)
	try:
		os.mkdir(text_address)
	except Exception as e:
		print(e)
	# print(os.path.join(word_root, '[9.7.1]--练习与作业.mp4'))
	# 文件遍历
	# 记录图片开始的记录
	num = 0
	for i in range(len(sort_pic_file)):
		# 前后顺序很重要
		name = str(sort_pic_file[i]) + '.png'
		print(name)
		# print(i)
		request_json = True
		while request_json:
			pic_add = os.path.join(now_address, name)
			# print(pic_add)
			pic_content = read_file(pic_add)
			result = request(image_url, urlencode({'image': base64.b64encode(pic_content)}))
			result_json = json.loads(result)
			# 错误请求
			try:
				if result_json['error_code'] == 18:
					print('qps请求炸了')
					print(result_json)
					time.sleep(0.5)
					request_json = True
			except:
				request_json = False
				pass

		new_dict = {

		}

		# 垃圾词清理
		try:
			if result_json['words_result_num'] <= 3:
				num = num + 1
				print('初始内容太少 删除')
				continue
		except Exception as e:
			print(e)
		# else:
		# 	result_json = rubbish_word_fun(result_json, rubbish_word)
		else:
			restart = True
			while restart:
				restart = False
				exam = len(result_json['words_result'])
				for k in range(exam):
					# print(i)
					try:
						if result_json['words_result'][k]['words'] in rubbish_word:
							del result_json['words_result'][k]
							restart = True
						elif len(result_json['words_result'][k]['words']) <= 3:
							del result_json['words_result'][k]
							restart = True
						elif k == (exam - 1):
							restart = False
					except:
						pass
		# 被删光管理
		if len(result_json['words_result']) == 0:
			num = num + 1
			print('被我删光了 你来打我')
			continue

		# 改成函数 不晓得 为什么不行
		# result_json = rubbish_word_fun(result_json, rubbish_word)
		# for i in range(1, len(result_json['words_result'])):
		# 	text += result_json['words_result'][i]['words']
		# 第一个数据必不可能是topic相同
		# 这里topic改变 应该留到限免去处理
		# try:
		# 	if topic != result_json['words_result'][0]['words']:
		# 		text = ''
		# except Exception as e:
		# 	continue

		try:
			for lala in range(1, len(result_json['words_result'])):
				# 这个是最后的text
				if result_json['words_result'][lala]['words'] in topic_context:
					continue
				text += result_json['words_result'][lala]['words']

		except Exception as e:
			print(e)
		# 这句话 只能走一次 的确直走一次
		if i == num:
			startTime = name[:-4]
			topic = result_json['words_result'][0]['words']
			for lala in range(1, len(result_json['words_result'])):
				text += result_json['words_result'][lala]['words']
			print(startTime)
		# 完成了改变
		elif topic != result_json['words_result'][0]['words']:
			new_dict['className'] = className
			new_dict['main'] = main
			new_dict['topic'] = topic
			new_dict['content'] = text
			new_dict['startTime'] = startTime
			new_dict['endTime'] = name[:-4]
			topic = topic.replace(':', '')
			json_dit = topic + '.json'
			json_add = os.path.join(text_address, json_dit)
			print(new_dict)
			# 成功啦
			with open(json_add, 'w', encoding='utf8') as f:
				json.dump(new_dict, f, ensure_ascii=False)
				print('处理好了')
			startTime = name[:-4]
			new_dict = {}
		# 关注尾部
		# 最后一个是抓住了
		elif i == (len(pic_file_name) - 1):
			new_dict['className'] = className
			new_dict['main'] = main
			new_dict['topic'] = topic
			new_dict['content'] = text
			new_dict['startTime'] = startTime
			new_dict['endTime'] = name[:-4]
			topic = topic.replace(':', '')
			json_dit = topic + '.json'
			json_add = os.path.join(text_address, json_dit)
			print(json_add)
			print(new_dict)
			with open(json_add, 'w', encoding='utf8') as f:
				json.dump(new_dict, f, ensure_ascii=False)
				print('最后一个')
			startTime = name[:-4]
			new_dict = {}
		# new_dict['topic'] = result_json['words_result'][0]['words']
		# print(len(result_json['words_result']))
		topic = result_json['words_result'][0]['words']
		topic_context = []
		for content in range(1, len(result_json['words_result'])):
			topic_context.append(result_json['words_result'][content]['words'])
		print(topic_context)
