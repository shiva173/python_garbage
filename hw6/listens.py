
# open file for write if file dont exist create file
#f = open('first.txt', 'w')
# open file for read if file don exist return error
#f = open('second.txt', 'r')

#f = open('first.txt', 'w')

#f.write('helo\n')
#f.write('helo\n')

#f.writelines(['hi\n', 'python\n'])

#f = open('first.txt', 'r')
#print(f.read())

#for line in f:
#    print(line.replace('\n', ''))

#print(f.readlines())

f = open('first.txt', 'r')

for line in f:
    print(line.replace('\n', ''))

f.close()

# чтение из файла и его автоматическое закрытие
with open('first.txt', 'r') as f:
    for line in f:
        print(line.replace('\n', ''))

print('end')

s = 'Hello world'
print(type(s))

sb = b'hello byte'
print(type(sb))


print(s[1:3])
print(sb[1:3])

for item in sb:
    print(item)


sb = b'Ad'

print(sb[0])

print(sb[1])

s = 'Hello world Мир'
sb = s.encode('utf-8')
print(sb)
print(type(sb))

s = sb.decode('utf-8')
print(s)
print(type(s))


with open('bytes.txt', 'wb') as f:
    f.write(b'Hello bytes')

with open('bytes.txt', 'r', encoding='ascii') as f:
    print(f.read())

with open('bytes.txt', 'wb') as f:
    str = 'Привет мир'
    f.write(str.encode('utf-8'))

with open('bytes.txt', 'r', encoding='utf-8') as f:
    print(f.read())


with open('bytes.txt', 'wb') as f:
    str = 'Привет Мир'
    f.write(str.encode('utf-8'))


with open('bytes.txt', 'w', encoding='utf-8') as f:
    f.write('Привет Мир')

with open('bytes.txt', 'rb') as f:
    result = f.read()
    print(result)
    print(type(result))
    s = result.decode('utf-8')
    print(s)


person = {'name': 'Max', 'phones': [123, 345]}

with open('person.dat', 'wb')as f:
    name = person['name']
    f.write(f'{name}\n'.encode('utf-8'))
    phones = person['phones']
    for phone in phones:
        f.write(f'{phone}\n'.encode('utf-8'))

print('объект записан')