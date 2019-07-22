# -*- coding：utf-8 -*-
# Author：wu 
# Time: 2018年9月3日 20:45

# if语句

# 一个简单示例
cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())


""" 条件测试 """

# 检查是否相等
cars = 'bmw'
if cars == 'bmw':
    print(True)
else:
    print(False)

# 检查是否不相等
requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
    print("Hold the anchovies")

# 比较数字
answer = 17

if answer != 42:
    print("That is not the correct answer. Please try again!")

# 检查多个条件
age1 = 22
age2 = 18
if (age1 >= 0) and (age2 >= 21):
    print(True)
else:
    print(False)

age1 = 22
age2 = 18
if (age1 >= 0) or (age2 >= 21):
    print(True)
else:
    print(False)

# 检查特定值是否包含在列表中
requested_topping = ['mushrooms', 'onions', 'pineapple']
if 'mushrooms' in requested_topping:
    print(True)
else:
    print(False)

# 检查特定值是否不包含在列表中
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(user.title() + ", you can post a response if you wish.")

# 5-1练习
cars = ['audi', 'bmw', 'subaru', 'toyota']
car = 'subaru'
if car in cars:
    print("Is car == 'subaru'? I predict True.")
    print(car == 'subaru')
else:
    print("\nIs car == 'audi'? I predict False")
    print(car == 'audi')


""" if 语句 """

# 最简单的if语句
age = 19
if age >= 18:
    print("You are old enough to vote!")

# if-else语句
age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote!")
    print("Please register to vote as soon as you turn 18!")

# if-elif-else结构
# print("Please tell me your age!")
# age = int(input())
age = 12
if age < 4:
    print("Your admission cost is 0.")
elif age < 18:
    print("Your admission cost is 5.")
else:
    print("Your admission cost is 10.")

# print("Please tell me your age!")
# age = int(input())
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 5
else:
    price = 10

print("Your admission cost is " + str(price) + ".")

# 使用多个elif代码块
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
else:
    price = 6

print("Your admission cost is " + str(price) + ".")

# 省略else代码块
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
elif age >= 65:
    price = 6

print("Your admission cost is " + str(price) + ".")

# 5-3练习
alien_color = 'green'
if alien_color == 'green':
    print("You just earned 5 points!")

alien_color = 'red'
if alien_color == 'green':
    print("You just earned 5 points!")

# 5-4练习
alien_color = 'green'
if alien_color == 'green':
    print("You got 5 points")
else:
    print("You got 10 points")

# 5-5练习
alien_color = 'red'
if alien_color == 'green':
    print("You just earned 5 points!")
elif alien_color == 'yellow':
    print("You just earned 10 points!")
else:
    print("You just earned 15 points!")

# 5-6练习
age = 26
if age < 2:
    print("You're a baby!")
elif age < 4:
    print("You're a toddler!")
elif age < 13:
    print("You're a kid!")
elif age < 20:
    print("You're a teenager!")
elif age < 65:
    print("You're an adult!")
else:
    print("You're an elder!")

# 5-7练习
favorite_fruits = ['blueberries', 'salmonberries', 'peaches']
if 'bananas' in favorite_fruits:
    print("You really like bananas!")
if 'apples' in favorite_fruits:
    print("You really like apples!")
if 'blueberries' in favorite_fruits:
    print("You really like blueberries!")
if 'kiwis' in favorite_fruits:
    print("You really like kiwis!")
if 'peaches' in favorite_fruits:
    print("You really like peaches!")


""" if语句处理列表 """

# 检查特殊元素
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print("Add " + requested_topping + ".")
print("\nFinished making your pizza!")

# 确定列表不是空的
requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print("Add " + requested_topping + ".")
else:
    print("Are you sure you want a plain pizza?")

# 使用多个列表
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Add " + requested_topping + ".")
    else:
        print("Sorry, we don't have " + requested_topping + ".")
print("\nFinished making your pizza!")

# 5-8练习
usernames = ['eric', 'willie', 'admin', 'erin', 'ever']

for username in usernames:
    if username == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print("Hello " + username + ", thank you for logging in again!")

# 5-9练习
usernames = []
if usernames:
    for username in usernames:
        if username == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print("Hello " + username + ", thank you for logging in again!")
else:
    print("We need to find some users")

# 5-10练习
current_users = ['eric', 'willie', 'admin', 'erin', 'Ever']
new_users = ['sarah', 'Willie', 'PHIL', 'ever', 'Iona']

current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print("Sorry " + new_user + ", that name is taken.")
    else:
        print("Great, " + new_user + " is still available.")

# 5-11练习
numbers = list(range(1,10))

for number in numbers:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    else:
        print(str(number) + "th")

