import math
import numpy as np
import os
os.system('cls')
# задача 1. Задайте натуральное число N.
# Напишите программу, которая составит список простых множителей числа N.

# num = int(input("Введите число: "))
# def primes(x):
#     i = 2
#     array = []
#     while i <= x:
#         if x % i == 0:
#             array.append(i)
#             x //= i
#             i = 2
#         else:
#             i += 1
#     return array
# print(primes(num))

# задача 2 . Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

# array = np.random.randint(0, 10, 10)
# print(f'Исходный массив: {array}')


# def getUniqueNum(arr):
#     newArray = []
#     for i in arr:
#         if i not in newArray:
#             newArray.append(i)
#     return newArray


# print(getUniqueNum(array))

# задача 4.
# Найдите корни квадратного уравнения, уравнение вводит через строку пользователь.
# например, 6*x^2+5*x+6=0 . Само собой, уравнение может и не иметь решения.
# Предусмотреть все варианты, сделать обработку исключений.


# print('Введите коэффициенты для уравнения')
# print('ax^2 + bx + c = 0:')
# a = float(input('a = '))
# b = float(input('b = '))
# c = float(input('c = '))


# if a != 0:
#     if b != 0 and c != 0:
#         D = b ** 2 - 4 * a * c
#         print(f'D = {D}')
#         if D < 0:
#             print('Нет корней')
#         elif D == 0:
#             print('1 корень')
#             x = -b / (2 * a)
#             print(f'x = %.2f' % x)
#         else:
#             print('2 корня')
#             x1 = (-b + math.sqrt(D)) / (2 * a)
#             x2 = (-b - math.sqrt(D)) / (2 * a)
#             print('x1 = %.2f \nx2 = %.2f' % (x1, x2))
#     elif b == 0 and c == 0:
#         print('Корень x = 0')
#     elif b == 0:
#         if -c / a < 0:
#             print('Нет корней')
#         else:
#             print('2 корня')
#             x1 = math.sqrt(-c / a)
#             x2 = -x1
#             print('x1 = %.2f \nx2 = %.2f' % (x1, x2))
#     else:
#         print('2 корня')
#         x1 = 0
#         x2 = -b / a
#         print('x1 = %.2f \nx2 = %.2f' % (x1, x2))
# else:
#     print('a=0 => уравнение линейное')
