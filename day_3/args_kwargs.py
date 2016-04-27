def hello(name, age):
	'''
	Explains...
	'''
	if class_ != '':
		return "I am {}, {} y/o, and {} class_".format(name, age, class_)
	return "I am {}, amd I'm{}".format(name, age)
people =[
			("Jane", 23), 
			("Joe", 25), 
			("Brian", 60),
			 ("Betty", 45)
			]
for name, age in people:
	print hello(name, age)

for person in people:
	print hello(*person)
