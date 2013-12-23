'''
Created on Dec 23, 2013

@author: kinow
'''
from decimal import Decimal

if __name__ == '__main__':
    data = '17375 16744 17370 16747 18767 16079'
    arr = filter(None, data.split(' '))
    probabilities = [1.0, 1.0, 1.0, 0.75, 0.5, 0]

    total = Decimal(0)
    index = 0
    for e in arr:
        total += Decimal(e) * Decimal(probabilities[index]) * 2
        index += 1

    print total

