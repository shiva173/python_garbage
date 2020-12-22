#Task 2-1
first_list = [3, 8, 5, 24, 13, 4]
second_list = [24, 5, 8, 3]


for i in second_list:
    if i in first_list:
        first_list.remove(i)

print(first_list)


# Вариант с преобразованием к множеству
# first_list = set(first_list)
# second_list = set(second_list)
#
# result = first_list - second_list
# result = list(result)
#
# print(result)
#

# print(first_list, second_list)





