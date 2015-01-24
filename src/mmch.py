from fasta.Fasta import read_fasta
import time

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

if __name__ == '__main__':
	start_time = time.time()
	data = '''
>Rosalind_92
AUGCUUC
'''

	m0 = memory()
	
	# le sequence
	sequence = read_fasta(data)[0].sequence
	
	au_count1, au_count2 = sorted([sequence.count('A'), sequence.count('U')])
	cg_count1, cg_count2 = sorted([sequence.count('C'), sequence.count('G')])
	
	matchings = 1
	for i in range(au_count1):
		matchings *= (au_count2 - i)
	for j in range(cg_count1):
		matchings *= (cg_count2 - j)
		
	print matchings

	m1 = memory(m0)

	print m1

#	print list(itertools.combinations(sequence, 6))
	print("--- %s seconds ---" % str(time.time() - start_time))
