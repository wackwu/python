#-*- coding：utf-8 -*-
#Author：wu 
# Time: 2018年8月14日 10:50

#绘制散点图

#导入需要使用的相关模块
import matplotlib.pyplot as plt

x_value = list(range(1, 10001))
y_value = [x ** 2 for x in x_value]
plt.scatter(x_value, y_value, c=y_value, cmap=plt.cm.Blues, edgecolors='none', s = 40)

#设置图表标题并给坐标轴加上标签
plt.title("Square Numbers", fontsize = 24)
plt.xlabel("Value", fontsize = 14)
plt.ylabel("Square of Value", fontsize = 14)

#设置刻度标记的大小
plt.tick_params(axis='both', which='major', labelsize = 14)

#设置每个坐标轴的取值范围
plt.axis([0, 1100, 0, 1100000])

image = plt.gcf()

plt.show()

#程序自动将图表保存到文件中，bbox代表去掉多余的白边
image.savefig("/Users/wuxuhao/Desktop/Python/Data Analysis/files/squares_plot.jpg", bbox_inches = 'tight', dpi = 200)