'''
UUU F      CUU L      AUU I      GUU V
UUC F      CUC L      AUC I      GUC V
UUA L      CUA L      AUA I      GUA V
UUG L      CUG L      AUG M      GUG V
UCU S      CCU P      ACU T      GCU A
UCC S      CCC P      ACC T      GCC A
UCA S      CCA P      ACA T      GCA A
UCG S      CCG P      ACG T      GCG A
UAU Y      CAU H      AAU N      GAU D
UAC Y      CAC H      AAC N      GAC D
UAA Stop   CAA Q      AAA K      GAA E
UAG Stop   CAG Q      AAG K      GAG E
UGU C      CGU R      AGU S      GGU G
UGC C      CGC R      AGC S      GGC G
UGA Stop   CGA R      AGA R      GGA G
UGG W      CGG R      AGG R      GGG G 
'''

from collections import defaultdict
import operator

inv_codon_table = defaultdict(list)

inv_codon_table['F'].append('UUU')
inv_codon_table['L'].append('CUU')
inv_codon_table['I'].append('AUU')
inv_codon_table['V'].append('GUU')
inv_codon_table['F'].append('UUC')
inv_codon_table['L'].append('CUC')
inv_codon_table['I'].append('AUC')
inv_codon_table['V'].append('GUC')
inv_codon_table['L'].append('UUA')
inv_codon_table['L'].append('CUA')
inv_codon_table['I'].append('AUA')
inv_codon_table['V'].append('GUA')
inv_codon_table['L'].append('UUG')
inv_codon_table['L'].append('CUG')
inv_codon_table['M'].append('AUG')
inv_codon_table['V'].append('GUG')
inv_codon_table['S'].append('UCU')
inv_codon_table['P'].append('CCU')
inv_codon_table['T'].append('ACU')
inv_codon_table['A'].append('GCU')
inv_codon_table['S'].append('UCC')
inv_codon_table['P'].append('CCC')
inv_codon_table['T'].append('ACC')
inv_codon_table['A'].append('GCC')
inv_codon_table['S'].append('UCA')
inv_codon_table['P'].append('CCA')
inv_codon_table['T'].append('ACA')
inv_codon_table['A'].append('GCA')
inv_codon_table['S'].append('UCG')
inv_codon_table['P'].append('CCG')
inv_codon_table['T'].append('ACG')
inv_codon_table['A'].append('GCG')
inv_codon_table['Y'].append('UAU')
inv_codon_table['H'].append('CAU')
inv_codon_table['N'].append('AAU')
inv_codon_table['D'].append('GAU')
inv_codon_table['Y'].append('UAC')
inv_codon_table['H'].append('CAC')
inv_codon_table['N'].append('AAC')
inv_codon_table['D'].append('GAC')
inv_codon_table['Stop'].append('UAA')
inv_codon_table['Q'].append('CAA')
inv_codon_table['K'].append('AAA')
inv_codon_table['E'].append('GAA')
inv_codon_table['Stop'].append('UAG')
inv_codon_table['Q'].append('CAG')
inv_codon_table['K'].append('AAG')
inv_codon_table['E'].append('GAG')
inv_codon_table['C'].append('UGU')
inv_codon_table['R'].append('CGU')
inv_codon_table['S'].append('AGU')
inv_codon_table['G'].append('GGU')
inv_codon_table['C'].append('UGC')
inv_codon_table['R'].append('CGC')
inv_codon_table['S'].append('AGC')
inv_codon_table['G'].append('GGC')
inv_codon_table['Stop'].append('UGA')
inv_codon_table['R'].append('CGA')
inv_codon_table['R'].append('AGA')
inv_codon_table['G'].append('GGA')
inv_codon_table['W'].append('UGG')
inv_codon_table['R'].append('CGG')
inv_codon_table['R'].append('AGG')
inv_codon_table['G'].append('GGG')

if __name__ == '__main__':
    data = 'MWKTQSSFDHHENNHRWDPCYCTWDGMSSMIRRSYEYTYAHRENHPLTIFTFYYKRIMRFVWCRLVVRTCYGNEALRCDPAQKLSFNQNPDETFHWFPDFEEIDLQPVESMPNLKYKVYWHDTSTVCDVHYQLEPAQRHPEQVGDRADHDTWWNQEPNHTDVPNQNCPWTPESEVYKDCIRKTMMWRGDNQKYVCVPRWSMMILFIGETMYFYVQPGGHPHNNDPTGGTRWPAYIVELRHLHITMYQYYPQSESDWDNESGTCASYWCMFNDRRPWWLEYKMALFTGVTLMWKCRWQNEWGHEGHCQLAPCVRGKQPPTSLQYPHHAGVNGFNRMIFEWMQQPEREKVGVQHTLIKYYHIAQGPALQFAFTTAWKTEWRESNCWPCYENRLARNIYDDLIQLHYREAMPKMVCWTIYQYYHWYCDKMTGCSQKVLISAQVQTHSIAVDRIWMIWRWCSRLAAGCLLFQYGHECWRNQVSKFTPDYTQNMQFPNMRHGDSEIKRERSEFNEYINCCQVIHCSMDWHITIQKTRRVMDRLTKLESWDAVVFKWGYDESLAYRIWLQMKFIYYSQSAHHDVVYESYMNAILNAANPARMSANVFKQLCAKTTHPCLLMYEKHNLGTQTAEPKPVKSYMYDSPAFIESHNPTLEDEAYFFNPNAGDIHTFFKIRSPPCHIQTHLTFCCQENTNPWNMDMHLWQMEMTYQPLWVEMIWSSQHVRIIVSKAGFFGPGHEVPIPPYVADCPGVKVDCYNWRQYVAMGITRDCIAITEQQSCDSPSGEIELCTNYHVATEDDETWMGAKYPGHTRASIKYAWTDQYSDDCQELDSRFIVAIFPWQKGKCDIPQIRRGMYSIMHCMNHLVFWQAGVNHCCDRGVCRFKWFKHRQTQTMYNWIHHMTPAKDKRPHIPKGVADQYRTMAEDCNLNVSYRKFGISANGVISTQKCDFVFLCAHWSPQPWCFVWQMEDMHNQFSWMDSYMDTDYRHISDLMYMCDGVACE'
    
    elements = list()
    for c in data:
        nt = inv_codon_table[c]
        elements.append(nt)
    elements.append(inv_codon_table['Stop'])
    
    total = 1 #considering there will always exist elements
    for i in range(len(elements)):
        total *= len(elements[i])
        
    print total % 1000000
        