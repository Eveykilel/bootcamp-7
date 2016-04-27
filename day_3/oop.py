from person import Person
from kenya import Kenyan

#end of class		
p = Person('Joe', 23)
p2 = Person('Jane', 23)
p3 = Person('JAcky', 43)

print p.say_hello()

a = [('Jane', 23), ('Joe', 50),
		('Jackie', 34), ('Jacob', 23),
		('Jee', 18), ('Josh', 60)]
b = []

for name, age in a:
	person = Person(name, age)
	b.append(person)

print Person.people_count
print b

for people in b:
	print people.say_hello()

k = Kenyan('Miguna', 20)

k.probe(True)
print "Is {} corrupt {}?".format(k.name, k.is_corrupt())

print k.say_hello()




		