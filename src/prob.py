from decimal import Decimal, getcontext, ROUND_HALF_DOWN
from math import log10

context = getcontext()
context.prec = 5
context.rounding = ROUND_HALF_DOWN

def get_prob(gc, at, gc_prob):
    return Decimal(gc*log10(gc_prob/2)) + Decimal(at*log10((1-gc_prob)/2))

if __name__ == '__main__':
    seq = 'TCCAGGGAAGCCCGTTCTAGTGGGGCAGGCCGATTTGTCGGTTAAAGGGGTACGTTCCTCAGCAGATCGTCAGGGACAAACCCGGTGTCAATTAT'
    gc_probs = [Decimal(x) for x in '0.094 0.120 0.173 0.233 0.310 0.358 0.415 0.438 0.489 0.539 0.599 0.668 0.692 0.763 0.839 0.867 0.904'.split(' ')]

    seq_gc = 0
    seq_at = 0
    for c in seq:
        if c in ['C', 'G']:
            seq_gc += 1
        elif c in ['A', 'T']:
            seq_at += 1

    for k in range(len(gc_probs)):
        print get_prob(seq_gc, seq_at, gc_probs[k]),

    print

