#-*- coding：utf-8 -*-
#Author：wu 
# Time: 2018年8月14日 22:17

#抛一个6面的骰子跟一个10面的骰子，并绘制点数柱状图

#导入需要使用的相关模块
import pygal
from die import Die

#创建一个D6和一个D10
die_1 = Die()
die_2 = Die(10)

#掷骰子多次，并将结果存储在一个列表中
results = []
for roll_num in range(50000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

#分析结果
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

#print(frequencies)

#对结果进行可视化
hist = pygal.Bar()

hist.title = "Result of rolling D6 and D10 500000 times"
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 + D10', frequencies)
hist.render_to_file('/Users/wuxuhao/Desktop/Python/Data Analysis/files/die_visual3.svg')