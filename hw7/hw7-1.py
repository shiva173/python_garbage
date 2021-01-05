box1 = ['apple', 'banana', 'watermelon']
box2 = ['strawberry', 'banana', 'apple']

result = [fruit for fruit in box1 if fruit in box2]
print(result)
