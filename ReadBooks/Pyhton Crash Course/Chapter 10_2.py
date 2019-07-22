# -*- coding：utf-8 -*-
# Author：wu 
# Time: 2018年9月12日 16:10

# 文件和异常

# 导入需要使用的相关模块
import json

""" 存储数据 """

# 使用json.dump()和json.load()
numbers = [2, 3, 5, 7, 11, 13]

filename = '/Users/wuxuhao/Desktop/Python/ReadBooks/Pyhton Crash Course/files/numbers.json'
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)

with open(filename) as f_obj:
    numbers = json.load(f_obj)

print(numbers)

# 保存和读取用户生成的数据
print("What is your name? ")
username = input()

filename = '/Users/wuxuhao/Desktop/Python/ReadBooks/Pyhton Crash Course/files/username.json'
with open(filename, 'w') as f_obj:
    json.dump(username, f_obj)
    print("We'll remember you when you come back, " + username + "!")

with open(filename) as f_obj:
    username = json.load(f_obj)
    print("Welcome back, " + username + "!")

# 如果以前存储了用户就加载它，否则就提示用户输入用户名并存储它
try:
    with open(filename) as f_obj:
        username = json.load(f_obj)
except FileExistsError:
    username = input("What is your name?")
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
        print("We'll remember you when you come back, " + username + "!")
else:
    print("Welcome back, " + username + "!")

# 重构
def greet_user1():
    # 问候用户，并指出其名字
    filename = '/Users/wuxuhao/Desktop/Python/ReadBooks/Pyhton Crash Course/files/username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileExistsError:
        username = input("What is your name?")
        with open(filename, 'w') as f_obj:
            json.dump(username, f_obj)
            print("We'll remember you when you come back, " + username + "!")
    else:
        print("Welcome back, " + username + "!")
greet_user1()


def get_stored_username():
    # 如果存储了用户名，就获取它
    filename = '/Users/wuxuhao/Desktop/Python/ReadBooks/Pyhton Crash Course/files/username2.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileExistsError:
        return None
    else:
        return username

def get_new_username():
    # 提示用户输入用户名
    username = input("What is your name?")
    filename = '/Users/wuxuhao/Desktop/Python/ReadBooks/Pyhton Crash Course/files/username2.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username

def greet_user():
    # 问候用户，并指出其名字
    username = get_stored_username()
    if username:
        print("Welcome back, " + username + "!")
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + "!")

greet_user()