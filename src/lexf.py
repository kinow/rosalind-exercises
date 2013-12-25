import itertools

data = 'V F K P B O'
n = 3
order = [x for x in data.split()]

def get_order(char):
    for i in len(order):
        if (order[i]) == char:
            return i
    return -1

if __name__ == '__main__':
    combs = [''.join(entry) for entry in list(itertools.product(order, repeat=n))]
    total = 0
    for c in combs:
        print c
        total += 1
