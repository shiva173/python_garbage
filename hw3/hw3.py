import random

min_number = 1
max_number = 100
result = None

while result != '=':
    number = random.randint(min_number, max_number)
    print(number)
    print(min_number, max_number)
    result = input('= > <')

    if result == '>':
        min_number = number + 1
    elif result == '<':
        max_number = number - 1

print('Машина победила')