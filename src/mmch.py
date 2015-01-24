from fasta.Fasta import read_fasta
import networkx as nx
import time
import threading

#http://code.activestate.com/recipes/286222/
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

class Counter():

	def __init__(self, count):
		self.lock = threading.Lock()
		self.count = count
		
	def increment(self):
		with self.lock:
			self.count += 1

# I'm sure there's some well-tested algorithm for that... but I just couldn't find it... then...
def search(g, idx, nodes, counter):
	left = g.nodes()[idx]
	for right in g.neighbors(left):
		if right not in nodes: # if False == matchings[-1].has_node(right):
			nodes.append(left)
			nodes.append(right)
			# matchings[-1].add_edge(*edge) # adding a part of the matching
		if (idx + 1 < len(g.nodes())):
			search(g, idx +1, nodes, counter)
					# matchings[-1].add_edge(*edge) # adding a part of the matching
		else: # last node
			# matchings.append(nx.Graph())
			if len(nodes) > 0: # we've found a matching...
				counter.increment()
			del nodes[:]

if __name__ == '__main__':
	start_time = time.time()
	data = '''
>Rosalind_0976
CUAUCAUCGCGGUCACCUCG
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

	counter = Counter(0)
	
	left = G.nodes()[0]
	threads = list()
	for right in G.neighbors(left):
		nodes = list()
		nodes.append(left)
		nodes.append(right)
		t = threading.Thread(target=search, args = (G, 1, nodes, counter))
		t.daemon = True
		t.start()
		threads.append(t)
		#search(G, 1, nodes, counter)

	for t in threads:
		t.join()

	m3 = memory(m2)

	print m3

#	for g in ms:
#		print "MATCHING!"
#		print g.edges()

	print counter.count

#	print list(itertools.combinations(sequence, 6))
	print("--- %s seconds ---" % str(time.time() - start_time))
