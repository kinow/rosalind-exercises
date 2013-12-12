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

def rname(dna):
    rna = ''
    for c in dna:
        if (c == 'T'):
            rna += 'U'
        else:
            rna += c
    return rna

def is_start_codon(codon):
    return codon == 'ATG'

def is_stop_codon(codon):
    return codon_table[codon] == 'Stop'

def compl(args):
    output = ''
    for c in args:
        if (c == 'A'):
            output += 'T'
        elif (c == 'T'):
            output += 'A'
        elif (c == 'C'):
            output += 'G'
        else:
            output += 'C'
    return output

if __name__ == '__main__':
    sequence = '''
>Rosalind_99
AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG
'''
    for i in read_fasta(sequence):
        seq = i.sequence
        codon = ''
        protein = ''
        in_protein = False
        for c in (seq):
            if (len(codon) == 3):
                if (is_start_codon(codon)):
                    print codon, 'is start'
                    in_protein = True
                    protein += codon_table[codon]
                elif (is_stop_codon(codon) and in_protein):
                    in_protein = False
                    protein = ''
                    codon = ''
                    continue
                elif in_protein:
                    protein += codon
                else:
                    continue
                codon = ''
            codon += c
