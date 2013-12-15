from itertools import takewhile

codontable = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
    'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
    }

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

def translate_dna(sequence, stop_codons = ('TAA', 'TGA', 'TAG')):
    start = sequence.find('ATG')

    # Take sequence from the first start codon
    trimmed_sequence = sequence[start:]

    # Split it into triplets
    codons = [trimmed_sequence[i:i+3] for i in range(0, len(trimmed_sequence), 3)]

    found = False
    for c in codons:
        if (c in stop_codons):
            found = True

    if(False == found):
        return '', start

    # Take all codons until first stop codon
    coding_sequence  =  takewhile(lambda x: x not in stop_codons and len(x) == 3 , codons)

    # Translate and join into string
    protein_sequence = ''.join([codontable[codon] for codon in coding_sequence])

    # This line assumes there is always stop codon in the sequence
    return "{0}".format(protein_sequence), start

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

if __name__ == '__main__':
    sequence = '''
>Rosalind_6173
TTCTAAGGTCCCTCGTAAAGCAACAGGCCCGCAAACGGCGAACGCCCTAGGCCACCCTGA
AACGCTAACACCGACAACAATGTGCAGCCCGCGCCGGATCGCAAGCGTTGATTACACCAC
ACCGCGAAGCGATAAAAAAAGATGTTTAGCTCCCCCATCGGGCTCCTTGTGATCCGCGAC
GGACGCTTCTAGAGACCACCTTAGGCCAACTCAACCGGCGCGACCGCACCCGTTACTCCA
GTGTACTCTACAAATTCAAGTAGTTGTAAAGGGGGCATAAAAAGCGCAGTATCGCTCTGC
CGGTTGCACCTGCGATTGGCAAACGAGGCTGGCCCCGTGGATCGGTATTCCAAACTATGC
GTTTTGGGGCGGGCTCAACTCGGGAAAGACTTAGATAAGTTCTAGCGTTTATCGAGGGGG
CTCATGCTCTAACGTAGACATTAGCTAATGTCTACGTTAGAGCATCCTGACCACCATCCT
ACCGAGAGTAAGTATGGAACGTACACGCAGCTATGGATGGCATACCACTTAGTCCGGGAG
CTTTTTGGCTGATGCTTCGGCGGAGAGAGGTTGGGGAACGCGAATGAAACGCACTCTGTC
TGTGCAAAAAAAAGCAAACCGATCTGGAACCCGACGGATAGTAAAGGGTCGGGGGGTCGC
TCAGACCGCCTGCTAGGGTGTCATGCTCTACCATATGCCGCCGGGCTTTACGGAACCTGT
GCGTAGCGCAGCATGACGTTCAGTCGCAAGCCGTCCTTGTTACAAGTAGACAGCCCAACA
GGTAGCGTTAATCCTTTCTTCTTACATTTTACTAATAGGCTCCGTAGTATTCCTATGGTC
GTGCCCACATGTCCCACAATCATGTTGATGCATAGGACAGCTGGGATC
'''
    proteins = list()
    for i in read_fasta(sequence):
        seq = i.sequence
        while(True):
            out, start = translate_dna(seq)
            if (out != '' and out not in proteins):
                proteins.append(out)
            if (start == -1):
                break;
            seq = seq[start+3:len(seq)]
        #other frames
        seq = i.sequence
        seq = compl(seq)
        seq = seq[::-1]
        while(True):
            out, start = translate_dna(seq)
            if (out != '' and out not in proteins):
                proteins.append(out)
            if (start == -1):
                break;
            seq = seq[start+3:len(seq)]

        for p in proteins:
            print p