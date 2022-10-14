from unittest import result
import numpy as np
import random
import os
os.system('cls')

# Задача 1 Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# *Пример:*
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# arr = np.random.randint(1, 10, 10)
# print(arr)
# sum = 0
# for i in range(len(arr)):
#     if i % 2 != 0:
#         sum += arr[i]
#         print(f'arr[{i}] = {arr[i]}')
# print('-----')
# print(f'Ответ: {sum}')


# Задача 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# *Пример:*
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# arr = np.random.randint(1, 10, 5)
# length = len(arr)
# result = []
# for i in range(length):
#     while i < length/2 and length > length/2:
#         length = length - 1
#         mult = arr[i] * arr[length]
#         result.append(mult)
#         i += 1
# print(arr)
# print(result)


# Задача 3. Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между
# максимальным и минимальным значением дробной части элементов.
# *Пример:*
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# arr = np.random.random_sample(size=4)
# arr2 = [round(i % 1, 2) for i in arr if i % 1 != 0]
# print(arr)
# print(arr2)
# print(max(arr2) - min(arr2))
