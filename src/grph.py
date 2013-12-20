'''
Created on Dec 19, 2013

@author: kinow
'''
from fasta.Fasta import read_fasta

visited = dict()

def node_exists(left, right):
    return (left[2] in visited.keys() and right[1] in visited.values()) or (right[2] in visited.keys() and left[1] in visited.values())

if __name__ == '__main__':
    data = '''
>Rosalind_0498
AAATAAA
>Rosalind_2391
AAATTTT
>Rosalind_2323
TTTTCCC
>Rosalind_0442
AAATCCC
>Rosalind_5013
GGGTGGG
'''
    seqs = read_fasta(data)

    graph = list()

    for s in seqs:
        sequence = s.sequence
        name = s.name

        left = sequence[0:3]
        right = sequence[:3:-1]

        graph.append((sequence, left, right, name))

    for i in range(len(graph)):
        e = graph[i]
        for j in range(len(graph)):
            f = graph[j]
            if (e[3] == f[3]):
                continue
            if (node_exists(e,f) == False):
                if (e[2] == f[1]):
                    visited[e[3]] = f[3];

    print visited
    for key, value in visited:
        print key, value
