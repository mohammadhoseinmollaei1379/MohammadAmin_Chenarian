# # 1
# def numbers(n):
#     for i in range(n + 1):
#         yield i

# for num in numbers(10):
#     print(num)

# def even_numbers(n):
#     for i in range(n + 1):
#         if i % 2 == 0:
#             yield i










# # 2
# import sys

# list_nums = [i for i in range(100001)]
# gen_nums = (i for i in range(100001))

# print("List size:", sys.getsizeof(list_nums))
# print("Generator size:", sys.getsizeof(gen_nums))










# # 3
# print(*numbers(10))










# # 4
# first_half = [1, 2, 3]
# second_half = [5, 6, 7]
# combined = [*first_half, 4, *second_half]
# print(combined)










# # 5
# user_profile = {'name': 'Ali', 'age': 30}
# user_permissions = {'is_admin': False, 'can_post': True}
# merged = {**user_profile, **user_permissions}
# print(merged)










# # 6
# try:
#     age = int(input("سن خود را وارد کنید: "))
# except ValueError:
#     print("لطفاً فقط عدد وارد کنید.")










# # 7
# try:
#     a = float(input("عدد اول: "))
#     b = float(input("عدد دوم: "))
#     op = input("عملگر (+ - * /): ")
#     if op == '+':
#         print(a + b)
#     elif op == '-':
#         print(a - b)
#     elif op == '*':
#         print(a * b)
#     elif op == '/':
#         print(a / b)
# except ValueError:
#     print("ورودی باید عدد باشد.")
# except ZeroDivisionError:
#     print("تقسیم بر صفر مجاز نیست.")










# # 8
# filename = input("نام فایل: ")
# try:
#     f = open(filename, 'r')
# except FileNotFoundError:
#     print("فایل پیدا نشد.")
# else:
#     print(f.read())
#     f.close()










# # 9
# filename = input("نام فایل: ")
# try:
#     f = open(filename, 'r')
# except FileNotFoundError:
#     print("فایل پیدا نشد.")
# else:
#     print(f.read())
#     f.close()
# finally:
#     print("عملیات بررسی فایل به پایان رسید.")










# # 10
# def check_age(age):
#     if age < 0:
#         raise ValueError("سن نمی‌تواند منفی باشد.")
#     return age










# # 11
# f = open("data.txt", "r")
# print(f.read())
# f.close()










# # 12
# with open("data.txt", "r") as f:
#     print(f.read())










# # 13
# with open("source.txt", "r") as src, open("destination.txt", "w") as dst:
#     dst.write(src.read())










# # 14
# class Dog:
#     sound = "Woof!"
#     def bark(self):
#         print(self.sound)

# d = Dog()
# d.bark()










# # 15
# d = Dog()
# s = "hello"
# print(isinstance(d, Dog))
# print(isinstance(s, Dog))










# # 16
# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age










# # 17
# class Dog:
#     species = "Canis familiaris"
#     def __init__(self, name):
#         self.name = name

# d = Dog("Bobby")
# print(d.name)
# print(d.species)










# # 18
# Dog.species = "New Species"
# d.species = "Changed via instance"
# print(Dog.species)
# print(d.species)










# # 19
# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     @classmethod
#     def from_birth_year(cls, birth_year):
#         return cls("Rex", 2025 - birth_year)

# d = Dog.from_birth_year(2020)
# print(d.name, d.age)










# # 20
# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __str__(self):
#         return f"سگی به نام {self.name} که {self.age} سال دارد"

# d = Dog("بادی", 3)
# print(d)










# # 21
# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __eq__(self, other):
#         return self.age == other.age

#     def __gt__(self, other):
#         return self.age > other.age

# d1 = Dog("A", 5)
# d2 = Dog("B", 3)
# print(d1 == d2)
# print(d1 > d2)










# # 22
# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __add__(self, other):
#         return Dog(self.name + "-" + other.name, 0)

# d1 = Dog("Max", 4)
# d2 = Dog("Bella", 5)
# puppy = d1 + d2
# print(puppy.name, puppy.age)










# # 23
# class tagCloud:
#     def __init__(self):
#         self.tags = {}


#     def add(self, tag):
#         self.tags{tag} = self.get(tag, 0) + 1   








# # 24
#     def __getitem__(self, tag):
#         return self.tags.get(tag, 0)










# # 25
#     def __setitem__(self, tag, count):
#         self.tags[tag] = count










# # 26
#     def __len__(self):
#         return len(self.tags)










# # 27
#     def __iter__(self):
#         return iter(self.tags.items())










# # 28
# class TagCloud:
#     def __init__(self):
#         self._tags = {}










# # 29
# import timeit

# print(timeit.timeit('[i**2 for i in range(1000)]', number=1000))
# print(timeit.timeit('result=[]\nfor i in range(1000): result.append(i**2)', number=1))







# # 30
# class FutureFeature:
#     pass










# # 31
# class InvalidOperationError(Exception):
#     pass

# raise InvalidOperationError("عملیات نامعتبر است.")










# # 32
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __add__(self, other):
#         return Point(self.x + other.x, self.y + other.y)










# # 33
# def read_lines(filename):
#     with open(filename, 'r') as f:
#         for line in f:
#             yield line










# # 34
# class Account:
#     def __init__(self):
#         self._balance = 0

#     def deposit(self, amount):
#         self._balance += amount

#     def withdraw(self, amount):
#         if amount > self._balance:
#             print("موجودی کافی نیست.")
#         else:
#             self._balance -= amount










# # 35
#     def __eq__(self, other):
#         if isinstance(other, Point):
#             return self.x == other.x and self.y == other.y
#         return False










# # 36
# class Circle:
#     def __init__(self, radius):
#         self._radius = radius

#     @property
#     def area(self):
#         return 3.14 * self._radius ** 2










# # 37
# import time

# class Timer:
#     def __enter__(self):
#         self.start = time.time()
#         return self

#     def __exit__(self, *args):
#         print("مدت زمان:", time.time() - self.start)










# 38
class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

class AddressBook:
    def __init__(self):
                

    def add(self, contact):
        self.contacts.append(contact)

    def remove(self, name):
        self.contacts = [c for c in self.contacts if c.name != name]

    def search(self, name):
        return [c for c in self.contacts if c.name == name]










# # 39
# def process_number(s):
#     try:
#         num = int(s)
#         try:
#             inverse = 1 / num
#             print(inverse)
#         except ZeroDivisionError:
#             print("تقسیم بر صفر!")
#     except ValueError:
#         print("ورودی عددی نیست.")










# # 40
# class Counter:
#     def __init__(self):
#         self.count = 0

#     def __call__(self):
#         self.count += 1
#         return self.count
# ```







