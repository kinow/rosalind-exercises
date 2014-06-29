import itertools
import math

if __name__ == '__main__':

	n = 929

	# First naive approach
	# for i in range(0, len(values)):
	# 	for subset in itertools.combinations(values, i+1):
	# 		subsets += 1

	# From python itertools.combinations doc
	# The number of items returned is n! / r! / (n-r)! when 0 <= r <= n or zero when r > n.
	subsets = 1
	for r in range(0, n):
		subsets += math.factorial(n) / math.factorial(r) / math.factorial(n-r)

	print subsets % 1000000