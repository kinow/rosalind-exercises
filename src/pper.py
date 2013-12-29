from math import factorial
# http://www.daniweb.com/software-development/python/code/448888/number-of-permutations-python
if __name__ == '__main__':
    n = 99
    k = 9

    c = (factorial(n)/factorial(n-k) % 1000000)
    print c
