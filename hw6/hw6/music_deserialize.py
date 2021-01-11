import json, pickle

with open('group.pickle', 'rb') as f:
    pickle_group = pickle.load(f)

print('group.pickle=========================->')
print(type(pickle_group), pickle_group)

with open('group.json', 'r') as f:
    # out file in json
    json_music = json.load(f)

print('group.json=========================->')
print(type(json_music), json_music)