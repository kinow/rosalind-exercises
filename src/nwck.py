from Bio import Phylo
from cStringIO import StringIO

if __name__ == '__main__':
	d = '''(cat)dog;
dog cat

(dog,cat);
dog cat'''
	i = 0
	tree = ''
	nodes = ''
	entries = list()
	for line in d.split('\n'):
		if i == 0:
			tree = line
			i += 1
		elif i == 1:
			nodes = line
			i += 1
			entries.append((tree, nodes))
		else:
			i = 0
	for entry in entries:
		handle = StringIO(entry[0])
		tree = Phylo.read(handle, "newick")
		a, b = entry[1].split(' ')
		print int(tree.distance(a, b)),

# from ete2 import Tree

# if __name__ == '__main__':
# 	t = Tree('((cat)dog);')
# 	print t
# 	#print t.get_distance('dog', 'cat')