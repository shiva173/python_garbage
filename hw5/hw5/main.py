from cadd import create_dirs, delete_dirs
import random_number

nums = [1, 2, 3, 4, 5]

create_dirs()
delete_dirs() # вызвать после вызова предыдущей

print(random_number.get_random(nums))
