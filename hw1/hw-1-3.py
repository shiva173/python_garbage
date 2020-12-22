# Task 1-3
name=input("Ваше имя: ")
last_name=input("Ваша фамилия: ")
age=int(input("Ваш возраст: "))
weight=int(input("Ваш вес: "))



if age < 30 and (weight <= 50 or weight <= 120):
    result = ", вы здоровы"

elif age > 30 and age < 40 and (weight < 50 or weight > 120):
    result = ", вам нужно заняться собой"

elif age > 40 and (weight < 50 or weight >= 120):
    result = ", все плохо, вам надо в больницу"

else:
    result = ", вы здоровы"

print(name, last_name + result)