# -*- coding：utf-8 -*-
# Author：wu 
# Time: 2019年6月19日 16:30
# Target: 使用数据转换str()、int()、float()及数据拼接符号+,打印一句话： 脸黑怪我咯7张蓝票一个SSR都没有


slogan = '脸黑怪我咯'
number = '7.8'
unit = '张'
sentence = '蓝票一个SSR都没有'
number2 = int(float(number))
print(type(slogan))
print(type(number2))
print(number2)
print(type(unit))
print(type(sentence))
print(slogan + str(number2) + unit + sentence)
