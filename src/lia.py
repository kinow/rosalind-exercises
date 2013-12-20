import decimal
from scipy.misc import comb

context = decimal.getcontext()
context.prec = 3
context.rounding = decimal.ROUND_HALF_DOWN

def p(children, n):
    
    return 0

def binomial(n, k):
    """Compute n factorial by a direct multiplicative method."""
    if k > n - k:
        k = n - k  # Use symmetry of Pascal's triangle
    accum = 1
    for i in range(1, k + 1):
        accum *= (n - (k - i))
        accum /= i
    return accum

if __name__ == '__main__':
    k = 6
    N = 15
    
    children = 2**k
    
    total = 0.0
    # for each child
    for i in range(N, children+1):
        AaBb = 0.25**i
        NotAaBbChildren = 0.75**(children-i)
        #print AaBb, NotAaBbChildren
        p = comb(children, i, 1) * AaBb * NotAaBbChildren
        total += p
        
    print round(total, 3)
    
