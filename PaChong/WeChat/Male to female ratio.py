#-*- coding：utf-8 -*-
#导入需要使用的相关模块
import itchat
from echarts import Echart, Legend, Pie

#登陆方法，会弹出登陆二维码，用微信扫描登陆
itchat.auto_login()

#爬取自己好友相关信息，返回一个json文件
friends = itchat.get_friends(update=True)[0:]

#初始化计数器
male = female = other = 0
#friends[0]是自己的信息，所以要从friends[1]开始
#0表示不明性别，1表示男性，2表示女性
for i in friends[1:]:
    sex = i["Sex"]
    if sex == 1:
        male += 1
    elif sex == 2:
        female += 1
    else:
        other += 1

#计算朋友总数
total = len(friends[1:])
print ("好友总数是：", total)

#打印出自己好友的性别比例
print("男性好友: %.2f%%" % (float(male) / total * 100) + "\n" + 
      "女性好友: %.2f%%" % (float(female) / total * 100) + "\n" + 
      "不明性别好友: %.2f%%" % (float(other) / total * 100))

#使用饼图打印出自己好友的性别比例
chart = Echart('%s的微信好友性别比例' % (friends[0]['NickName']), 'from Wechat')
chart.use(Pie('Wechat', 
                   [{'Value': male, "name": '男性好友: %.2f%%' % (float(male) / total * 100)},
                    {'Value': female, "name": '女性好友: %.2f%%' % (float(female) / total * 100)},
                    {'Value': other, "name": '不明性别好友: %.2f%%' % (float(other) / total * 100)}],
    radius = ["50%", "70%"]))
chart.use(Legend(["male", "female", "other"]))
del chart.json["xAxis"]
del chart.json["yAxis"]
chart.plot()