# def hello(name, age):
# 	'''
# 	Explains...
# 	'''
# 	if class_ != '':
# 		return "I am {}, {} y/o, and {} class_".format(name, age, class_)
# 	return "I am {}, amd I'm{}".format(name, age)
# people =[
# 			("Jane", 23), 
# 			("Joe", 25), 
# 			("Brian", 60),
# 			 ("Betty", 45)
# 			]
# for name, age in people:
# 	print hello(name, age)

# for person in people:
# 	print hello(*person)
def super_sum(*args):
	'''
	Takes in variable number of items,
	and returns the sum.
	e.g. super_sum(10, 20) = 30
		super_sum(10, 20, 40) = 70
		super_sum(1, 4, 5, 6, 7) = 23
	'''
	total = 0
	for i in args:
		total += i

	return total

print super_sum(10, 20)
print super_sum(1, 4, 5, 7)
a = [10, 40, 60]
print super_sum(*a)

	#args and kwargd
def hello_again(**kwargs):
	return "I'm {}, and I'm {}".format(kwargs['name'], ['age'])

print hello_again(name='Joe', age=20)
print hello_again(age=20, name='Jane')
other_people = [
		{'name': 'Joe', 'age': 98},
		{'name': 'Jone', 'age': 68},
		{'name': 'Trump', 'age': 39}
	]
for person in other_people:
	print hello_again(**person)

joe = {'name': 'Joe', 'age': 98}
print hello_again(**joe)
print hello_again(name='joe', age=98)