#-*- coding：utf-8 -*-
#Author：wu 
# Time: 2018年8月15日 10:34

#获取文件中的两个数据，并在一张图上绘制折线图，并且标注出差距区域

#导入需要使用的相关模块
import csv
import pygal
from datetime import datetime
from matplotlib import pyplot as plt

#从文件中获取日期、最高气温和最低气温
filename = '/Users/wuxuhao/Desktop/Python/Data Csv/files/sitka_weather_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    head_row = next(reader)

    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[0], '%Y-%m-%d')
        dates.append(current_date)

        #最高温
        high = int(row[1])
        highs.append(high)
        
        #最低温
        low = int(row[3])
        lows.append(low)

    # print(highs)
    # print(lows)
    # print(dates)

#根据数据绘制图形(alpha代表颜色的透明度，数值0是完全透明)
fig = plt.figure(dpi=125, figsize=(10, 6))
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='yellow', alpha=0.1)

#设置图形的格式
plt.title("Daily high and low temperatures - 2014", fontsize = 24)
plt.xlabel('Datetime', fontsize = 16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize = 16)
plt.tick_params(axis='both', which='major', labelsize = 16)

plt.show() 

#保存为svg图片
filename = '/Users/wuxuhao/Desktop/Python/Data Csv/files/sitka_weather_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    head_row = next(reader)

    dates = []
    for row in reader:
        current_date_str = datetime.strptime(row[0], '%Y-%m-%d')#将表格里面的时间先转换成str
        current_date = datetime.strftime(current_date_str, '%Y-%m-%d')#先str转换成想要的Datetime
        dates.append(current_date)
image = pygal.Line(x_label_rotation=20, show_minor_x_labels=False)
image.title = "Daily high and low temperatures - 2014"
image.x_labels = dates
N = 20 #X坐标轴每隔20天显示一次
image.x_labels_major = dates[::N]
image.y_title = "Temperature (F)"
image.add('highs', highs, c='red')
image.add('lows', lows, c='blue')
image.render_to_file("/Users/wuxuhao/Desktop/Python/Data Csv/files/highs_lows4.svg")
