# -*- coding：utf-8 -*-
# Author：wu 
# Time: 2018年8月27日 22:00

# 变量和简单的数据类型


"""变量"""
message = "Hello World"
print(message)

message = "Hello world 2"
print(message)


"""字符串"""
# 字符串的首字母大写
name = "ada lovelace"
print(name.title())
# 字符串长度
print(len(name))

# 字符串全部大写
name = "Ada Lovelace"
print(name.upper())

# 字符串全部小写
name = "Ada Lovelace"
print(name.lower())

# 2-3练习
name = "Eric"
print("Hello " + name + ", would you like to learn some Python today?")

# 2-6练习
famous_person = "Albert Einstein"
message = '"A person who never made a mistake never tried anything new."'
print(famous_person + " once said " + message)

# 2-7练习
name = "\tEric Matthes\n"

print("Unmodified:")
print(name)

print("\nUsing lstrip():")
print(name.lstrip())

print("\nUsing rstrip():")
print(name.rstrip())

print("\nUsing strip():")
print(name.strip())

# 2-9练习
favourite_number = 8
message = "My favourite number is "
print(message + str(favourite_number) + ".")