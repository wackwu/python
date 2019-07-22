# -*- coding：utf-8 -*-
# Author：wu 
# Time: 2019年6月27日 10:30
# Target:眼看要过年了，深夜食堂经营的不错，你打算给员工发奖金犒劳一下。请你定义函数，当输入员工姓名和工作时长两个参数，即可打印出该员工获得多少奖金。
#        发放奖金的要求如下：
#        工作时长不满六个月，发放固定奖金500元。
#        工作时长在六个月和一年之间(含一年)，发放奖金120元*月数（如8个月为960元）
#        工作时长在一年以上，发放奖金180元*月数 （如20个月为3600元）



def bonus(come_time):
    if come_time <= 6:
        money = 500
    elif 6 < come_time <= 12:
        money = 120 * come_time
    else:
        money = 180 * come_time
    return money

def main(name, come_time):
    gain = bonus(come_time)
    print("%s来了%s个月，获得奖金%s元" % (name, come_time, gain))

main("大刚", 7)