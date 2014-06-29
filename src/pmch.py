#!/usr/bin/python

from math import factorial

if __name__ == '__main__':

	data = 'CCUGGCAACAAGGAUCCCUUUUUCGCGUUGGUUCACCAAGUUCUAUACAAAUCUGUAAUAGAAGGGGCUGACGA'

	As = 0
	Cs = 0

	for c in data:
		if (c == 'A' or c == 'U'):
			As = As + 1
		else:
			Cs = Cs + 1


	Asfact = factorial(As/2)
	Csfact = factorial(Cs/2)

	print Asfact * Csfact