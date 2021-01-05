import random

random_numbers = [random.randint(-50, 50) for i in range(20)]
print('random list: ',random_numbers)
result_list = [number for number in random_numbers if not number % 3 and number > 0 and number % 4]
print('Результат из random list: ',result_list)