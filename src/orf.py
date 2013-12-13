codon_table = {
'TTT': 'F',
'CTT': 'L',
'ATT': 'I',
'GTT': 'V',
'TTC': 'F',
'CTC': 'L',
'ATC': 'I',
'GTC': 'V',
'TTA': 'L',
'CTA': 'L',
'ATA': 'I',
'GTA': 'V',
'TTG': 'L',
'CTG': 'L',
'ATG': 'M',
'GTG': 'V',
'TCT': 'S',
'CCT': 'P',
'ACT': 'T',
'GCT': 'A',
'TCC': 'S',
'CCC': 'P',
'ACC': 'T',
'GCC': 'A',
'TCA': 'S',
'CCA': 'P',
'ACA': 'T',
'GCA': 'A',
'TCG': 'S',
'CCG': 'P',
'ACG': 'T',
'GCG': 'A',
'TAT': 'Y',
'CAT': 'H',
'AAT': 'N',
'GAT': 'D',
'TAC': 'Y',
'CAC': 'H',
'AAC': 'N',
'GAC': 'D',
'TAA': 'Stop',
'CAA': 'Q',
'AAA': 'K',
'GAA': 'E',
'TAG': 'Stop',
'CAG': 'Q',
'AAG': 'K',
'GAG': 'E',
'TGT': 'C',
'CGT': 'R',
'AGT': 'S',
'GGT': 'G',
'TGC': 'C',
'CGC': 'R',
'AGC': 'S',
'GGC': 'G',
'TGA': 'Stop',
'CGA': 'R',
'AGA': 'R',
'GGA': 'G',
'TGG': 'W',
'CGG': 'R',
'AGG': 'R',
'GGG': 'G'
}

class Fasta:
    def __init__(self, name, sequence):
        self.name = name
        self.sequence = sequence

def read_fasta(text):
    items = []
    index = 0
    aninstance = None
    seq = ''
    name = ''
    for line in text.splitlines():
        if line.startswith(">"):
            if index >= 1:
                items.append(aninstance)
            index += 1
            name = line[1:]
            seq = ''
            aninstance = Fasta(name, seq)
        else:
            seq += line
            aninstance = Fasta(name, seq)

    items.append(aninstance)
    return items

def is_stop_codon(codon):
    return (codon == 'TAA' or codon == 'TAG' or codon == 'TGA')

if __name__ == '__main__':
    sequence = '''
>Rosalind_99
AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG
'''
    for i in read_fasta(sequence):
        seq = i.sequence

        start = 0
        end = len(seq)
        index = seq.find('ATG', start, end)
        start = index+3

        while (index > 0) :
            protein = 'M'
            seq = str(seq[start:end])
            codons = [seq[x:x+3] for x in range(0, len(seq), 3)]
            if (len(codons) == 0):
                break;
            for codon in codons:
                print codon, '->', codon_table[codon]
                if (is_stop_codon(codon)):
                    print protein
                    seq = str(seq[start:end])
                    print seq
                    index = seq.find('ATG', start, end)
                    print start
                    break
                else:
                    protein += codon_table[codon]
                    start += 3
#         codons = [seq[x:x+3] for x in range(0, len(seq), 3)]
#
#         for codon in codons:
#             print 'Processing codon', codon, '->', codon_table[codon]
#             if (is_start_codon(codon) and in_protein == False):
#                 print codon, 'is start'
#                 in_protein = True
#                 protein += codon_table[codon]
#             elif (is_stop_codon(codon) and in_protein == True):
#                 print codon, 'is end'
#                 in_protein = False
#                 print '#P: ', protein
#                 protein = ''
#                 continue
#             elif in_protein:
#                 protein += codon_table[codon]
#             else:
#                 continue
