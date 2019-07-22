#-*- coding：utf-8 -*-
#Author：wu 
# Time: 2018年8月14日 22:30

#处理csv文件，并读取第一行文字

#导入需要使用的相关模块
import csv

filename = '/Users/wuxuhao/Desktop/Python/Data Csv/files/death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    head_row = next(reader)

    for index, column_header in enumerate(head_row):
        print(index, column_header)



filename = '/Users/wuxuhao/Desktop/Python/Data Csv/files/xu.csv'
with open(filename) as f:
    reader = csv.reader(f)
    head_row = next(reader)

    for index, column_header in enumerate(head_row):
        print(index, column_header)