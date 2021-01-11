with open('person.dat', 'rb') as f:
    result = f.readlines()

person = {}

person['name'] = result[0].decode('utf-8').replace('\n', '')

phones = []

for bphone in result[1:]:
    phones.append(bphone.decode('utf-8').replace('\n', ''))

person['phones'] = phones

print(person)