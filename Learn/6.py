# -*- coding：utf-8 -*-
# Author：wu 
# Time: 2019年6月24日 20:40
# Target:现在有一个社会学家，在不同的人群中做这个实验，一旦遇到都不认罪的情况，就停止该人群中的实验。
#        同时，他希望程序能记录每一对实验者的选择，以及记录第几对实验者都选择不认罪。请你帮帮他吧。


n = 0
list_answer = []

while True:
    n += 1
    a = input('A，你认罪吗？请回答认罪或者不认：')
    b = input('B，你认罪吗？请回答认罪或者不认：')
    list_answer.append([a,b])  # 用列表嵌套的方式来存放实验者的选择，也可用元组或字典。
    if a == '认罪' and b == '认罪':
        print('两人都得判10年，唉')
    elif a == '不认' and b == '认罪':
        print('A判20年，B判1年，唉')
    elif a == '认罪' and b == '不认':
        print('A判1年，B判20年')
    else:
        print('都判3年，太棒了')
        break

print('第' + str(n) + '对实验者选了最优解。')

for i in range(n):
    # 注意数据类型的转换，以及计数起点的不同（0和1）
    print('第' + str(i+1) + '对实验者的选择是：' + str(list_answer[i]))
