#Task 4-1
def person(name, age, city):
    string = "{}, {} год(а), проживает в городе {}".format(name, age, city)
    return string

print(person('Leo', 34, 'Москва'))
