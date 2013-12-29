# jellyfish count -m 4 -s 1000000 <input_file>
# jellyfish dump <result_file> > <test.out>

from itertools import product

if __name__ == '__main__':
    jellyfish_out = dict()
    index = 0
    with open('/home/kinow/Downloads/rosalind_kmer.out') as f:
        for line in f.readlines():
            line = line.strip()
            if (line == ''):
                continue
            if (index % 2 == 0):
                khmer = line[1:]
            else:
                jellyfish_out[line] = khmer
            index += 1

    n = ['A', 'C', 'G', 'T']
    c = [''.join(x) for x in product(n, repeat=4)]
    out = list()
    for entry in c:
        if (entry not in jellyfish_out.keys()):
            out.append(0)
        else:
            out.append(jellyfish_out.get(entry))

    for khmer_count in out:
        print khmer_count,

