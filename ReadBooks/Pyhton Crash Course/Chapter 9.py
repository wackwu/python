# -*- coding：utf-8 -*-
# Author：wu 
# Time: 2018年9月11日 14:00

# 类

""" 创建和使用类 """

# 创建Dog类
class Dog():
    # 模拟一次小狗的简单尝试
    def __init__(self, name, age):
        # 初始化属性name和age
        self.name = name
        self.age = age

    def sit(self):
        # 模拟小狗被命令时蹲下
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        # 模拟小狗被命令时打滚
        print(self.name.title() + " rolled over!")

# 根据类创建实例
my_dog = Dog('willie', 6)

print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")

# 调用方法
my_dog.sit()
my_dog.roll_over()

# 创建多个实例
my_dog = Dog('willie', 6)
your_dog = Dog('lucy', 3)

print("\nMy dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
my_dog.sit()

print("My dog's name is " + your_dog.name.title() + ".")
print("My dog is " + str(your_dog.age) + " years old.")
your_dog.sit()

# 9-1 练习
class Restaurant():
    """A class representing a restaurant."""

    def __init__(self, name, cuisine_type):
        """Initialize the restaurant."""
        self.name = name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Display a summary of the restaurant."""
        msg = self.name + " serves wonderful " + self.cuisine_type + "."
        print("\n" + msg)

    def open_restaurant(self):
        """Display a message that the restaurant is open."""
        msg = self.name + " is open. Come on in!"
        print("\n" + msg)

restaurant = Restaurant('the mean queen', 'pizza')
print(restaurant.name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()

# 9-2 练习
class Restaurant2():
    """A class representing a restaurant."""

    def __init__(self, name, cuisine_type):
        """Initialize the restaurant."""
        self.name = name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Display a summary of the restaurant."""
        msg = self.name + " serves wonderful " + self.cuisine_type + "."
        print("\n" + msg)

    def open_restaurant(self):
        """Display a message that the restaurant is open."""
        msg = self.name + " is open. Come on in!"
        print("\n" + msg)

mean_queen = Restaurant2('the mean queen', 'pizza')
mean_queen.describe_restaurant()

ludvigs = Restaurant2("ludvig's bistro", 'seafood')
ludvigs.describe_restaurant()

mango_thai = Restaurant2('mango thai', 'thai food')
mango_thai.describe_restaurant()

# 9-3 练习
class User():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describle_uesr(self):
        full_name = self.first_name.title() + self.last_name
        print(full_name)

    def greet_user(self):
        print("Hello," + self.first_name.title() + self.last_name)

name = User('wu', 'xuhao')
name.describle_uesr()
name.greet_user()


""" 使用类和实例 """

# Car类
class Car():
    # 一次模拟汽车的简单尝试

    def __init__(self, make, model, year):
        # 初始化描述汽车的属性
        self.make = make
        self.model = model
        self.year = year
    
    def get_descriptive_name(self):
        # 返回整洁的描述性信息
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

# 给属性指定默认值
class Car2():
    # 一次模拟汽车的简单尝试

    def __init__(self, make, model, year):
        # 初始化描述汽车的属性
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        # 返回整洁的描述性信息
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        # 打印一条指出汽车里程的信息
        print("This car has " + str(self.odometer_reading) + " miles on it.")

my_new_car = Car2('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

# 直接修改属性的值
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

# 通过方法修改属性的值
class Car3():
    # 一次模拟汽车的简单尝试

    def __init__(self, make, model, year):
        # 初始化描述汽车的属性
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        # 返回整洁的描述性信息
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        # 打印一条指出汽车里程的信息
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        # 将里程表读数设置为指定的值，禁止将里程表读数往回调
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer")

my_new_car = Car3('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(23)
my_new_car.read_odometer()

my_new_car.update_odometer(10)
my_new_car.read_odometer()

# 通过方法对属性的值进行递增
class Car4():
    # 一次模拟汽车的简单尝试

    def __init__(self, make, model, year):
        # 初始化描述汽车的属性
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        # 返回整洁的描述性信息
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        # 打印一条指出汽车里程的信息
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        # 将里程表读数设置为指定的值，禁止将里程表读数往回调
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer")

    def increment_odometer(self, miles):
        self.odometer_reading = self.odometer_reading + miles

my_used_car = Car4('subaru', 'outback', 2013)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()

# 9-4 练习
class Restaurant3():
    """A class representing a restaurant."""

    def __init__(self, name, cuisine_type):
        """Initialize the restaurant."""
        self.name = name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Display a summary of the restaurant."""
        msg = self.name + " serves wonderful " + self.cuisine_type + "."
        print("\n" + msg)

    def open_restaurant(self):
        """Display a message that the restaurant is open."""
        msg = self.name + " is open. Come on in!"
        print("\n" + msg)

    def set_number_served(self, number_served):
        """Allow user to set the number of customers that have been served."""
        self.number_served = number_served

    def increment_number_served(self, additional_served):
        """Allow user to increment the number of customers served."""
        self.number_served += additional_served


restaurant = Restaurant3('the mean queen', 'pizza')
restaurant.describe_restaurant()

print("\nNumber served: " + str(restaurant.number_served))
restaurant.number_served = 430
print("Number served: " + str(restaurant.number_served))

restaurant.set_number_served(1257)
print("Number served: " + str(restaurant.number_served))

restaurant.increment_number_served(239)
print("Number served: " + str(restaurant.number_served))

# 9-5 练习
class User2():
    def __init__(self, first_name, last_name, login_attempts):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describle_uesr(self):
        full_name = self.first_name.title() + self.last_name
        print(full_name)

    def greet_user(self):
        print("Hello," + self.first_name.title() + self.last_name)

    def increment_login_attempts(self):
        self.login_attempts = self.login_attempts + 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0

name = User2('wu', 'xuhao', 0)
name.describle_uesr()
name.greet_user()

name.increment_login_attempts()
name.increment_login_attempts()
name.increment_login_attempts()
print(str(name.login_attempts))

name.reset_login_attempts()
print(str(name.login_attempts))


""" 继承 """

# 子类的方法__init__
class Car5():
    # 一次模拟汽车的简单尝试

    def __init__(self, make, model, year):
        # 初始化描述汽车的属性
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        # 返回整洁的描述性信息
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        # 打印一条指出汽车里程的信息
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        # 将里程表读数设置为指定的值，禁止将里程表读数往回调
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer")

    def increment_odometer(self, miles):
        self.odometer_reading = self.odometer_reading + miles


class ElectricCar(Car5):
    # 电动汽车的独特之处

    def __init__(self, make, model, year):
        # 初始化父类的属性
        super().__init__(make, model, year)

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())

# 给子类定义属性和方法
class ElectricCar2(Car5):
    # 电动汽车的独特之处

    def __init__(self, make, model, year):
        # 初始化父类的属性,再初始化电动汽车特有的属性
        super().__init__(make, model, year)
        self.battery_size = 70

    def describe_battery(self):
        # 打印一条描述电瓶容量的消息
        print("This car has a " + str(self.battery_size) + "-KWh battery")

my_tesla = ElectricCar2('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()

# 将实例用作属性
class Battery():

    def __init__(self, battery_size=70):
        self.battery_size = battery_size
    
    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-KWh battery")

    def get_range(self):
        # 打印一条消息，指出电瓶的续航里程
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "This car can go approximately " + str(range) + " miles on a full charge"
        print(message)

    def update_range(self):
        if self.battery_size == 60:
            self.battery_size == 85
            print("Upgraded the battery to 85 kWh.")
        else:
            print("The battery is already upgraded.")

    def increment_get_range(self, increment_get_range):
        self.battery_size = self.battery_size + increment_get_range

class ElectricCar3(Car5):
    # 电动汽车的独特之处

    def __init__(self, make, model, year):
        # 初始化父类的属性,再初始化电动汽车特有的属性
        super().__init__(make, model, year)
        self.battery = Battery()

my_tesla = ElectricCar3('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

my_tesla.battery.increment_get_range(15)
my_tesla.battery.get_range()

print("\nUpgrade the battery, and check it again:")
my_tesla.battery.update_range()
my_tesla.battery.describe_battery()

print("\nTry upgrading the battery a second time.")
my_tesla.battery.update_range()
my_tesla.battery.describe_battery()


# 9-6 练习
class IceCreamStand(Restaurant3):
    """Represent an ice cream stand."""

    def __init__(self, name, cuisine_type='ice_cream'):
        """Initialize an ice cream stand."""
        super().__init__(name, cuisine_type)
        self.flavors = []

    def show_flavors(self):
        """Display the flavors available."""
        print("\nWe have the following flavors available:")
        for flavor in self.flavors:
            print("- " + flavor.title())


big_one = IceCreamStand('The Big One')
big_one.flavors = ['vanilla', 'chocolate', 'black cherry']

big_one.describe_restaurant()
big_one.show_flavors()

# 9-7 练习
class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = []

    def show_privileges(self):
        print("\nPrivileges:")
        for privilege in self.privileges:
            print("- " + privilege)

name = Admin('wu', 'xuhao')
name.describle_uesr()
name.privileges = [
    'can reset passwords',
    'can moderate discussions',
    'can suspend accounts',
    ]
name.show_privileges()

# 9-8 练习
class User3():
    """Represent a simple user profile."""

    def __init__(self, first_name, last_name, username, email, location):
        """Initialize the user."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()
        self.login_attempts = 0

    def describe_user(self):
        """Display a summary of the user's information."""
        print("\n" + self.first_name + " " + self.last_name)
        print("  Username: " + self.username)
        print("  Email: " + self.email)
        print("  Location: " + self.location)

    def greet_user(self):
        """Display a personalized greeting to the user."""
        print("\nWelcome back, " + self.username + "!")

    def increment_login_attempts(self):
        """Increment the value of login_attempts."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset login_attempts to 0."""
        self.login_attempts = 0


class Admin2(User3):
    """A user with administrative privileges."""

    def __init__(self, first_name, last_name, username, email, location):
        """Initialize the admin."""
        super().__init__(first_name, last_name, username, email, location)

        # Initialize an empty set of privileges.
        self.privileges = Privileges()

class Privileges():
    """A class to store an admin's privileges."""

    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        print("\nPrivileges:")
        if self.privileges:
            for privilege in self.privileges:
                print("- " + privilege)
        else:
            print("- This user has no privileges.")


eric = Admin2('eric', 'matthes', 'e_matthes', 'e_matthes@example.com', 'alaska')
eric.describe_user()

eric.privileges.show_privileges()

print("\nAdding privileges...")
eric_privileges = [
    'can reset passwords',
    'can moderate discussions',
    'can suspend accounts',
    ]
eric.privileges.privileges = eric_privileges
eric.privileges.show_privileges()