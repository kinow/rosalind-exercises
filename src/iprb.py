from __future__ import division

if __name__ == '__main__':
    data = '19 30 15'
    data = filter(None, data.split(' '))

    total = 0
    for i in data:
        total += float(i)

    AA = float(data[0])
    Aa = float(data[1])
    aa = float(data[2])

    p1 = (AA/total) * (AA-1)/(total-1)
    p2 = (AA/total) * (Aa)/(total-1)
    p3 = (AA/total) * (aa)/(total-1)
    p4 = (Aa/total) * (AA)/(total-1)
    p5 = float((Aa/total) * (Aa-1)/(total-1) * (3/4))
    p6 = (Aa/total) * (aa)/(total-1) * (2/4)
    p7 = (aa/total) * (AA)/(total-1)
    p8 = (aa/total) * (Aa)/(total-1) * 2/4

    #print p1, p2, p3, p4, p5, p6, p7, p8
    e = p1 + p2 + p3 + p4 + p5 + p6 + p7 + p8

    print "%.5f" % e


