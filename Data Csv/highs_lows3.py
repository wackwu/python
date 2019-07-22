#-*- coding：utf-8 -*-
#Author：wu 
# Time: 2018年8月14日 10:03

#根据得到文件中的数据绘制折线图

#导入需要使用的相关模块
import csv
from datetime import datetime
from matplotlib import pyplot as plt

#从文件中获取日期和最高气温
filename = '/Users/wuxuhao/Desktop/Python/Data Csv/files/sitka_weather_07-2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    head_row = next(reader)

    dates, highs = [], []
    for row in reader:
        current_date = datetime.strptime(row[0], "%Y-%m-%d")
        dates.append(current_date)
        high = int(row[1])
        highs.append(high)

    print(highs)

#根据数据绘制图形
fig = plt.figure(dpi=100, figsize=(10, 6))
plt.plot(dates, highs, c='red')

#设置图形的格式
plt.title("Daily high temperatures, July 2014", fontsize = 24)
plt.xlabel('Datetime', fontsize = 16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize = 16)
plt.tick_params(axis='both', which='major', labelsize = 16)

plt.show() 