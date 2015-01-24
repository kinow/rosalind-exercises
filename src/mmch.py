from fasta.Fasta import read_fasta
import networkx as nx

import os

_proc_status = '/proc/%d/status' % os.getpid()

_scale = {'kB': 1024.0, 'mB': 1024.0*1024.0,
          'KB': 1024.0, 'MB': 1024.0*1024.0}

def _VmB(VmKey):
    '''Private.
    '''
    global _proc_status, _scale
     # get pseudo file  /proc/<pid>/status
    try:
        t = open(_proc_status)
        v = t.read()
        t.close()
    except:
        return 0.0  # non-Linux?
     # get VmKey line e.g. 'VmRSS:  9999  kB\n ...'
    i = v.index(VmKey)
    v = v[i:].split(None, 3)  # whitespace
    if len(v) < 3:
        return 0.0  # invalid format?
     # convert Vm value to bytes
    return float(v[1]) * _scale[v[2]]


def memory(since=0.0):
    '''Return memory usage in bytes.
    '''
    return _VmB('VmSize:') - since


def resident(since=0.0):
    '''Return resident memory usage in bytes.
    '''
    return _VmB('VmRSS:') - since


def stacksize(since=0.0):
    '''Return stack size in bytes.
    '''
    return _VmB('VmStk:') - since

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
>Rosalind_0976
AUGCUUCA
'''

	seqs = read_fasta(data)

	G = nx.Graph()

	m0 = memory()
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
	m1 = memory(m0)

	print m1

	#print G.edges()

	m2 = memory(m1)
	matchings = list()
	matchings.append(nx.Graph())

	stack = list()
	search(matchings, G, 0, stack)

	m3 = memory(m2)

	print m3

#	for g in ms:
#		print "MATCHING!"
#		print g.edges()

	print len(matchings)

#	print list(itertools.combinations(sequence, 6))
