import sys
def getQ(size):
    bucket=[[] for i in range(size)]
    return bucket
def noDigit(b):
    return len(str(max(b)))
def getHash(val,i):
    i+=1
    return (val%10**i)/(10**(i-1))
def radix(b,i):
    bucket=getQ(10)
    for elem in b:
        p=getHash(elem,i)
        bucket[p].append(elem)
    dic=[]
    for everylist in bucket:
        dic.extend(everylist)
    return dic
def SortIt(b):
    noofd=noDigit(b)
    for i in range(noofd):
        b=radix(b,i)
    return b
if __name__=='__main__':
    print 'Enter The Numbers'
    a=sys.stdin.readline().split()
    b=[int(i) for i in a]
    b=SortIt(b)
    for i in b:
        print i
