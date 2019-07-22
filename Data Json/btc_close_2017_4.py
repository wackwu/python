#-*- coding：utf-8 -*-
#Author：wu 
# Time: 2018年8月16日 16:00

#绘制数据中收盘价的折线图

#导入需要使用的相关模块
import json
import pygal
import math

#将数据加载到一个列表中
filename = '/Users/wuxuhao/Desktop/Python/Data Json/files/btc_close_2017.json'
with open(filename) as f:
    btc_data = json.load(f)

#创建5个列表，分别存储日期和收盘价
dates = []
months = []
weeks = []
weekdays = []
close = []

#每一天的信息
for btc_dict in btc_data:
    dates.append(btc_dict['date'])
    months.append(int(btc_dict['month']))
    weeks.append(int(btc_dict['week']))
    weekdays.append(btc_dict['weekday'])
    close.append(int(float(btc_dict['close'])))


#绘制图表
line_chart = pygal.Line(x_label_rotation=20, show_minor_x_labels=False)
line_chart.title = '收盘价对数变换（RMB）'
line_chart.x_labels = dates
N = 20 #X坐标轴每隔20天显示一次
line_chart.x_labels_major = dates[::N]
close_log = [math.log10(_) for _ in close]
line_chart.add('收盘价', close_log)
line_chart.render_to_file('/Users/wuxuhao/Desktop/Python/Data Json/files/收盘价对数变换折线图.svg')