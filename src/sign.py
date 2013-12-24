from itertools import permutations

if __name__ == '__main__':
    data = 4

    values = list()
    for i in range(0-data, 0+data+1):
        if i != 0:
            values.append(i)

    out = list(permutations(values, data))
    result = list()
    for temp in out:
        seen = set()
        for entry in temp:
            if (abs(entry) not in seen):
                seen.add(abs(entry))
        if (len(seen) == data):
            result.append(temp)

    print len(result)
    for e in result:
        for v in e:
            print v,
        print
