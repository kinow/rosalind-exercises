from itertools import product
data = 'F J O A K V M U R N X'
alphabet = data.split(' ')
order = dict()
for i in range(len(alphabet)):
    order[alphabet[i]] = i
natural_order = {
0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J', 10: 'K', 11: 'L', 12: 'M',
13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T', 20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y', 25: 'Z'
} # blergh... TODO: fix me later
def compare(item1, item2):
    item1 = ''.join(natural_order[order[x]] for x in item1)
    item2 = ''.join(natural_order[order[x]] for x in item2)
    return cmp(item1, item2)
    #item1 = item1[0]
    #item2 = item2[0]
#     for i in range(len(item1)):
#         if (i > len(item2)):
#             return 0
#         if (order[item1[i]] > order[item2[i]]):
#             return 1
#         elif (order[item1[i]] < order[item2[i]]):
#             return -1
#         else:
#             return 0

if __name__ == '__main__':

    bucket = list()
    n = 4
    i = 1
    while(i <= n):
        values = product(alphabet, repeat=i)
        bucket.extend(values)
        i+=1
    bucket = sorted(bucket, cmp=compare)

    f = open('/home/kinow/Desktop/test.txt','w')
    for drop in bucket:
        for c in drop:
            f.write(str(c)) # python will convert \n to os.linesep
        f.write('\n')
    f.close() # you can omit in most cases as the destructor will call if
