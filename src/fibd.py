

def fibo(n, m):
    t = list()
    for i in range(n):
        if i < m:
            if i == 0 or i == 1:
                t.append(1)
            else:
                t.append(t[-1] + t[-2])
        else:
            rabbits = 0

            for j in range(i-m, i-1):
                rabbits = rabbits + t[j]

            t.append(rabbits)
    return t




if __name__ == '__main__':
    n = 99 # number of months to calculate
    m = 16 # months a rabbit lives

    print fibo(n, m)[-1]

