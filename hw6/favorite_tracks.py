import json

favorite_tracks = [
    {'name': 'Вечная Любовь', 'artist': 'Аггата Кристи'},
    {'name': 'Angel', 'artist': 'Massive Attack'},
    {'name': 'Jaming', 'artist': 'Bob Marley'}
]

with open('tracks.json', 'w', encoding='utf-8') as f:
    json.dump(favorite_tracks, f)


with open('tracks.json', 'rb') as f:
    result = f.read()
    print(result)
    print(type(result))
    s = result.decode('utf-8')
    print(s)

print('Done!')