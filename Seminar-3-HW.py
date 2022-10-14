import numpy as np
import os
os.system('cls')

# Задача 1 Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# *Пример:*
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

arr = np.random.randint(1, 10, 10)
print(arr)
sum = 0
for i in range(len(arr)):
    if i % 2 != 0:
        sum += arr[i]
        print(f'arr[{i}] = {arr[i]}')
print('-----')
print(f'Ответ: {sum}')
