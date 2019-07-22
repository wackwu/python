#-*- coding：utf-8 -*-
#Author：wu 
# Time: 2018年8月15日 09:40

#获取文件中第二行，第一列的信息

#导入需要使用的相关模块
import csv

#从文件中获取最高气温
filename = '/Users/wuxuhao/Desktop/Python/Data Csv/files/death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    head_row = next(reader)

    highs = []
    for row in reader:
        #去除表里面的空值
        try:
            high = int(row[1])
        except ValueError:
            print(high, 'missing data')
        else:
            highs.append(high)

    print(highs)


#从文件中获取名字
filename = '/Users/wuxuhao/Desktop/Python/Data Csv/files/xu.csv'
with open(filename) as f:
    reader = csv.reader(f)
    head_row = next(reader)

    NickName = []
    for row in reader:
        NickName.append(row[1])

    print(NickName)