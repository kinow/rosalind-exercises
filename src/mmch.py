from fasta.Fasta import read_fasta
import itertools
import networkx as nx

# I'm sure there's some well-tested algorithm for that... but I just couldn't find it... then...
def search(matchings, g, idx, stack):
	node = g.nodes()[idx]
	for right in g.neighbors(node):
		edge = (node, right)
		if False == matchings[-1].has_node(right):
			stack.append(edge)
			matchings[-1].add_edge(*edge)
		if (idx + 1 < len(g.nodes())):
			search(matchings, g, idx +1, stack)
			if len(stack) > 0 and stack[-1] == edge:
				stack.pop()
				for i in xrange(0, len(stack)):
					edge = stack.pop()
					matchings[-1].add_edge(*edge)
		else: # last node
			matchings.append(nx.Graph())

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

	#print G.edges()

	matchings = list()
	matchings.append(nx.Graph())

	stack = list()
	search(matchings, G, 0, stack)

	i = 0
	ms = list()
	for g in matchings:
		if len(g.edges()) > 0:
			ms.append(g)

#	for g in ms:
#		print "MATCHING!"
#		print g.edges()

	print len(ms)

#	print list(itertools.combinations(sequence, 6))
