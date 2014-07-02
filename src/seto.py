import sys

def printset(seto):
	sys.stdout.write('{')
	i = 1
	length = len(seto)
	for x in seto:
		sys.stdout.write(str(x))
		if (i != length):
			sys.stdout.write(', ')
		i += 1
	print '}'

if __name__ == '__main__':
	n = 10
	a = {1, 2, 3, 4, 5}
	b = {2, 8, 5, 10}
	u = set(range(1, n+1))

	printset(a | b)
	printset(a & b)
	printset(a - b)
	printset(b - a)
	printset(u - a)
	printset(u - b)

