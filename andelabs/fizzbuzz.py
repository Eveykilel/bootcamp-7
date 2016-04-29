def fizz_buzz(x):
	if x%3 == 0 and x%5 == 0:
		return "Fizz Buzz"
	elif x%3 == 0:
		return "Fizz"
	elif x%5 == 0:
		return "Buzz"
	else:
		return x
		
print fizz_buzz(3)
print fizz_buzz(5)
print fizz_buzz(9)
print fizz_buzz(15)