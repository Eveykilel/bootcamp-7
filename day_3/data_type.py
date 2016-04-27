def data_type(x):
	'''
	Takes an argument, x:
		- For a integer, return x ** 2
		- For a float, return x/2
		- For a string, returns "hello" + x
		- For a boolean, return "boolean"
		- For a long, return string "long"
	'''

	if type(x) == int:
		return (x ** 2)
	elif type(x) == float:
		return (x/2)
	elif type(x) == str:
		return ("hello" + x)
	elif type(x) == bool:
		return ("boolean")
	elif type(x) == long:
		return "long"
	else:
		return "Invalid Input"
print data_type(7)		
print data_type(7.566)
print data_type("Evey")
print data_type(True)
print data_type(2 ** 256)
print data_type([10, 20, 30])	