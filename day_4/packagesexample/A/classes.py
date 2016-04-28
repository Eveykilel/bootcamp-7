
class Animal(object):
	pass

class Person(object):
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def walk(self):
		return "I'm walking"

class Poacher(Person):

	def __init__(self, name, age, **kwargs):
		Person.__init__(self, name, age)
		self.gun = kwargs.get('gun', 'AK-47')
		self.loc = kwargs.get('loc', 'Nairobi')
		self.game_park = kwargs.get('game_park', 'Tsavo')
		self.fav = kwargs.get('fav', 'Elephant')

		#for args
		if args[0]


class Tourist(object):
	pass

p = Person('Jane', 23)
pc = Poacher('Joe', 45, gun='Rifle', fav='Elephant', loc='Mombasa')

print pc.name, pc.age, pc.guun

