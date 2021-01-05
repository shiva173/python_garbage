import pickle

person = {'name': 'Max', 'phones': [123, 345], 'age': 20}

with open('person.dat', 'wb') as f:
    pickle.dump(person, f)

print('Объект записан')

