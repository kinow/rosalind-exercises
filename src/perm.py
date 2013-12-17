# http://stackoverflow.com/questions/104420/how-to-generate-all-permutations-of-a-list-in-python

def all_perms(elements):
    if len(elements) <=1:
        yield elements
    else:
        for perm in all_perms(elements[1:]):
            for i in range(len(elements)):
                #nb elements[0:1] works in both string and list contexts
                yield perm[:i] + elements[0:1] + perm[i:]
                
if __name__ == '__main__':
    n = 6
    perms = list()
    for i in all_perms(range(1,n+1)):
        perms.append(i)
        
    print len(perms)
    for p in perms:
        for e in p:
            print e, 
        print