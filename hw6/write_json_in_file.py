import json

friends = [
    {'name': 'Max', 'age': 23, 'phones': [123, 234]},
    {'name': 'Leo', 'age': 33}
]

print(type(friends))

with open('friends.json', 'w') as f:
    # serialize list in json and save file
    json_friends = json.dump(friends, f)

with open('friends.json', 'r') as f:
    # out file in json
    friends = json.load(f)

print(friends)
print(type(friends))