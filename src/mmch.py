from fasta.Fasta import read_fasta
import itertools

if __name__ == '__main__':
	data = '''
>Rosalind_92
AUGCUUC
'''

	seqs = read_fasta(data)

	max_mat = 0

	elems = dict()

	for s in seqs:
		sequence = s.sequence
        for i in xrange(0, len(sequence)):
        	for j in xrange(0, len(sequence)):
        		if (i != j):
        			left = sequence[i]
        			right = sequence[j]
        			if (left == 'A' and right == 'U' or \
        				left == 'U' and right == 'A' or \
        				left == 'C' and right == 'G' or \
        				left == 'G' and right == 'C'):
	        			d = dict()
	        			d[i] = j
	        			if (i in elems):
				    		elems[i].append(d)
				    	else:
				    		elems[i] = list()
				    		elems[i].append(d)

	print elems

#	print list(itertools.combinations(sequence, 6))
