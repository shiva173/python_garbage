#trinarniu operator

is_has_name = False
name = 'Max' if is_has_name else 'Empty'
print(name)

is_one = True
number = 1 if is_one else 2
print(number)

is_russian = True
print('Привет' if is_russian else 'Hello')

word = 'слово'
result = []

for i in range(len(word)):
        letter = word[i]
        letter = letter.lower() if i%2 != 0 else letter.upper()
        result.append(letter)

result = ''.join(result)
print(result)


password = input('Введите пароль: ')
print('Войти' if password == 'secret' else 'Вход запрещен')

#generation lists and dickts

numbers = [1, 2, 3, 4, 5, -1, -2, -3]

result = []

for number in numbers:
    if number > 0:
        result.append(number)

print(result)


result = filter(lambda number: number > 0, numbers)
print(list(result))

result = [number for number in numbers if number > 0]
print(result)

pairs = [(1, 'a'), (2, 'b'), (3, 'e')]
result = {}
for pair in pairs:
    key = pair[0]
    val = pair[1]
    result[key] = val

print(result)

result = {pair[0]: pair[1] for pair in pairs}
print(result)

import random

numbers = [random.randint(1, 100) for i in range(10)]
print(numbers)


numbers = [1, 2, 3, -4]
numbers = [number**2 for number in numbers]
print(numbers)


names = ['Руслан', 'Алексей', 'Андрей']
names = [name for name in names if name.startswith('А')]
print(names)

s = 'abc'

if len(s) != 0:
    print('string')
else:
    print('empty string')


if s:
    print('another string s')
else:
    print('empty string')

l = [1, 2, 3]
d = {1: 'a'}

if l and d:
    print('not empty')
else:
    print('empty')

import math

if 1 > 2 and math.sqrt(-1):
    print('math error')
print('go next')

print([1] and [2] and '' and 1)
#========================================================>
numbers = [4, 1, 2, 3, -4, -2, 7, 16]

result = []

for number in numbers:
    if number > 0 and math.sqrt(number) < 2:
        result.append(number)

print(result)

result = []

for number in numbers:
    if number > 0 and math.sqrt(number) < 2:
        result.append(number)

print(result)

result = [number for number in numbers if number > 0 and math.sqrt(number) < 2]
print(result)
#=============================================>
def add_to_list(input_list=None):
    if input_list is None:
        input_list = []
    input_list.append(2)
    return  input_list

result = add_to_list([1, 2, 3])
print(result)
result = add_to_list()
print(result)


def add_to_list(input_list=None):
    input_list = input_list or []
    input_list.append(2)
    return  input_list

result = add_to_list([1, 2, 3])
print(result)
result = add_to_list()
print(result)
#================================================>

a = 1
b = a
b = 100
print(a, b)

a = [1, 2, 3]
b = a
b[1] = 100
print(b, a)

#====================================
numbers = [1, 2, 3]

def change_number_in_list(input_list):
    input_list[1] = 200

change_number_in_list(numbers)
print(numbers)

#=====================================

a = [1, 2, 3]
b = a[:]
b[1] = 200
print(a)

b = a.copy()
b[1] = 200
print(a)
# не учитывает вложенные списки
# для глубокого копирования списков включая вложенные
import copy

a = [1, 2, [1, 2]]
b = copy.deepcopy(a)
b[2][1] = 200
print(a, b)