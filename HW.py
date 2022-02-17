# strings
#
# 1)написати прогу яка вибирає зі введеної строки цифри і виводить їх через кому,
# наприклад:
# с введена строка
# st = 'as 23 fdfdg544 34'
# 2,3,5,4,4        #вивело в консолі.
# st = 'as 23 fdfdg544 34'
# l=[]
# for i in st:
#     if i.isnumeric():
#         l.append(i)
# print(','.join(l))

# #################################################################################
# 2)написати прогу яка вибирає зі введеної строки числа і виводить їх
# так як вони написані
# наприклад:
# st = 'as 23 fdfdg544 34'  # введена строка
# #   23, 544, 34              #вивело в консолі
# l = []
# n = ''
# for i in st:
#     if '0' <= i <= '9':
#         n += i
#     else:
#         if n != '':
#             l.append(n)
#             n = ''
# if n != '':
#     l.append(n)
#
# print(' ,'.join(l))

# #################################################################################
#
# list comprehension
#
# 1)есть строка:
# greeting = 'Hello, world'
# записать каждый символ в лист поменяв его на верхний регистр
# пример:
# ['H', 'E', 'L', 'L', 'O', ',', ' ', 'W', 'O', 'R', 'L', 'D']
#
# greeting = 'Hello, world'
# l=[]

# for i in greeting:
#     l.append(i.upper())
#
# print(l)

# 2) с диапазона от 0-50 записать в лист только не парные числа, при этом возвести их в квадрат
# пример:
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, ...]
#
l = [i ** 2 for i in range(50) if i % 2 != 0]

# print(l)

# function
#
# - створити функцію яка виводить ліст
# def listWriter(list):
#     print(list)
#
# listWriter(l)

# - створити функцію яка приймає три числа та виводить та повертає найменьше.
# def minFunc (a,b,c):
#     l=[a,b,c]
#     char = min(l)
#     print(char)
#     return char


# minNum = minFunc(14,82,63)
# print(minNum)

# - створити функцію яка приймає три числа та виводить та повертає найбільше.
# def maxFunc(a, b, c):
#     l = [a, b, c]
#     char = max(l)
#     print(char)
#     return char
#
#
# maxNum = maxFunc(14, 82, 63)
# print(maxNum)

# - створити функцію яка приймає будь-яку кількість чисел, повертає найменьше, а виводить найбільше
# def someFunc(*args):
#     print(max(args))
#     return min(args)
# minNum = someFunc(1,2,3,34,54,0.5)
# print(minNum)

# - створити функцію яка виводить ліст
# def someFunc(*args):
#      print(args)
#
# someFunc(l)


# - створити функцію яка повертає найбільше число з ліста
# def someFunc(args):
#     maxChar = max(args)
#     return maxChar
#
#
# maxNum = someFunc(l)
# print(maxNum)


# - створити функцію яка повертає найменьше число з ліста
# def someFunc(args):
#     minChar = min(args)
#     return minChar
#
# minNum = someFunc(l)
# print(minNum)


# - створити функцію яка приймає ліст чисел та складає значення елементів ліста та повертає його.
# def someFunc(args):
#     sum = 0
#     for i in args:
#         sum = sum + i
#     return sum
#
#
# sumNum = someFunc(l)
# print(sumNum)

# # - створити функцію яка приймає ліст чисел та повертає середнє арифметичне його значень.
# def someFunc(args):
#     sum = 0
#     for i in args:
#         sum = sum + i
#     return sum / len(args)
#
#
# char = someFunc(l)
# print(char)
#
# #################################################################################################
# 1)Дан лист:
# list = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]
#   - найти min число в листе
# minChar = min(list)
# print(minChar)

#   - удалить все дубликаты в листе
# newList = [i for i in list if list.count(i) <= 1]
# print(newList)

#   - заменить каждое четвертое значение на "Х"
# for i in list[4::4]:
#     list[list.index(i)] = 'X'
# print(list)

# 2)вывести на экран пустой квадрат из "*" сторона которого указана в переменой:
# side = 8
# i = side
# while i >= 1:
#     if i == side or i == 1:
#         j = side
#         while j > 0:
#                 print('*', end='')
#                 j -= 1
#         print('')
#     else:
#         j = side - 2
#         print('*', end='')
#         while j > 0:
#             print(' ', end='')
#             j -= 1
#         print('*')
#     i -= 1

# 3) вывести табличку умножения с помощью цикла while

# i = 1
# while i <= 9:
#     j = 1
#     while j <= 9:
#         print(i * j, end='\t')
#         j = j + 1
#     print('')
#     i = i +1
# 4) переделать первое задание под меню с помощью цикла
# list = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]
# while True:
#     print("1. Найти min число в листе")
#     print("2. Удалить все дубликаты в листе")
#     print("3. Заменить каждое четвертое значение на 'X' ")
#
#     choise = int(input("Введите № задания от 1 до 3: "))
#     if choise == 1:
#         print("1.Найти min число в листе")
#         print(min(list))
#     elif choise == 2:
#         newList = [i for i in list if list.count(i) <= 1]
#         print(newList)
#     elif choise == 3:
#         print("3. Заменить каждое четвертое значение на 'X'" )
#         for i in list[4::4]:
#             list[list.index(i)] = 'X'
#         print(list)
#     else:
#         print("Нет такого пункта")
#     break
#
# ***  - вывести элемент листа, значение которого ближе всего к среднему арифметическому всех элементов этого же листа
# пример:
# [1, 2, 3, 4, 5, 6, 7, 8, 9] => 5
# [-1, -2, 3, 4, 555] => 4
# [5, 5, 5, 5] => 5
# [-10, 5, 5] => 5
