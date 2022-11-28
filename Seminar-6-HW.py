import math
import os
os.system('cls')
# Задача 1. Создайте программу для игры в "Крестики-нолики".
'''
board = list(range(1, 10))
winsComb = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7),
            (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]


def drawBoard():
    print('-------------')
    for i in range(3):
        print('|', board[0+i*3], '|', board[1+i*3], '|', board[2+i*3], '|')
    print('-------------')


def takeInput(playerToken):
    while True:
        value = input(f'Куда поставить {playerToken} (от 1 до 9)? : ')
        if not (value in '123456789'):
            print('Ошибка. Введите число от 1 до 9')
            continue
        value = int(value)
        if str(board[value - 1]) in 'XO':
            print('Эта клетка уже занята')
            continue
        board[value - 1] = playerToken
        break


def checkWin():
    for each in winsComb:
        if (board[each[0] - 1]) == (board[each[1] - 1]) == (board[each[2] - 1]):
            return board[each[1] - 1]
    else:
        return False


def main():
    counter = 0
    while True:
        drawBoard()
        if counter % 2 == 0:
            takeInput('X')
        else:
            takeInput('O')
        if counter > 3:
            winner = checkWin()
            if winner:
                drawBoard()
                print(f'{winner} Выиграл!')
                break
        counter += 1
        if counter > 8:
            drawBoard()
            print('Ничья')
            break


main()
'''
# ===========================================================
# Задача 2. Напишите программу вычисления арифметического выражения заданного строкой.
# Используйте операции +,-,/,*. приоритет операций стандартный.
# *Пример:*
# 2+2 => 4;
# 1+2*3 => 7;
# 1-2*3 => -5;
# Добавьте возможность использования скобок, меняющих приоритет операций
# *Пример:*
# 1+2*3 => 7;
# (1+2)*3 => 9;


# ===========================================================
