# def print_sep(sep, sep_len):
#     return sep * sep_len
#
# print(print_sep('^', 30))
# print(print_sep('*', 30))
# print(print_sep('^', 30))
#
# sep = print_sep('^', 10)
# text = 'hello {} Func {}'.format(sep, sep)
# print(text)



# def hello_max():
#     print('Hello', 'Max')
#
# hello_max()
#
#
# def hello(who):
#     print('Hello', who)
#
# hello('Leo')
# hello('Oleg')
#
#
# def greeting(say, who):
#     print(say, who)
#
# greeting('Hi','Vadim')
#

# def greeting(say, *args):
#     print(say, args)
#
# greeting('Hello', 'Leo')
# greeting('Hello', 'Leo', 'Max')
# greeting('Hello', 'Leo', 'Max', 'Kate')

def get_person(**kwargs):
    for k,v in kwargs.items():
        print(k, v)

get_person(name='Leo', age=20, has_car=True)

# numbers = []
#
# for i in range(3):
#     number = int(input('input number: '))
#     numbers.append(number)
#
# print(max(numbers))
# print(min(numbers))
# print(sum(numbers))

# numbers = [1, 5, 3, 7, 11]
#
# print(sorted(numbers, reverse=True))
#
# names = ['Max', 'Alex', 'Kate']
#
# print(sorted(names))
#
# cities = [('Moscow', 1000), ('Las-Vegas', 500), ('Berlin', 2000)]
# print(sorted(cities))
# print(cities[1])
#
# def by_count(city):
#     return city[1]
#
# print(sorted(cities, key=by_count))
#
# print(sorted(cities, key=lambda city: city[1]))


# numbers = (1, 2, 3, 4, 5, 6, 7, 8)
#
# def is_even(number):
#     return number % 2 == 0
#
# result = filter(is_even, numbers)
# print(result)
# result = list(result)
# print(result)
#
# names = ['Max', 'Leo', 'Kate']
# print(list(filter(lambda x: len(x)>3, names)))


# numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# print(list(map(lambda x: x**2, numbers)))
# print(list(map(lambda x: str(x), numbers)))