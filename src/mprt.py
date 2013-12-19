from fasta.Fasta import read_fasta
from urllib import urlopen
import re

#damn regexes
le_regex_1 = '[N][^P][T][^P]'
le_regex_2 = '[N][^P][S][^P]'

if __name__ == '__main__':
    data = '''
P02725_GLP_PIG
P19835_BAL_HUMAN
O13188
P02760_HC_HUMAN
Q4FZD7
Q00001_RHGA_ASPAC
Q47A87
Q8R1Y2
A6NM15
P22457_FA7_BOVIN
P03415_VME1_CVMA5
P11171_41_HUMAN
'''
    for x in filter(None, data.split('\n')):
        url = 'http://www.uniprot.org/uniprot/' + x + '.fasta'
        fasta_content = urlopen(url).read()
        seq = read_fasta(fasta_content)
        indexes = list()
        s = seq[0].sequence
        matches = filter(None, list(re.finditer(le_regex_1, s)))
        if (len(matches) > 0):
            for m in matches:
                if m not in indexes:
                    indexes.append( m.start()+1)

        matches = filter(None, list(re.finditer(le_regex_2, s)))
        if (len(matches) > 0):
            for m in matches:
                if m not in indexes:
                    indexes.append( m.start()+1)

        if (len(indexes) > 0):
            print x
            indexes.sort()
            for index in indexes:
                print index,
            print
