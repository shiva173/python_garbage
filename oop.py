# class Car():
#     def exclaim(self):
#     	print("I'm a Car!")

# class Yugo(Car):
# # переопределение методов
#     def exclaim(self):
#     	print("I'm a Yugo! Much like a Car, but more Yugo-ish")
#     def need_a_push(self):
#     	print("Little help here ?")

# print(issubclass(Yugo, Car)) # проверяем, что Yugo подкласс базового класса Car

# give_me_a_car = Car()
# give_me_a_yugo = Yugo()

# give_me_a_car.exclaim()
# give_me_a_yugo.exclaim()

# give_me_a_yugo.need_a_push()



# class Person():
# 	# переопрделение метода инициализации(что то вроде конструктора)
# 	def __init__(self, name):
# 		self.name = name

# class MDPerson(Person):
# 	def __init__(self, name):
# 		self.name = "Doctor " + name

# class JDPerson(Person):
# 	def __init__(self, name):
# 		self.name = name + ", Esquire"

# # получаем помощь от своего родителя
# class EmailPerson(Person):
# 	def __init__(self, name, email):
# 		# используй super().__init__() кошда потомк делает что то по своему но все еще нуждается в родителе
# 		super().__init__(name)
# 		self.email = email

# bob = EmailPerson('Bob Frapples', 'bob@frapples.com')
# print(bob.name, bob.email)


# person = Person('first')
# doctor = MDPerson('doc')
# lawyer = JDPerson('lawyer')

# print(person.name)
# print(doctor.name)
# print(lawyer.name)

# множественное наследование наследник унаследует метод с одним и тем же именем или атрибут того родителя который указан первым
class Animal():
	def says(self):
		return 'I speak'


class Horse(Animal):
	def says(self):
		return 'Ygogo'

class Donkey(Animal):
	def says(self):
		return 'Hee-haw!'

class Mule(Donkey, Horse):
	pass

class Hinny(Horse, Donkey):
	pass

mule = Mule()
hinny = Hinny()
print(mule.says())
print(hinny.says())

# миксин или примесь вспомогальный родительский класс не будет иметь общих методов другого родителя
class PrettyMixin():
	def dump(self):
		import pprint
		pprint.pprint(vars(self))

class Thing(PrettyMixin):
	pass


t = Thing()
t.name = "vadim"
t.feauter = "ichor"
t.age = "older"
t.dump()


# декораторы нужны для расширения функционала функций
def document_it(func):
	def new_function(*args, **kwargs):
		print('Running function: ', func.__name__)
		print('Positional arguments: ', args)
		print('key words arguments: ', kwargs)
		result = func(*args, **kwargs)
		print('Result: ', result)
		return result
	return new_function

def add_ints(a, b):
	return a + b

add_ints(3, 5)

# создание декортора вручную
cooler_add_ints = document_it(add_ints)
cooler_add_ints(3, 5)
# или так 
@document_it
def add_ints(a, b):
	return a + b

add_ints(3, 5)