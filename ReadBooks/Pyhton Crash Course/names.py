# -*- coding：utf-8 -*-
# Author：wu 
# Time: 2018年9月12日 17:10

# 测试代码

# 导入需要使用的相关模块
from name_function import get_formatted_name

print("Enter 'q' at any time to quit.")
while True:
    print("\nPlease give me a first name: ")
    first = input()
    if first == 'q':
        break
    print("\nPlease give me a last name: ")
    last = input()
    if last == 'q':
        break

    formatted_name = get_formatted_name(first, last)
    print("\tNeatly formatted name: " + formatted_name + ".")
    