from math import sqrt
import random

def magic(input_list):
    return [number if number < 0 else sqrt(number) for number in input_list]

random_numbers = [10, 20, 30, 40, 50]
print('Новый список если числа положительные: ', magic(random_numbers))
random_numbers = [-1, -2, -3, -4, -5]
print('Список если числа отрицательные', magic(random_numbers))
random_numbers = [-1, -2, -3, -4, 8, 9, 12, 16]
print('Список с отрицательными и положительными числами', magic(random_numbers))