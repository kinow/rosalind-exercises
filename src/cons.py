from fasta.Fasta import read_fasta
import sys

if __name__ == '__main__':
    data = '''
>Rosalind_4592
>Rosalind_9829
TTAGACCATGCTGTTGTACTCCCCCCGTCATGGCAAAAATGACTCATTCGAGTCTTTCGC
ATGCGTCCACCCGGCTGTGGACTTGTCTGTTCGGCCTAGGCGTGACAAAGGTTAAAGTCA
TGTATACAGGATGCCGACCAAATGTAGAGCTACTCATTCCGTATAGCTTCTAAGCCACTA
ACGAGGATACGAAGTGTATAGATATCCTTAAAGCTGGCGTTTGTAGCCTAGTTCGGCTAG
CCGGCATTATAATAATGAGATAAATTACAGGTGATCGCCAAGGCTCATTTAGTTGTGTTC
TTCGCAACTTTCCGGACCTTCGCCCTAATAATTAAAGCGCAGAGCCGCCTCGTATAGGAG
ATTAGTTTTATGCGACCGGATCTCGTAAGAAAATTAGATCGGGAAATTGTTAAACTACAG
TACTTAATTCAGGTAATGACATTTCCGTCGTTTGTATCTTTATAATAGTATATGATCGCC
TATAGTTATAAGAGCGCGAACGACAGCTTACGCGTGGTTGCGATTATCGGGTTAGTCTTA
ACTCGGCCCAAATGAGAAGAATTCACGTGGTAAAGTGTCGGACTGATAGCGCACGCATTC
GGTGACTTCTGATAGGCGACCCAGTATCTACGTCTGCCTATTCTGCACAGCGTATATCCT
ATTCAACCTAGGGTTACGTCGCGAAAGCTATATGCCCACACGGCAAGGGTAGCTGCAAGG
TGATAAGGTTGTTTGATTTGCCTCATAGCTGAGAAGACCGACAGAGGCTGCCTACTGGCA
CGTACAAACCAAGGTAACGTATCTGTGGGACACTTCGATGGTTGTGTCTAACGCCTTGAG
ACGTACGATACAAAACGTAGCGGGATTCACATGCAGGTAGTTGAAGTGTGTTCGGAGCTA
>Rosalind_8886
ACCAGCTATAACGTCCTAGCGTACCCTGCTTTGGTTAAAACACGAAATTGTTACAGTTGA
CGTCCGCCACTACTACGTGGAATATACAACTAGCCGAGTAGCTAAGCACTGTTCGTATCA
TCGGAGGATCCTAGTCTTGTCCTCGCTCTACAAAGGCCAAAAAATGTGTGGCTAAATGGC
GTAGGGTGGCTTATTAGAACTCTATTCATTCTCTATACTAAACTGCACGTGCTACATGGT
CTCCACGCGGGGTTCCGATAGTCGCCGCGAGTCTACGATTGGTACGTCCAAAAACCGTGG
GAGCGGGGAATAAATTTGCGGAACAGCCGACCACTGCCTCAAACACGGCGGGTTGAAGCC
GGGGCGTAGCCCTGAGGCAGTCTTGGGGGCGAGTTCCGCGCCGAGACGTACTGTCTAAGT
CGGACTGGGTACATCAGCGTGCTAGACAATAGCAATCGTCCTATTGATTACCCAAGACCG
CTAAGATTTGGAATCAACACCCTATAGAGGCGTATTTGACGAACCAGGAGTAATAGTTGA
GCATCTATGGATACAATAACCGAGGCCTACTACAGAAAAGTGTCCTAGTTGAGTAATACG
GCGTAACTACTAAAGCCGTTCGTGCAGAAGAGGTCAAGTGTAACGGCTCACGAGCCCAGC
GATCAGCCTTAACTTCTACAATGTGCGAGATATGTTTCGAAGGCACATCGCTTGGCGGCC
TCGCATTTTCTTTCTCGTTTTGGACAAGGCAAACTCAGGATGATGTAGTCGGCTTAGCAA
AAACCATACACAGGGATCTAGCCGAATCGGTCCGGGTCTCAAACACTAGGCTACCAGAAT
CCCTTCGACTGAAGACTCGGTGCAAGCCTCTATGGTACGCATACTCGAAAGCAGATAATA
>Rosalind_8552
GATTCCCGGACACCCGTGCTACCGCACGCCTCTTGTAAGTCAGTTTTCCGCTGAGTGTGG
ATCCGCACGTGATCAGCTGCAGTCACGCCGCACAGTATGGTGTATCTAGGTTCAGACACT
ACAGGCTGCGGGGTGACCGGATTTAGCGTTATCCATAAACAGATAGCGGGTTATGATGCA
TGTTACCACTATGTATATCGGGCCGGGCAGCGATCTGTTAACGGTCGGTAAACTGATCGG
CCGCTAGACGTAGTCTTTAGTAGCGGATCCTGTTCACCCACAATACGACAGGTAGTGCTT
CTGAAGTTATATAGGGCAAATATTGTATGTGGCCGACCGGCACAGCATTGACACGACGTC
TTGTCTCCTGACATCAACCGATAGAAGCATGAGAAGATAGTTACGTTATGGCGAATAGGA
AGGTACGCACCGAAACCTTCCATGAGATGGATGCCCATGCTTCTCTATGGGCGTTCCGGG
GAGCTATGGACTACCGGGATTCAACAGGCACCAGACGTTGTGGCGGGACTGTCGTCCATT
GCCGTGAATCTGGACTTTTAGTTCTAAGTATGAAGCCGTCGGGTCTGTATATGGAATCTG
AAAATCCATAGAGATGGATCACTGTGTATTGTTACGGAGGACTGATTTTCCAAAGTTTAC
CTGGTTACAGACCGCCGGTGGCAATTTTGATTAAAGTGGGGTCTTGATCCTGGCTGTATA
CGTGCTAGCGTCTCTCGCGTACCCCGCTTGAGTCGCAACAGCCGCTACGTCAAGAGACGT
GGTCCTACTAAACGGGCATGGGTCCGATGGTTCGACTCTCGATTGCTGTTCGAACCGGAG
ATTTATAGGGACTGAACCGCCCATCCACCTACTTGACTTCAGAGTGCTTCGCCATAACCC
>Rosalind_3431
TCCCCCGATCCTGCATTTTAGACCGTCATTTCTGAGCGCAGCCGTTACTCTGTGTTCTAG
TCAATACGTGAGCGACGCGTGGTCAAGGATTAGCTTTGTTCTAGCATCATAGGTGGAACT
GTTTCCGAAACCTAGAGCTTGCAAGTAGCTCACCCTGTTTCACTGCATAACGAATTAAGT
GATACGAGCCTTAGGTAAACTATGGAATAGCATCCCCCAACGCTGCCCTTTGCTAGTTTT
CCAAGCATGCCTGGTTTTAGATCAGTTTACTTTTAAGTGAGTGCGCGTGATGCGAATCTC
TCAGCGATTTATTGCTGACCTACCAGTGAAACTTATGCAAGGCTATGTGCGCCTGGCCGT
ACCTGAAGCCGGGACCAGTTCTATGAGTGGCAATATACCTTCTTTTGGTTCCCTCGTATG
AACGTTAACATGGGGATTGAAAACTTGTTGATGTTTTATTTCAATTGTTCCCATGATGTG
TCGATGGGTGGAACGCATCGCAGTTCGCACAGATAGCGTCCAGGAATGTTCACGCGGGAT
TGCGGGAGCGTAGCTTTCGGGAAAAGGACGACGTTCGCATACCGATCAGTCGCCATGCCA
CATATACGGAGTTGGTATCAGTCTTTTGCATGGTCAGAGCGTACCAGGCCAACCGGACCC
ACATATCGTGGTTACCGCGACAGCAGTATGCACCGGGTGCACAATCCTGCTAAACCCCGG
ATCTTGGGCCATCAAGAGGTTACTTCGAAAGGCTCAATGGCCGTAGTGTGGTGCCGATCC
GGGCATGATCTCCTCGTTTGAATGTTCTGCCGCACCTCAACGGTTAAGTGAACTTACACT
GGAAGGTAGATCGTCACGGCTAAGTTCGGCCAAAACCTCGCCCGCAGTTGGAGCCAATCC
>Rosalind_2026
CTCATCATTTCCCAGCAATGGAGTTAAAGTTGGTCCTCCTCTCGTGAGTGAGCGTTGAAT
TTATAAGTAACCTCGTAGGTCCGAAGGAGAGTAAGGGAATAAGAAACGGCTCCGTTCCTA
ATGACTAGTTAGGAGGTTTGGGATGACGTGAGAAGGGTGTCCCTTTGGTACTCGAATCGG
AATATGTCGCTCGCATCCATGTGCTATACATCCTTACTTGCAAGTCATATGCGGGGTCAG
GGTTAGGTAGCCAGTGGCCTCTGAACTATCGGGATGACCTGTACTAACCGGTTTACAACC
AGACGGACCAGGGCACGGGAGTCCCTACGGTGCCCAGTACTACTGCGGGAAAATACACCC
TCACTGCAATAACGCGAAGACTAAACTCTGCCATAATATCGTAGGTATGCTCGCTCGCGC
GAATCGGTATCCTAGCCTTGGTATTCTTGGCCGGGGCCAATCTGCCCTCCTTAAGCGGAC
CATAATACCGGACCTCGTAATAAGCCGAAATAGATATTCCCATCCAAACGAGTTACCCTA
GGCGAGACGGCAGAGCTTCCATATGGTAAACCTACCTGATGCGGGTATGGCTCCAAAGCG
TTGGCATTCCACCATCCCGGATAAATTAAGGAACCTCATGAGTGGGTTTGCAACTGGGAG
CGTTTGCGCCGACCTTCGCTTTCCCACGTCTTAACTCGATCCGATATCCTGGTCGGGGGT
GAGGGCAGCACGGTACCTGGTTTGCTGACAGGTTCTCTCCGGCCGCCAGCCCCAGGGCGT
GTTAAGAGAAACCGCAACGGAGACCACCTAGTATTTTAGGCCGCCGGGGTGTTAGGTGAA
TAAACACAGACAACTTCCACAACACTCCAATTCTCATACGAACGGGTTAATAAGGATTTT
>Rosalind_5007
GGGAAGCTAAATCCCCCCCCAAGTGGGGCCGAGAAAAATAAGTACGCAGTCCTGTCAACC
CCGGATCTACCTACTCCCATCTTGCGCGGCTTGAACAGATGTGAGGGTCAGCGGCCTCTG
GATGTTCTCTGGCTTGGGTACTAGGAGACGAACCCAATTGTTAGTTCGAATTATTTGCCC
CAGGCGCCGATCCTTCTTCTCGAACGCCTCTTCCTAGCCCTGCCGGCTCCCTCCGAAATG
GACTCAGGCGCTTTCGTAGTCCCGACACGCGCGTTCTCATCTTGGTAATCAACGGTTCTT
GTGAGTGCGAATTGGTCGCACTCGTGCCCTGACACTTGCGGGCGGTGTGGACTTTACAAC
ATATGACCTGCGCACTTTGGGGCATAATCATGAAAATGAACCGCTTGTGACGTAGCGGGT
AGAGTTTGGGTAACTGAAGTGAAGTGCACGCGGGGGACGACAGTCGAGGCGGGTTAGAAT
ATTCGGGAAGCACACACCTACCTTCAGGGTCAGCCGGTGGAGAGGGGGGCTTCCGTGGCA
TTACACATACTGGACCAGATCAACTTACTGCGGTTTATCATAGTTTTCATCAGATTAATT
TTTCACGGTCTGCGAAGCGGTCTCTCAGCACAATAACCCTTTACCTTTCCGCAGATGACT
GTTTGGAATAGATTGGGTAGACACCCCGTCGCCCGCTTATCATGTAAATTACCCACTAAG
GAAGTTCGTACTAAGTAGACGTTTCTGGAAGGACGTCAAGAGAGTGTACTAGACACTATT
AATCTCACCACGATTTGTTGACACTATGCAGAAACTCAGGTTAGATATCCTCCTGTGGCC
TTCCACTTGCACTTTCCATTATCGTGCGCTAACAAAGCACACGACTGGGTCTACAACGTA
>Rosalind_2348
AAAACCCGCGCAGCTCTACGGCCCATCAATCTGAGCTAATAAGTCGTTCGCTTAAAGGGA
CTTCGCACCCCATCATCTGAACAAACCGTCAGACGTCTCTTGTGGACTCTACTGGTACGG
TTCTCGACGAAATTGCGCCATCAACGCAGCACGTAGGTCCACCGTAGCCACCTGAGGTAC
GGCTGGGCACAGTTTGCTCTGTATGCTACTGGGCAGAGAGTGTCTACTACTGCCGGTGCC
TGGACGCGCTCCTGCTAGACCACAATCTCCAAGGAGATTGCCTTGAAAGCTGCATATGTA
GAGTTCATCAATCCATAACTTCTCCGGACGCACTGTAAATCAATTATAGCATCTGTTCAC
TGTGAGATGTGTTTCAGGATGATTCCTTTCTAGAGATACCTTTTGATTGGCAGAGTCCTC
TGGAATCTCGGTGGACCATGGTTCTCATAACTCAGGGATCTCCATTCTATCGCACCGGTT
AACGTGGACACTCTTGTTCTGCGACGCCTGTCTTGTCGCGATGACGAGATACCGTGGGCT
TCGAGTACTATCAAGGACTACGCCGTACCCAAATCAATTGAACGATCAGCATATTGGCGC
GAGGCTTAAACGGCGTCTGCATGAGTATAGTTGCTTGGTCCAGGGCCTTATCATTGCATG
ACTTTATGGTTAGTATATGGTGTGGTAAGTTGTCGGTGGAGCTTTACTGGCCCGTTTATG
ACTGCCCATTACAGACTCCGTGTGCTGAATCGGGTCAGCCACCTCCATCTATGCCGCAGC
TCCCCGCTGGCTACATATCCGCACCGTATACAGGGGAAAGAGTACGCTCTAGACAGACCC
GCTGGCATCTCGTGCCCACCTGGACCGAATAGCGACCACAGTCATTCACGACTTTGCAAT
>Rosalind_3740
GAGCCGTTCTTTTGATATACTTAGGTCCGTGCGGTCTCCACCCAAGCAACTCCTCTTAAC
GCTATTACTCGGATTGATAGTATATAGGTACCTCTGTGAAGTTTTGCAACGAGCATCTTA
CATGTCCCCAGGTGGACTCAAGTATTGACGAGGTGACCGGCGTCCTAGGATTGGGCCAAT
GACTTAAGGGTATTGTGAACTAAGTTATGCTACCTTTCGATCGAGAGATCCACCCTTGCA
TCAGGCCATTTACGGGAGCAGCGTGTAATATTGGCTAGACTATCTCTAGTTCGAAATCGA
CAGATGGGTGCCCTTAGCTACTGTGTCCAGCCAGCCTAATGGTCGAGGGTTGATACATCT
TGATCGTACGTTCCTCTAGCGGCCAAGAACTCGATCGTGTGGAGAACATGAGCAACCCCA
CAGACATGCTATAGTCCTAGAGCTGATCTTTACCCTGGGAGAAGTCTGTTTTCTCGGGGC
ATGCCGTGTTTGGCTGGGCTATTACGGTGCCCCACACGGTACTTACAGTACAAGAGTTAG
CACTGGTTAAGGGATAAATTATCGATATATTGTCCCCCGAGAGCACTTTCAGAGGACCTG
ACCAAGTAACTTATGGGGCCAAGCACGAATCGGTGTCCGTTCGCCTACGCGTGAACCAGC
CGCAGGAGGTTAACGTTACCTATTCTGCTTAGTCCTCAGTCCGATAGTAGCACCTTTGTG
AGCGCAGGGAAAGTAGAGGCTAGGCCTTCATTGGCGCCCCAACAAGACCAACCCAAGGCG
AATAAAACCGCCCCAGTTCAGAGAAATTCGCGGACGAAACACCACTCGTGAACAACCATA
TCATGAGTAGAGTGGCCACATAGACGGGAACAACAAAAACGTAAGTGAATGGCTGGACTT
>Rosalind_0868
CTCTGAGTGGGCACACACTGCGGTGCCACCGCAGCTAGCAAGCGTGATACCACTATTCTT
CAGTGCTCCCTGCAGATGTGGCATACCTTGCTTTAATTTCGTTTAAGGGCGGCATGGCTT
TAACTGTTCTACATGCGTATATTGATCATCCAATGCCGCGCGTGCACAGTTCAAAATTAG
TCAGTTCCCACCCGACAATCTTCCCAGTCACTTCGATAAAAACGGCAGAGAATTTTGCTG
AGCAGAGTGACCATCAATATGGCTTGCGACTTACTTAAGTTTCCTCCCAGGTTATACATT
AATAGCGTCAGCATGCATTCCAGCATGAAGTTCCCAGATTCGCTCTCGCCTCAACTAAAG
CAGAAGCCACCACCGACCACCGCATGTTGTTTTTGGATAGCTACTATTCACACAGAGAAG
CTGTTTCGATTATTTGTGATTTGCACCGATTGAAGATTCGGCTCGATAGGGACTCTCGGA
CAGACTGTACCGGTTAGGGGATCTTTATTTACTATGTTACTATTATGTCTTCCCTAATAC
GCCTCTGCTAGTAGCTAAGGTTCCAGATTAAAACCCGGAGACGTGCGGTCGTACCGATCG
GCGGCCATCACAATGATCTTATTTAATTACACGTAGGCCATTGTCTTCGTCAATTTGCAG
GGCTTTGACTAGGACACACGAACGGCTTGAGGGGAAACCCGGCAACGTGCGCGAATATTC
TTTAGGCATTTTGGAGTGGTCATTTCAGGTCCTACCCCGAACCTGAAAGCGGGTAGGGGC
GTGGAATGCAGCAAACGATGCTTGAGGTCGCTCAAGCGGGCCCAATGTCAAGGGTTACCT
GCGAGAGGCGGAAGTGCAAAGAACCAGCGAAGGATATTGGCTATTCCCTAGTCATGAGGT
>Rosalind_6517
AGCTATTTGGGGTTTCACAATAGAGTTTCGAGGCTTAAGATAGACACCAGGCATAGACGT
CGGCAATCCTTTTACTTCAATATAGATATTATCCAAATTTTAAGCCACTCTTTCCGGTCA
GTTCCGCATCGGCCACCTCTCCTGGCCGCCACATTAAACGACCCTTTCTGTGGTCTTGGA
CTACCTCGCCTGCCATAGCCTACATACAATTGACAGATCTCGCTATTCCGCAAGTGTTGG
GCTAAACAAGGCAAGGATACTCATCTTCGTGCGCGATGGAAGTTATTCCTCTGTCGATGT
CCCAAGTCTGAATTGGAATGCATCAGACTAGTGCTGTCAGACCGCAGCTGGCTCATATGT
GAATCCATTCTTGAACGAGCGCGTCTATGTCTTCGGACTCCTGGGACTATTTACCCGCCA
AATGAGTACGGTATTGTTGCCGCATCACGCGAACACGTAGTGGGGCAAGTTAGGACATAT
GGGTTCCATCATACGTTTGCGAGGCAGCGGTATGGTATAACTCCAGCTAAGGAAGTCGCC
ACGGTTGCTTCGTCAACGAAGGCTGTGATGGACGCAGTCGTGTAGCAAATACTGACAAAA
CACTGAGTTGGCCACAGAAGCGGCTAAAATTAATCATCGTCTTGAAAATGTCGCCTTGAA
ATTGGTACAGTATGTTATGAGCTCGCACGGGGTTGGAGGATAACGAGTTTAAGTTACCTG
CCACGCAAAACATTGAACTCGAAACTTCGTTTTGAGGAGTATCTTTATCAATCGCGTTGG
GTGATTTATGCTGAGGGTATGAGATAATAATGCGATGAACTAGGAAAGCGGAGTTTCTAT
TGGCAGTATGGTCGCTTTATCGTCCATGTCTAAAATCCTTAGTTAGTGAGTTAAATGCAA
'''
    seqs = read_fasta(data)
    
    # matrix
    m = []
    
    length = 0
    for s in seqs:
        r = []
        length = len(s.sequence)
        for c in s.sequence:
            r.append(c)
        m.append(r)
    
    a = [0] * length 
    c = [0] * length
    g = [0] * length
    t = [0] * length
    
    for row in m:
        col = 0
        for e in row:
            if (e == 'A'):
                a[col] += 1
            elif (e == 'C'):
                c[col] += 1
            elif (e == 'G'):
                g[col] += 1
            else:
                t[col] += 1
            col += 1
    
    profile = list()
    
    for i in range(length):
        if (a[i] >= c[i] and a[i] >= g[i] and a[i] >= t[i]):
            profile.append('A')
        elif (c[i] >= a[i] and c[i] >= g[i] and c[i] >= t[i]):
            profile.append('C')
        elif (g[i] >= c[i] and g[i] >= a[i] and g[i] >= t[i]):
            profile.append('G')
        elif (t[i] >= c[i] and t[i] >= a[i] and t[i] >= a[i]):
            profile.append('T')
    
    for e in profile:
        sys.stdout.write(e)
    print
    
    print 'A:',
    for e in a:
        print e, 
    print
    print 'C:',
    for e in c:
        print e, 
    print    
    print 'G:',
    for e in g:
        print e, 
    print
    print 'T:',
    for e in t:
        print e, 
    
    