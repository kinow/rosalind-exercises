import sys
import string
from fasta.Fasta import read_fasta

def hamming_distance(base_seq, ref_seq):    
    hd = 0
    
    for i in range(0, len(base_seq)):
        if (base_seq[i] != ref_seq[i]):
            hd += 1
            
    return hd

def compl(args):
    r = args[::-1]
    tbl = string.maketrans('ATGC', 'TACG')
    return r.translate(tbl)

if __name__ == '__main__':
    data = open("rosalind_corr.txt", 'r').read()
    fasta = read_fasta(data)

    #s was correctly sequenced and appears in the dataset at 
    #least twice (possibly as a reverse complement);
    counter = dict()
    for f in fasta:
        s = f.sequence
        if compl(s) in counter:
            counter[compl(s)] = (counter[compl(s)]+1)
        else:
            if (s in counter):
                counter[s] = (counter[s] + 1)
            else:
                counter[s] = 1

    correct = list()
    ambiguous = list()

    corrected = dict()

    for sequence, count in counter.iteritems():
        if count >= 2:
            correct.append(sequence)
        else:
            ambiguous.append(sequence)

    for error in ambiguous:
        for sequence in correct:
            if (hamming_distance(sequence, error) == 1):
                corrected[error] = sequence
                print error + "->" + sequence
                break
            if (hamming_distance(compl(sequence), error) == 1):
                corrected[error] = compl(sequence)
                print error + "->" + compl(sequence)
                break