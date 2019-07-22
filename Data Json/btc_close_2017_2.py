#-*- coding：utf-8 -*-
#Author：wu 
# Time: 2018年8月16日 14:00

#json读取方法

#导入需要使用的相关模块
import json

#将数据加载到一个列表中
filename = '/Users/wuxuhao/Desktop/Python/Data Json/files/btc_close_2017.json'
with open(filename) as f:
    btc_data = json.load(f)

#打印每一天的信息，原始数据打印出
for btc_dict in btc_data:
    date = btc_dict['date']
    month = btc_dict['month']
    week = btc_dict['week']
    weekday = btc_dict['weekday']
    close = btc_dict['close']
    print("{} is month {} week {}, {}, the close price is {} RMB". format(date, month, week, weekday, close))


#打印每一天信息，用int类型打印出数据
for btc_dict in btc_data:
    date = btc_dict['date']
    month = int(btc_dict['month'])
    week = int(btc_dict['week'])
    weekday = btc_dict['weekday']
    close = int(float(btc_dict['close']))
    print("{} is month {} week {}, {}, the close price is {} RMB". format(date, month, week, weekday, close))