import json
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

# 对于 屏蔽词管理
rubbish_word = ['中国大学MOOC', 'python', '2']
# print(result_json['words_result'])
# target = ''
# if result_json['words_result_num'] >= 3:
# 	pass
# 	for text in result_json['words_result']:
# 		if text['words'] in rubbish_word:
# 			continue
# 		print(text['words'])
new_json = {}
# print(result_json['log_id'])
# new_json = new_json.append(684554584)
# print(new_json)
# for text in result_json:
# 	text = str(text)
# 	# 前面是键 后面是值
# 	new_json[text] = result_json[text]
# 	print(new_json)
print(type(result_json))
if result_json['words_result_num'] >= 3:
	# id会变
	# new_json['log_id'] = result_json['log_id']
	# 文字处理
	# 缺一个time
	# 等下写

	# 垃圾词处理完成
	text = ''
	new_json['topic'] = result_json['words_result'][0]['words']
	for i in range(1, len(result_json['words_result'])):
		text += result_json['words_result'][i]['words']
	new_json['content'] = text
# 这个东西 在加个时间 完美
print(new_json)