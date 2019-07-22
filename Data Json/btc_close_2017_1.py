#-*- coding：utf-8 -*-
#Author：wu 
# Time: 2018年8月15日 16:21

#请求文件地址数据，并把数据写入到规定好的文件中

#导入需要使用的相关模块
from __future__ import (absolute_import, division, print_function, unicode_literals)

try:
    #python 2.x版本
    from urllib2 import urlopen
except ImportError:
    #python 3.x 版本
    from urllib.request import urlopen

import requests
import json


json_url = 'https://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.json'
response = urlopen(json_url)

#读取数据
req1 = response.read()
req2 = requests.get(json_url)

#将数据写入文件
with open('/Users/wuxuhao/Desktop/Python/Data Json/files/btc_close_2017_urllib.json', 'wb') as f:
    f.write(req1)

with open('/Users/wuxuhao/Desktop/Python/Data Json/files/btc_close_2017_request.json', 'w') as f:
    f.write(req2.text)

#记载json格式
file_urllib = json.loads(req1)
print(file_urllib)

file_requests = req2.json()
print(file_urllib == file_requests)