from fasta.Fasta import read_fasta
import itertools
import networkx as nx

if __name__ == '__main__':
	data = '''
>Rosalind_92
AUGCUUC
'''

	seqs = read_fasta(data)

	G = nx.Graph()

	for s in seqs:
		sequence = s.sequence
        for i in xrange(0, len(sequence)):
        	G.add_node(i)

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
	        			e = (i, j)
	        			G.add_edge(*e)

	print G.edges()

	matching = set([])
	edges = set([])
	for u,v in G.edges_iter():
		if (u,v) not in edges and (v,u) not in edges:
			matching.add((u,v))
			edges |= set(G.edges(u))
			edges |= set(G.edges(v))

	print matching

#	print list(itertools.combinations(sequence, 6))
