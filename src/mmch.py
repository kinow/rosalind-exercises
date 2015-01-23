from fasta.Fasta import read_fasta
import itertools
import networkx as nx

# I'm sure there's some well-tested algorithm for that... but I just couldn't find it... then...
def search(matchings, g, node, idx, stack):
	for right in g.neighbors(node):
		if matchings[-1].has_node(right):
			#if (idx + 1 < len(g.nodes())):
			#	idx = idx + 1
			#	search(matchings, g, g.nodes()[idx], idx)
			next
		else:
			edge = (node, right)
			stack.append(edge)
			matchings[-1].add_edge(*edge)
		if (idx + 1 < len(g.nodes())):
			idx = idx + 1
			search(matchings, g, g.nodes()[idx], idx, stack)
		else:
			if len(stack) > 0:
				stack.pop()
			matchings.append(nx.Graph())
			for i in xrange(0, len(stack)):
				edge = stack.pop()
				matchings[-1].add_edge(*edge)
			if len(matchings[-1]) > 0:
				print "Stack leftover"
				print matchings[-1].edges()

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
	matchings.append(nx.Graph())

	seed = G.nodes()[0] # initial node
	stack = list()
	search(matchings, G, seed, 0, stack)

	i = 0
	ms = list()
	for g in matchings:
		if len(g.edges()) > 0:
			ms.append(g)

	for g in ms:
		print "MATCHING!"
		print g.edges()

	print len(ms)

#	print list(itertools.combinations(sequence, 6))
