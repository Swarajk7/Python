import sys
def getQ(size):
    bucket=[[] for i in range(size)]
    return bucket
def noDigit(b):
    return len(str(max(b)))
def getHash(val,i):
    i+=1
    return (val%10**i)/(10**(i-1))
def radix(bucket,b,i):
    for elem in b:
        p=getHash(elem,i)
        bucket[p].append(elem)
    dic=[]
    for everylist in bucket:
        dic.extend(everylist)
    for i in range(10):
        bucket[i]=[]
    return dic
def SortIt(b):
    noofd=noDigit(b)
    bucket=getQ(10)
    for i in range(noofd):
        b=radix(bucket,b,i)
    return b
if __name__=='__main__':
    n=int(sys.stdin.readline())
    b=[]
    for i in range(n):
        b.append(int(sys.stdin.readline()))
    b.sort()
    for i in b:
        print i
