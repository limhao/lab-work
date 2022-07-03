import requests
import base64
import json
def getResult(imagePath):
    with open(imagePath, 'rb') as f:
        data = f.read()
    image = str(base64.b64encode(data), encoding='utf-8')
    data = '{"images":["' + image + '"]}'
    txt = requests.post("http://paddleocr.paddleocr.1227030814500443.cn-shenzhen.fc.devsapp.net/predict/ocr_system", data = data,
                        headers={'Content-Type': 'application/json'})
    return txt.content.decode("utf-8")


# text = {"msg":"","results":[[{"confidence":0.8851825594902039,"text":"中中国大学MOOC","text_region":[[787,25],[930,25],[930,42],[787,42]]},{"confidence":0.9835241436958313,"text":"第1章Python基本语法元素","text_region":[[138,61],[643,63],[643,99],[138,97]]},{"confidence":0.9846452474594116,"text":"-1.1","text_region":[[245,195],[289,195],[289,216],[245,216]]},{"confidence":0.9988856911659241,"text":"程序设计基本方法","text_region":[[310,195],[519,195],[519,217],[310,217]]},{"confidence":0.9860273599624634,"text":"-1.2","text_region":[[245,244],[292,244],[292,266],[245,266]]},{"confidence":0.9966786503791809,"text":"Python开发环境配置","text_region":[[286,245],[555,245],[555,268],[286,268]]},{"confidence":0.9774389266967773,"text":"-1.3","text_region":[[245,292],[299,292],[299,317],[245,317]]},{"confidence":0.95084547996521,"text":"实例1：温度转换","text_region":[[307,293],[497,296],[497,320],[307,317]]},{"confidence":0.9739024043083191,"text":"-1.4","text_region":[[245,344],[298,344],[298,366],[245,366]]},{"confidence":0.9975464940071106,"text":"Python程序语法元素分析","text_region":[[291,345],[607,345],[607,368],[291,368]]},{"confidence":0.8748312592506409,"text":"pythom","text_region":[[59,448],[219,441],[222,493],[62,500]]}]],"status":"000"}
text = getResult('./84.096.png')
text = json.loads(text)

print(type(text))
print(text["results"])
# print(text['results'])
# 这个接口才算是取到了
# print(text["results"][0])
# print(len(text["results"][0]))
text1 = {"msg":"","results":[[{"confidence":0.9296902418136597,"text":"中国大学MOOC","text_region":[[789,24],[929,25],[929,42],[789,41]]},{"confidence":0.9363934397697449,"text":"pythom","text_region":[[101,381],[209,365],[215,403],[107,420]]},{"confidence":0.6767761707305908,"text":"baruou","text_region":[[103,470],[212,458],[216,496],[107,507]]}]],"status":"000"}
