from random import randint
import os
os.system('cls')


def playerInputValue(name):
    x = int(
        input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
    while x < 1 or x > 28:
        x = int(input(f"{name}, введите корректное количество конфет: "))
    return x


def botInputValue(total):
    k = randint(1, 29)
    while total-k <= 28 and total > 29:
        k = randint(1, 29)
    return k


def currentResults(name, k, counter, total):
    print(
        f"Ходил {name}, он взял {k}, теперь у него {counter}. Осталось на столе {total} конфет.")
    print('=======================')


player1 = input("Введите ваше имя: ")
player2 = "Bot"
total = 2021
step = randint(0, 2)
if step:
    print(f"Первый ходит {player1}")
else:
    print(f"Первый ходит {player2}")

counter1 = 0
counter2 = 0

while total > 28:
    if step:
        k = playerInputValue(player1)
        counter1 += k
        total -= k
        step = False
        currentResults(player1, k, counter1, total)
    else:
        k = botInputValue(total)
        counter2 += k
        total -= k
        step = True
        currentResults(player2, k, counter2, total)

if step:
    print(f"Выиграл {player1}")
else:
    print(f"Выиграл {player2}")
