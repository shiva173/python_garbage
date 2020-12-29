#Task 2-3

first_list = [2, 3, 5, 2, 12, 8, 2, 12, 15]
second_list = []

print(first_list)

for i in range(len(first_list)):
    if first_list.count(first_list[i]) == 1:
        second_list.append(first_list[i])

print(second_list)

#count (возвращает количество раз, когда значение появляется в списке)