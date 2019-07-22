# -*- coding：utf-8 -*-
# Author：wu 
# Time: 2018年9月12日 11:10

# 文件和异常

""" 从文件中读取数据 """

# 读取整个文件
file_path = '/Users/wuxuhao/Desktop/Python/ReadBooks/Pyhton Crash Course/files/pi_digits.txt'
with open(file_path) as file_object:
    contents = file_object.read()
    print(contents)
    print(contents.rstrip()) # 去除空行

# 逐行读取
with open(file_path) as file_object:
    for line in file_object:
        print(line)

# 创建一个包含文件各行内容的列表
with open(file_path) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

# 使用文件内容
with open(file_path) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.rstrip()

print(pi_string)
print(len(pi_string))

pi_string = ''
for line in lines:
    pi_string += line.strip() # 去除行里面的空格

print(pi_string)
print(len(pi_string))

# 访问包含一百万的大型文件
file_name = '/Users/wuxuhao/Desktop/Python/ReadBooks/Pyhton Crash Course/files/pi_million_digits.txt'
with open(file_name) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string[:52] + "...")
print(len(pi_string))

# 圆周率中包含你的生日吗
print("Enter 'quit' when you are finished.")
while True:
    print("Enter your birthday, in the form mmddyy: ")
    birthday = input()

    if birthday == 'quit':
        break
    elif birthday in pi_string:
        print("Your birthday appears in the first million digits of pi!")
    else:
        print("Your birthday does not appear in the first million digits of pi.")

# 10-1 练习
filename = '/Users/wuxuhao/Desktop/Python/ReadBooks/Pyhton Crash Course/files/learning_python.txt'

print("--- Reading in the entire file:")
with open(filename) as f:
    contents = f.read()
print(contents)

print("\n--- Looping over the lines:")
with open(filename) as f:
    for line in f:
        print(line.rstrip())

print("\n--- Storing the lines in a list:")
with open(filename) as f:
    lines = f.readlines()

for line in lines:
    print(line.rstrip())

# 10-2 练习
with open(filename) as f:
    contents = f.readlines()

for content in contents:
    content = content.rstrip()
    print(content.replace('Python','C')) 


""" 写入文件 """

# 写入空文件 + 写入多行
file_name = '/Users/wuxuhao/Desktop/Python/ReadBooks/Pyhton Crash Course/files/programming.txt'

with open(file_name, 'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")

# 附加到文件
with open(file_name, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")

# 10-3 练习
file_name = '/Users/wuxuhao/Desktop/Python/ReadBooks/Pyhton Crash Course/files/guest.txt'
print("Please tell me your name!")
name = input()
with open(file_name, 'w') as file_object:
    file_object.write(name)

# 10-4 练习
file_name = '/Users/wuxuhao/Desktop/Python/ReadBooks/Pyhton Crash Course/files/guest_book.txt'
print("Enter 'quit' when you are finished.")
while True:
    print("What is your name?")
    name = input()
    if name != 'quit':
        print("Welcome " + name)
        with open(file_name, 'a') as file_object:
            file_object.write(name + "\n")
    else:
        break

# 10-5 练习
filename = '/Users/wuxuhao/Desktop/Python/ReadBooks/Pyhton Crash Course/files/programming_poll.txt'

responses = []
while True:
    response = input("\nWhy do you like programming? ")
    responses.append(response)

    continue_poll = input("Would you like to let someone else respond? (y/n) ")
    if continue_poll != 'y':
        break

with open(filename, 'a') as f:
    for response in responses:
        f.write(response + "\n")
