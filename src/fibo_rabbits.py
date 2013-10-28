def fibo(n, k):
    if (n == 1):
        return 1
    elif(n == 2):
        return 1
    else:
        return fibo(n-1, k)+(fibo(n-2, k)*k)

if __name__ == '__main__':
    i = '33 5'
    data = i.split()
    n = int(data[0])
    k = int(data[1])
    
    o = fibo(n, k)
    print o
    