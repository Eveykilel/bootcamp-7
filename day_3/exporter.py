
#Global variables not good practise
people =[
	('Joe', 78),
	('Jane', 30),
	('Brian', 40)
	]

def super_sum(*args):
	return sum(args)

def hello_again(name, age):
	return "I am {} and {} years old".format(name, age)

def max_min(A):

	#Return max value - min value
	
	max_, min_ = A[0], A[0]

	for i in A:
		if i > max_:
			max_ = i
		elif i < min_:
			min_ = 1

	return max_ - min_