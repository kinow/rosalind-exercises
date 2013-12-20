''''
n number of months
'''
import collections
rabbits = collections.defaultdict(list)

m = 3 # months a rabbit lives

def fibo(n, current_month):
    if (n == 1):
        #return 1
        rabbits[current_month].append(1)
    elif(n == 2):
        #return 1
        rabbits[current_month].append(1)
    else:
        #return fibo(n-1)+fibo(n-2)
        next_month = current_month+1
        rabbits[current_month].append(fibo(n-1, next_month)+fibo(n-2, next_month))
if __name__ == '__main__':
    n = 6 # number of months to calculate
    
    fibo(n, 0)
    
    print rabbits