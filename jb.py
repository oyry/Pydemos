# 脚本类，组合工具参数进行请求
import requests
import json
from WECHAT.cl import *
from WECHAT.gj import DICT
import traceback
import subprocess
gj=DICT()
def testall():
    apikeys = API.keys()
    for key in apikeys:
        apiname = key
        url = API[key]['url']
        querystring = API[key]['querystring']
        number = API[key]['number']
        print("=======" "api编号："+ number+" api名称：" + apiname + "=======")
        global payload
        for value in WORDS.values():
            INPUT = str(value)
            INDATA = ''.join(INPUT)
            # print(INDATA)
            payload = {"channel_id": "WECHAT", "id_type": "5", "id_keyword": INDATA}
            response = requests.request("POST", url=url, data=payload, params=querystring)
            code = str(response.status_code)
            time = str(response.elapsed.microseconds)
            print("接口响应code：" + code + "\t接口响应时间：" + time + "\t接口返回信息：\n" + str(response.json()))
testall()
res=subprocess.Popen('if not exist F:/code/OCMTEST/Loginfo/json.txt',shell=True,stdout=subprocess.PIPE)
try:
    FILE = open('F:/code/OCMTEST/Loginfo/json.txt', 'w', encoding="utf-8")
    FILE.write(json.dumps(payload,ensure_ascii=False,indent=4))
    FILE.close
except:
    traceback.print_exc()