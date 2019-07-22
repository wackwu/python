# -*- coding：utf-8 -*-
# Author：wu 
# Time: 2018年9月2日 19:00

# 操作列表


"""遍历整个列表"""

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    # print(magician)
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")
print("Thank you, everyone. That was a great magic show!")

# 4-1练习
favorite_pizzas = ['pepperoni', 'hawaiian', 'veggie']
for favorite_pizza in favorite_pizzas:
    print("I like " + favorite_pizza + " pizza")
print("\nI really love pizza!")

# 4-2练习
pets = ['dog', 'cat', 'mouse']
for pet in pets:
    print("A " + pet + " would make a great pet")
print("\nAny of these animals would make a great pet")


"""创建数值列表"""

# 使用函数range()
for values in range(1, 5):
    print(values)

# 使用range()创建数字列表
numbers = list(range(1, 6))
print(numbers)

even_numbers = list(range(2, 11, 2)) # 函数range()从2开始数，然后不断地增加2，直到达到或超过终值11
print(even_numbers)

squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square) # 等同 squares.append(value ** 2)
print(squares)

# 对数字列表执行简单的统计计算
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))

# 列表解析
squares = [value**2 for value in range(1, 11)]
print(squares)

# 4-3练习
for value in range(1, 21):
    print(value)

# 4-4练习
for value in range(1, 1000001):
     print(value)

# 4-5练习
value = list(range(1, 1000001))
print(min(value))
print(max(value))
print(sum(value))

# 4-6练习
even_numbers = list(range(1, 21, 2))
print(even_numbers)

# 4-7练习
even_numbers = list(range(3, 31, 3))
print(even_numbers)

# 4-8练习
squares = []
for value in range(1, 11):
    square = value ** 3
    squares.append(square)
for square in squares:
    print(square)

# 4-9练习
cubes = [number**3 for number in range(1,11)]

for cube in cubes:
    print(cube)


"""使用列表的一部分"""

# 切片
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[2:])
print(players[-3:])

# 遍历切片
players = ['charles', 'martina', 'michael', 'florence', 'eli']

print("Here are the first three players on my team:")
for player in players[:3]:
    print(player)

# 复制列表
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\n My freind's favorite foods are:")
print(friend_foods)

# 4-11练习
favorite_pizzas = ['pepperoni', 'hawaiian', 'veggie']
friend_pizzas = favorite_pizzas[:]

favorite_pizzas.append("meat lover's")
friend_pizzas.append('pesto')

print("My favorite pizzas are:")
for pizza in favorite_pizzas:
    print("- " + pizza)

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print("- " + pizza)


"""元组"""

# 定义元组
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# 遍历元组中的所有值
dimensions = (200, 50)
for dimension in dimensions:
    print(dimension)

# 修改元组数量
dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("Modified dimensions:")
for dimension in dimensions:
    print(dimension)

# 4-13练习
menu_items = (
    'rockfish sandwich', 'halibut nuggets', 'smoked salmon chowder',
    'salmon burger', 'crab cakes',
    )

print("You can choose from the following menu items:")
for item in menu_items:
    print("- " + item)

menu_items = (
    'rockfish sandwich', 'halibut nuggets', 'smoked salmon chowder',
    'black cod tips', 'king crab legs',
    )

print("\nOur menu has been updated.")
print("You can now choose from the following items:")
for item in menu_items:
    print("- " + item)
