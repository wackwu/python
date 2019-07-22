#-*- coding：utf-8 -*-
#Author：wu 
# Time: 2018年8月15日 11:21

#检查文件中错误的值，并跳过，然后打印出折线图

#导入需要使用的相关模块
import csv
from datetime import datetime
from matplotlib import pyplot as plt

#从文件中获取日期、最高气温和最低气温
filename = '/Users/wuxuhao/Desktop/Python/Data Csv/files/death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    head_row = next(reader)

    dates, highs, lows = [], [], []
    for row in reader:
        try:
            #日期
            current_date = datetime.strptime(row[0], "%Y-%m-%d")

            #最高温
            high = int(row[1])

            #最低温
            low = int(row[3])

        except ValueError:
            print(current_date, 'missing data')
            
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

    print(highs)
    print(lows)

#根据数据绘制图形(alpha代表颜色的透明度，数值0是完全透明)
fig = plt.figure(dpi=125, figsize=(10, 6))
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='yellow', alpha=0.1)

#设置图形的格式
title = "Daily high and low temperatures - 2014\nDeath Valley, CA"
plt.title(title, fontsize = 20)
plt.xlabel('Datetime', fontsize = 16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize = 16)
plt.tick_params(axis='both', which='major', labelsize = 16)

plt.show() 
