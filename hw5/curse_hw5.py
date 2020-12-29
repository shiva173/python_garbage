# подключение целиком import math
# импорт через псевдоним import math as mt
# импорт конкретных функций from math import sin, cos

# import math
# import random as rd
#
# print(math.sin(38))
#
# print(rd.randint(1, 10))


# from math import *
# from random import randint, randrange
# print(pi)
# print(sin(30))

# import math
# #1 найти длину окружности с определенным радиусом
# r = 100
# print(2*r*math.pi)
# #2 площадь окружности с определенным радиусом
# print((r**2)*math.pi)
# print((math.pow(r,2))*math.pi)
# #3  по координатам 2-х точек определить расстояние между ними
# x1=10
# y1=10
# x2=50
# y2=100
# l = math.sqrt((x1-x2)**2+(y1-y2)**2)
# print(l)
#
# #4 факториал числа 9
# print(math.factorial(9))

#1 загадать случайное число от 0 до 100
# from random import randint, choice, sample, shuffle
# print(randint(0, 100))
# #2 выбрать победителя в лотерее
# players = ['Max', 'Leo', 'Kate', 'Ron', 'Bill']
# print(choice(players))
# #3 выбрать трех победителей
# print(sample(players, 3))
# #4 перемешать карты в стопке
# cards = ['6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
# print(cards)
# shuffle(cards)
# print(cards)


# передача аргументов в скрипты
import sys, os
#
# for arg in sys.argv:
#     print(arg)
#     print(type(arg))

def ping():
    print('pong')

def hello(name):
    print('Hello', name)

def get_dir():
    print(os.listdir())

command = sys.argv[1]

if command == 'ping':
    ping()
elif command == 'list':
    get_dir()
elif command == 'name':
    name = sys.argv[2]
    hello(name)