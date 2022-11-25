import re
from random import randint
import os
os.system('cls')

# Задача 1
# # Создайте программу для игры с конфетами человек против человека.
# # Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# # Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# # Все конфеты оппонента достаются сделавшему последний ход.
# # Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# # Делаем игру против бота


# def playerInputValue(name):
#     x = int(
#         input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
#     while x < 1 or x > 28:
#         x = int(input(f"{name}, введите корректное количество конфет: "))
#     return x


# def botInputValue(total):
#     k = randint(1, 29)
#     while total-k <= 28 and total > 29:
#         k = randint(1, 29)
#     return k


# def currentResults(name, k, counter, total):
#     print(
#         f"Ходил {name}, он взял {k}, теперь у него {counter}. Осталось на столе {total} конфет.")
#     print('=======================')


# player1 = input("Введите ваше имя: ")
# player2 = "Bot"
# total = 2021
# step = randint(0, 2)
# if step:
#     print(f"Первый ходит {player1}")
# else:
#     print(f"Первый ходит {player2}")

# counter1 = 0
# counter2 = 0

# while total > 28:
#     if step:
#         k = playerInputValue(player1)
#         counter1 += k
#         total -= k
#         step = False
#         currentResults(player1, k, counter1, total)
#     else:
#         k = botInputValue(total)
#         counter2 += k
#         total -= k
#         step = True
#         currentResults(player2, k, counter2, total)

# if step:
#     print(f"Выиграл {player1}")
# else:
#     print(f"Выиграл {player2}")

# ===============================================
# Задача 2
# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.


# def coding(txt):
#     count = 1
#     res = ''
#     for i in range(len(txt)-1):
#         if txt[i] == txt[i+1]:
#             count += 1
#         else:
#             res = res + str(count) + txt[i]
#             count = 1
#     if count > 1 or (txt[len(txt)-2] != txt[-1]):
#         res = res + str(count) + txt[-1]
#     return res


# def decoding(txt):
#     number = ''
#     res = ''
#     for i in range(len(txt)):
#         if not txt[i].isalpha():
#             number += txt[i]
#         else:
#             res = res + txt[i] * int(number)
#             number = ''
#     return res


# with open('text-1.txt', 'r') as f:
#     text = f.read()
#     print(text)
#     result = coding(text)
#     print(result)
#     print(decoding(coding(text)))
# with open("text-2.txt", "w") as r:
#     r.write(result)

# ===============================================
# Задача 3. Напишите программу, удаляющую из текста все слова, содержащие "абв".
# Функции FIND и COUNT юзать нельзя.

text = 'Опытабвный разработчабвик всабвегда посмоабвтрит направоабв и абвналево, дабваже есабвли переходабвит улиабвцу с абводносторонним дабввижением'
result = re.sub(r'абв', '', text)
print(result)
