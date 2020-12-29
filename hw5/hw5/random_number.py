import random

def get_random(numbers):
    if len(numbers) == 0:
        return None
    num = random.choice(numbers)
    return num
