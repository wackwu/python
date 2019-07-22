# -*- coding：utf-8 -*-
# Author：wu 
# Time: 2018年9月10日 10:00

# 函数


""" 定义函数 """

# 定义函数
def greet_user():
    """ 显示简单的问候语 """
    print("Hello!")

greet_user()

# 向函数传递信息
def greet_user1(username):
    print("Hello, " + username.title() + ".")

greet_user1("wuxuhao")

# 8-1 练习
def display_message():
    print("学习的是函数")

display_message()

# 8-2 练习
def favorite_book(title):
    print("One of my favorite books is " + title.title() + ".")

favorite_book("alice in wonderland")


""" 传递实参 """

# 位置实参
def describe_pet(animal_type, pet_name):
    """ 显示宠物的信息 """
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet("hamster", "harry")
    # 调用函数多次
describe_pet("dog", "willie")

# 关键字实参
def describe_pet1(animal_type, pet_name):
    """ 显示宠物的信息 """
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet1(animal_type = "hamster", pet_name = "harry")
describe_pet1(pet_name = "harry", animal_type = "hamster")

# 默认值
def describe_pet2(pet_name, animal_type = "dog"):
    """ 显示宠物的信息 """
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet2(pet_name = "willie")
describe_pet2(pet_name = "chu")

def describe_pet3(animal_type = "dog", pet_name = "harry"):
    """ 显示宠物的信息 """
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet3()
describe_pet3(pet_name = "willie") # 给实参后会修改默认值

# 等效的函数调用
def describe_pet4(pet_name, animal_type = "dog"):
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

  # 一条名为Willie的狗
describe_pet4("willie")
describe_pet4(pet_name = "wliile")

  # 一只名为Harry的仓鼠
describe_pet4("harry", "hamster")
describe_pet4(pet_name= "harry", animal_type= "hamster")
describe_pet4(animal_type= "hamster", pet_name= "harry")

# 8-3 练习
def make_shirt(size, message):
    """Summarize the shirt that's going to be made."""
    print("\nI'm going to make a " + size + " t-shirt.")
    print('It will say, "' + message + '"')

make_shirt('large', 'I love Python!')
make_shirt(message="Readability counts.", size='medium')

# 8-4 练习
def make_shirt2(size= "large", message= "I Love Python"):
    print("\nI'm going to make a " + size + " t-shirt.")
    print('It will say, "' + message + '"')
make_shirt2()
make_shirt2(size='medium')
make_shirt2('small', 'Programmers are loopy.')

# 8-5 练习
def describe_city(city, country='chile'):
    """Describe a city."""
    msg = city.title() + " is in " + country.title() + "."
    print(msg)

describe_city('santiago')
describe_city('reykjavik', 'iceland')
describe_city('punta arenas')



""" 返回值 """

# 返回简单值
def get_formatted_name(first_name, last_name):
    """ 返回整洁的姓名 """
    full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name("jimi", "hendrix")
print(musician)

# 让实参变成可选
def get_formatted_name1(first_name, middle_name, last_name):
    """ 返回整洁的姓名 """
    full_name = first_name + ' ' + middle_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name1('john', 'lee', 'hooker')
print(musician)

def get_formatted_name2(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name 
    return full_name.title()
musician = get_formatted_name2('jimi', 'hendrix')
print(musician)

musician = get_formatted_name2('john', 'hooker', 'lee')
print(musician)

# 返回字典
def build_person(first_name, last_name):
    """ 返回一个字典，其中包含有关一个人的信息 """
    person = {'first_name': first_name, 'lasr_name':last_name}
    return person

musician = build_person('jimi', 'hendrix')
print(musician)

def build_person1(first_name, last_name, age=''):
    person = {'first_name': first_name, 'lasr_name':last_name}
    if age:
        person['age'] = age
    return person
musician = build_person1('jimi', 'hendrix', age=27)
print(musician)

# 结合使用函数和while循环
def get_formatted_name3(first_name, last_name):
    """ 返回整洁的姓名 """
    full_name = first_name + ' ' + last_name
    return full_name.title()

  # 这是一个无限循环
while True:
    print("\nPlease tell me your name")
    print("(enter 'q' or 'Q' at any time to quit)")
    f_name = input("First name")
    if f_name == 'q' or 'Q':
        break
    l_name = input("Last name")
    if l_name == 'q' or 'Q':
        break

    formatted_name = get_formatted_name3(f_name, l_name)
    print("\nHello, " + formatted_name + "!")

# 8-6 练习
def city_country(city, country):
    """Return a string like 'Santiago, Chile'."""
    return(city.title() + ", " + country.title())

city = city_country('santiago', 'chile')
print(city)

city = city_country('ushuaia', 'argentina')
print(city)

city = city_country('longyearbyen', 'svalbard')
print(city)

# 8-7 练习
def make_album(artist, title, tracks=''):
    """Build a dictionary containing information about an album."""
    album_dict = {
        'artist': artist.title(),
        'title': title.title(),
        }
    if tracks:
        album_dict['tracks'] = tracks
    return album_dict

album = make_album('metallica', 'ride the lightning')
print(album)

album = make_album('beethoven', 'ninth symphony')
print(album)

album = make_album('willie nelson', 'red-headed stranger')
print(album)

album = make_album('iron maiden', 'piece of mind', tracks=8)
print(album)

# 8-8 练习
def make_album2(artist, title, tracks=0):
    """Build a dictionary containing information about an album."""
    album_dict = {
        'artist': artist.title(),
        'title': title.title(),
        }
    if tracks:
        album_dict['tracks'] = tracks
    return album_dict

# Prepare the prompts.
title_prompt = "\nWhat album are you thinking of? "
artist_prompt = "Who's the artist? "

# Let the user know how to quit.
print("Enter 'quit' at any time to stop.")

while True:
    title = input(title_prompt)
    if title == 'quit':
        break
    
    artist = input(artist_prompt)
    if artist == 'quit':
        break

    album = make_album2(artist, title)
    print(album)

print("\nThanks for responding!")



""" 传递列表 """

def greet_user2(names):
    """ 向列表中的每位用户都发出简单的问候 """
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)

username = ['hannah', 'ty', 'margot']
greet_user2(username)

# 在函数中修改列表
  # 首先创建一个列表，其中包含一些要打印的设计
urprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

  # 模拟打印每个设计，直到没有未打印的设计为止
  # 打印每个设计后，都将其移动到列表completed_models中
while urprinted_designs:
    current_design = urprinted_designs.pop()

    # 模拟根据设计制作3D打印模型的过程
    print("Printing model: " + current_design)
    completed_models.append(current_design)

  # 显示打印好的所有模型
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)


def print_models(urprinted_designs, completed_models):
    while urprinted_designs:
        current_design = urprinted_designs.pop()

        print("Printing model: " + current_design)
        completed_models.append(current_design)
def show_completed_models(completed_models):
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

urprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(urprinted_designs, completed_models)
show_completed_models(completed_models)

# 8-9 练习
def show_magicians(magicians):
    """Print the name of each magician in the list."""
    for magician in magicians:
        print(magician.title())

magicians = ['harry houdini', 'david blaine', 'teller']
show_magicians(magicians)

# 8-10 练习
def show_magicians2(magicians):
    """Print the name of each magician in the list."""
    for magician in magicians:
        print(magician)

def make_great(magicians):
    """Add 'the Great!' to each magician's name."""
    # Build a new list to hold the great musicians.
    great_magicians = []

    # Make each magician great, and add it to great_magicians.
    while magicians:
        magician = magicians.pop()
        great_magician = magician + ' the Great'
        great_magicians.append(great_magician)

    # Add the great magicians back into magicians.
    for great_magician in great_magicians:
        magicians.append(great_magician)

magicians = ['Harry Houdini', 'David Blaine', 'Teller']
show_magicians2(magicians)

print("\n")
make_great(magicians)
show_magicians2(magicians)

# 8-11 练习
def show_magicians3(magicians):
    """Print the name of each magician in the list."""
    for magician in magicians:
        print(magician)

def make_great3(magicians):
    """Add 'the Great!' to each magician's name."""
    # Build a new list to hold the great musicians.
    great_magicians = []

    # Make each magician great, and add it to great_magicians.
    while magicians:
        magician = magicians.pop()
        great_magician = magician + ' the Great'
        great_magicians.append(great_magician)

    # Add the great magicians back into magicians.
    for great_magician in great_magicians:
        magicians.append(great_magician)

    return magicians

magicians = ['Harry Houdini', 'David Blaine', 'Teller']
show_magicians3(magicians)

print("\nGreat magicians:")
great_magicians = make_great3(magicians[:])
show_magicians3(great_magicians)

print("\nOriginal magicians:")
show_magicians3(magicians)


""" 传递任意数量的实参 """
def make_pizza(*toppings):
    # 打印顾客点的所有配料
    print(toppings)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

def make_pizza2(*toppings):
    # 概述要制作的披萨
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

make_pizza2('pepperoni')
make_pizza2('mushrooms', 'green peppers', 'extra cheese')

# 结合使用位置实参和任意数量实参
def make_pizza3(size, *toppings):
    print("\nMake a " + str(size) + "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)
make_pizza3(16, 'pepperoni')
make_pizza3(12, 'mushrooms', 'green peppers', 'extra cheese')

# 使用任意数量的关键字实参
def build_profile(first, last, **user_info):
    # 创建一个字典，其中包含我们知道的有关用户的一切
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile
user_profile = build_profile('albert', 'einstein', location='princeton', filed='physics')
print(user_profile)

# 8-12 练习
def make_sandwich(*items):
    """Make a sandwich with the given items."""
    print("\nI'll make you a great sandwich:")
    for item in items:
        print("  ...adding " + item + " to your sandwich.")
    print("Your sandwich is ready!")

make_sandwich('roast beef', 'cheddar cheese', 'lettuce', 'honey dijon')
make_sandwich('turkey', 'apple slices', 'honey mustard')
make_sandwich('peanut butter', 'strawberry jam')

# 8-14 练习
def make_car(manufacturer, model, **options):
    """Make a dictionary representing a car."""
    car_dict = {
        'manufacturer': manufacturer.title(),
        'model': model.title(),
        }
    for option, value in options.items():
        car_dict[option] = value

    return car_dict

my_outback = make_car('subaru', 'outback', color='blue', tow_package=True)
print(my_outback)

my_accord = make_car('honda', 'accord', year=1991, color='white',
        headlights='popup')
print(my_accord)




