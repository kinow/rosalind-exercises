'''
Created on Dec 25, 2013

@author: kinow
'''
from fasta.Fasta import read_fasta

if __name__ == '__main__':
    data = '''
>Rosalind_9712
GTGCCGCCTCAGACTTACAGGCACTGCCCGCGGCTCATCAGAGGGGTTGTTGCTAACGAT
AGAAGAATTACCTGGCTTGCCACGCGCCTGAGAACGGAAACCATTATATGCTGAGCACCC
GAGCTGTAAGGTTTCGCACTGCCAAACGCGAGGCGGCAAGGGAGGGTCTGTATCAGGGAC
AGAATAATCAAGGCGATCCGTCAAGACCGCCGCGTGAAGCGAGATCACTTCTGTTAGGTC
GAGGTCGTAACGCCTGGCTATGCTTATCGAGCCAAAAGCATCTTATAAGCAAGACACCTC
GTAATTCAAGCGCATGTCACTGCTCAATCGTGAGTTCATCTGTGAGAACGTTTTCGCCAA
CAGTGACTCTGAGGCCTAACGCCTCAATAAGTGAGAAGGTGACCCCGATACGACCCACCG
AAGTTAACATCAATAAGTATGTATTCATGAACACAAACTTCTCCTTGGTACGGCCATAGG
TACAATGGAAAGTAGTGATATTGGGATGGTGACCTCGGCGCCTACCCCTAGCCAGCCGGT
CATAAATTTTACAACCGCGCTACAGAGCCAGCGCTTGGGTGCTTCCCGTGCCTTTCAATT
ACGCGATTCATCTGGTCATATGGACGTATATTGGAGTTATGGGCAATATAGTTGTTCGCT
CTAGCCCGAAGATAAACACCACTCTTAAGTCATCGCAAACTACCTGACAGGGAGACCTTC
CCTCCACATCAGTCTAATGCATCGCAGCAACACAACCCGCCCGCGCTTATCTGGGAAATG
CTCGAAATGGGGGCATCTTTGAGCTC
>Rosalind_6280
AAGTAGATTACCCGTTCT
'''
    seqs = read_fasta(data)
    ref = str(seqs[0].sequence)
    substring = seqs[1].sequence
    indexes = list()
    i = 0
    for char in substring:
        i = ref.find(char, i) +1
        if (i >= 0):
            indexes.append(i)

    for x in indexes:
        print x,
