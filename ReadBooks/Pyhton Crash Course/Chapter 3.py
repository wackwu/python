# -*- coding：utf-8 -*-
# Author：wu 
# Time: 2018年8月28日 20:30

# 列表简介


"""列表"""
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

# 访问列表元素
print(bicycles[0]) # 正数第一个
print(bicycles[0].title())

print(bicycles[1]) # 正数第二个
print(bicycles[3]) # 正数第四个
print(bicycles[-1]) # 倒数第一个

message = "My first bicyle was a " + bicycles[0].title() + "."
print(message)

# 3-1练习
names = ['fanjun', 'wuxuhao', 'wackwu', 'lvjie']
print(names[0].title())
print(names[1].title())
print(names[2].title())
print(names[3].title())

# 3-2练习
message1 = "Hello my friend " + names[0].title() + '.'
print(message1)

message2 = "Hello my friend " + names[1].title() + '.'
print(message2)

message3 = "Hello my friend " + names[2].title() + '.'
print(message3)

message4 = "Hello my friend " + names[3].title() + '.'
print(message4)


"""修改、添加和删除元素"""

# 修改列表元素
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

# 列表末尾添加元素
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

# 列表中插入元素
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati') # 在正数第一个位置插入
print(motorcycles)

# 从列表中删除，使用del语句
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

del motorcycles[0] # 删除正数第一个值
print(motorcycles)

# 从列表中删除，使用pop()方法
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

poped_motorcycle = motorcycles.pop()
print(motorcycles)
print(poped_motorcycle)

poped_motorcycle = motorcycles.pop(0) # 删除正数第一个值
print(motorcycles)
print(poped_motorcycle)

# 根据值删除元素
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)

# 3-4练习
dinner_list = ['mayun', 'mahuateng', 'liyanhong']
print(dinner_list)

# 3-5练习
dinner_list = ['mayun', 'mahuateng', 'liyanhong']
message5 = "People " + dinner_list[2] + " can not come."
print(message5)

dinner_list[2] = 'likaifu'
print(dinner_list)

message6 = "Hello " + dinner_list[0].title() + ", thanks for coming"
print(message6)

# 3-6练习
print("\nWe got a bigger table!")
dinner_list.insert(0, 'leijun')
dinner_list.insert(2, 'yuminhong')
dinner_list.append('dongmingzhu')
print(dinner_list)

# 3-7练习
print("\nSorry, we can only invite two people to dinner.")

name = dinner_list.pop()
print("Sorry " + name.title() + "you can't come for the dinner")

name = dinner_list.pop()
print("Sorry " + name.title() + "you can't come for the dinner")

name = dinner_list.pop()
print("Sorry " + name.title() + "you can't come for the dinner")

name = dinner_list.pop()
print("Sorry " + name.title() + "you can't come for the dinner")
print(dinner_list)

name = dinner_list[0].title()
print(name + ", please come to dinner")
name = dinner_list[1].title()
print(name + ", please come to dinner")

del(dinner_list[0])
del(dinner_list[0])
print(dinner_list)


"""组织列表"""
# 使用sort()方法对列表进行永久性排序
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort() # 按照首字母正序排列,且不可改不变排序
print(cars)

cars.sort(reverse=True) # 按照首字母倒叙排列
print(cars)

# 使用sorted()函数对列表进行临时排序
cars = ['bmw', 'audi', 'toyota', 'subaru']

print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))# 按照首字母正序排列,可改变排序，临时排序

print("\nHere is the original list again:")
print(cars)

# 倒着打印列表
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

cars.reverse()
print(cars)

# 确定列表长度
length = len(cars)
print(length)

# 3-8练习
travel = ['shanghai', 'yunnan', 'usa', 'lasa', 'xian']
print(travel)
print(sorted(travel))
print(travel)
print(sorted(travel, reverse=True))
print(travel)

travel.reverse()
print(travel)
travel.reverse()
print(travel)

travel.sort()
print(travel)

travel.sort(reverse=True)
print(travel)

# 3-9练习
length = len(dinner_list)
print(length)
