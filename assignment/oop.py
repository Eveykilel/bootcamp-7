class Emloye:
	"""Common base class  Emloyee"""
	empCount = 0
	def __init__(self, name, salary):
		self.name = name
		self.salary = salary
		Emloyee.empCount += 1

	def displayCount(self):
		print "Name : ", self.name, "Salary : ", self.salary