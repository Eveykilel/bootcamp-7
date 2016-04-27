a = [10, 40, -9, 40, 60, 89]
'''
for i in a:
	print i

i = len(a)

while i >= 0:
	print a[i - 1]
	i -= 1
for index in range(len(a) - 1, -1, -1):
	print a[index]

b = [(2, 4), (5, 10), (6, 20), (50, 50)]
for values in b:
	print "x: {}, y: {}".format(*values)


x: 2, y: 4
x: 5, y: 10
'''
print "a[-1]: ", a[::-1]
