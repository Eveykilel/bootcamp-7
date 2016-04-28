a = [10, 40, -9, 40, 60, 89]

for i in a:
	print i

i = len(a)

while i >= 0:
	print a[i - 1]
	i -= 1
for index in range(len(a) - 1, -1, -1):
	print a[index]

b = [(2, 4), (5, 10), (6, 20), (50, 50)]
for x, y in b:
	print "x: {}, y: {}".format(x, y)

def card(x = '', y = '', z = ''):
	if x == False:
		return 'y: {}, z: {}'.format(y, z)
	elif y == False:
		return 'x: {}, z: {}'.format(x, z)
	elif z == False:
		return 'x: {}, y: {}'.format(x, y)
	return 'x: {}, y: {}, z: {}'.format(x, y, z)


f = [(10, 20, 30), (10, 40), (4, 5, 50)]
'''
x:10, y:20, z:40
x:10, y:40
x:4, y:5, z:50
'''
for i in f:
	print card(*i)