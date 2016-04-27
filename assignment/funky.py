def funky(a, b):

	if type(a) == int and type(b) == int:
		print a + b
	elif type(a) == float and type(b) == float:
		print a + b
	elif type(a) == str or type(b) == str:
		print str(a) + str(b)
	elif type(a) == dict or type(b) == dict:
		c = dict(a.items() + b.items())
		print c 
	else:
		print "Mismatch of Code"

funky('h',7)
funky('g', 'h')
funky(5, 8)
funky(2.4, 2.3)
funky('cat', 'dogs')
funky({"name" : "Evey"}, {"email" : "eve.kilel@gmail.com"})

