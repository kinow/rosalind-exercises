from fasta.Fasta import read_fasta
import itertools
import networkx as nx

def search(matchings, g, node, idx):
	for right in g.neighbors(node):
		if [node, right] in matchings or [right, node] in matchings:
			if (idx + 1 < len(g.nodes())):
				idx = idx + 1
				search(matchings, g, g.nodes()[idx], idx)
		matchings.append([node, right])
		if (idx + 1 < len(g.nodes())):
			idx = idx + 1
			search(matchings, g, g.nodes()[idx], idx)
	return matchings

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

	matchings = list()

	seed = G.nodes()[0] # initial node
	matchings = search(matchings, G, seed, 0)

	print matchings

	print len(matchings)

#	print list(itertools.combinations(sequence, 6))
