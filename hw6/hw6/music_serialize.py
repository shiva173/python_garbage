import json, pickle

my_favourite_group = {
'name': 'Г.М.О.',
'tracks': ['Последний месяц осени', 'Шапито'],
'Albums': [{'name': 'Делать панк-рок','year': 2016},
{'name': 'Шапито','year': 2014}]}

with open('group.pickle', 'wb') as f:
   group_pickle = pickle.dump(my_favourite_group, f)

with open('group.pickle', 'rb') as f:
    result = f.read()
    print('group.pickle=========================->', result)


with open('group.json', 'w', encoding='utf-8') as f:
    # serialize list in json and save file
    json_music = json.dump(my_favourite_group, f)


with open('group.json', 'rb') as f:
    result = f.read()
    print('group.json=========================->', result)
