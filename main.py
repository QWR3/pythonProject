# strings
#
# 1)написати прогу яка вибирає зі введеної строки цифри і виводить їх через кому,
# наприклад:
# st = 'as 23 fdfdg544' введена строка
# 2,3,5,4,4        #вивело в консолі.


# st = input('string')
# l =[]
# i= 0
# while i < len(st):
#     if st[i:i+1].isdigit():
#         l.append(st[i:i+1])
#     i = i+1
# print(l)


# #################################################################################
# 2)написати прогу яка вибирає зі введеної строки числа і виводить їх
# так як вони написані
# наприклад:
#   st = 'as 23 fdfdg544 34' #введена строка
#   23, 544, 34              #вивело в консолі

# st = input('string:')
# l = ''
# for item in st:
#     if item.isdecimal():
#         l+=item
#     else:
#         l+=' '
#
# jj = ','.join(l.split())
# print(jj)
#


# #################################################################################
#
# list comprehension
#
# 1)есть строка:
# greeting = 'Hello, world'
# записать каждый символ в лист поменяв его на верхний регистр
# пример:
# ['H', 'E', 'L', 'L', 'O', ',', ' ', 'W', 'O', 'R', 'L', 'D']

# l ='Hello, world'
# i = 0
# li = []
# while i < len(l):
#     li.append(l[i].upper())
#     i = i+1
# print(li)

#
# 2) с диапазона от 0-50 записать в лист только не парные числа, при этом возвести их в квадрат
# пример:
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, ...]

# i= 0
# l =[]
# while i < 50:
#     if i % 2 != 0:
#         l.append(i**2   )
#     i =i+1
# print(l)


# function
#
# - створити функцію яка виводить ліст
# def function():
#     s = input('введіть щось:')
#     ns = s.split(' ')
#     print(ns)
# function()
# - створити функцію яка приймає три числа та виводить та повертає найменьше.


# def function():
#     a = float(input('first number : '))
#     b = float(input('second number : '))
#     c = float(input('third number : '))
#     l = [a,b,c]
#     print(round(min(l)))
#     return round(min(l))
#
# function()

# - створити функцію яка приймає три числа та виводить та повертає найбільше.

# def function():
#     a = float(input('first number : '))
#     b = float(input('second number : '))
#     c = float(input('third number : '))
#     l = [a,b,c]
#     print(round(max(l)))
#     return round(max(l))
# function()

# - створити функцію яка приймає будь-яку кількість чисел, повертає найменьше, а виводить найбільше

# def function():
#     s = input('введіть числа:')
#     ns = s.split(' ')
#     l = []
#     i = 0
#     while i< len(ns):
#         l.append(int(ns[i]))
#         i +=1
#     print(max(l))
#     return min(l)
#
# f = function()


# - створити функцію яка виводить ліст

# def function():
#     s = input('введіть щось:')
#     ns = s.split(' ')
#     print(ns)
# function()

# - створити функцію яка повертає найбільше число з ліста
# def function():
#     s = input('введіть щось:')
#     ns = s.split(' ')
#     l = []
#     i = 0
#     while i < len(ns):
#         if ns[i].isdigit():
#             l.append(int(ns[i]))
#         i +=1
#     print(max(l))
#     return max(l)
# function()

# - створити функцію яка повертає найменьше число з ліста
# def function():
#     s = input('введіть щось:')
#     ns = s.split(' ')
#     l = []
#     i = 0
#     while i < len(ns):
#         if ns[i].isdigit():
#             l.append(int(ns[i]))
#         i +=1
#     print(min(l))
#     return min(l)
# function()
# - створити функцію яка приймає ліст чисел та складає значення елементів ліста та повертає його.
# def function():
#     s =input('введіть щось:')
#     l = s.split(' ')
#     n = 0
#     for i in l:
#         n +=int(i)
#     print(n)
#     return n
# function()
# - створити функцію яка приймає ліст чисел та повертає середнє арифметичне його значень.\
# def function():
#     s =input('введіть щось:')
#     l = s.split(' ')
#     n = 0
#     for i in l:
#         n +=int(i)
#     result =round(n/len(l))
#     print(result)
#     return result
# function()
#
# decorators
# - є функція:
# def pr():
#     return 'Hello_boss_!!!'
#  написати декоратор до цієї функції, який замінює нижні підчеркування на пробіли і повертає це значення

# def decor(func):
#     def wrap():
#         # func.index('_')
#         return func().replace('_', ' ')
#     return wrap()
#
#
# @decor
# def task():
#     return 'Hello_boss_!!!'
#
#
# print(task)
