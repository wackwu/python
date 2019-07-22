# -*- coding：utf-8 -*-
# Author：wu 
# Time: 2018年8月14日 21:54

# 抛一个6面的骰子，并绘制点数柱状图

# 导入需要使用的相关模块
import pygal
from die import Die

# 创建一个D6
die = Die()

# 掷几次骰子，并将结果存储在一个列表中
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# 分析结果
frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# print(frequencies)

# 对结果进行可视化
hist = pygal.Bar()

hist.title = "Result of rolling one D6 10000 times"
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6', frequencies)
hist.render_to_file('/Users/wuxuhao/Desktop/Python/Data Analysis/files/die_visual1.svg')