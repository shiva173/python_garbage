import json

friends = [
    {'name': 'Max', 'age': 23, 'phones': [123, 234]},
    {'name': 'Leo', 'age': 33}
]

print(type(friends))

json_friends = json.dumps(friends)

print(json_friends)

print(type(json_friends))

friends = json.loads(json_friends)

print(friends)
print(type(friends))