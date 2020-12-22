# Task 1-2
number=int(input('Введите число, которое будет больше 0, но меньше 10: '))

while not (0 < number < 10):
    number = int(input('Введите число, которое больше нуля, но меньше 10: '))

number **= 2
print(number)