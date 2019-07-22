#-*- coding：utf-8 -*-
#导入需要使用的相关模块
import itchat
from pandas import DataFrame

#登陆方法，会弹出登陆二维码，用微信扫描登陆
itchat.auto_login()

#爬取自己好友相关信息，返回一个json文件
friends = itchat.get_friends(update=True)[0:]

#定义一个函数，用来爬取各个变量
def get_var(var):
    variable = []
    for i in friends:
        value = i[var]
        variable.append(value)
    return variable

#调用函数得到各变量，并把数据存到csv文件中
NickName = get_var("NickName")
Sex = get_var('Sex')
Province = get_var('Province')
City = get_var('City')
Signature = get_var('Signature')
data = {'NickName': NickName, 'Sex': Sex, 'Province':Province, 'City':City, 'Signature':Signature}
frame = DataFrame(data)
frame.to_csv('data.csv', index = True)

#使用柱状图打印出城市排序
