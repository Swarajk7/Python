import sys
def getQ(size):
    bucket=[[] for i in range(size)]
    return bucket
def noDigit(b):
    return len(str(max(b)))
def getHash(val,i):
    return (val%10**i)/(10**(i-1))
p1=0
def radix(b,i,no):
    if i>=no:
        return b
    if len(b)<=1:
        return b
    bucket=getQ(10)
    for elem in b:
        p=getHash(elem,no-i)
        #print p,elem,i
        bucket[p].append(elem)
    for j in range(len(bucket)):
        #print eachar
        bucket[j]=radix(bucket[j],i+1,no)
    dic=[]
    for everylist in bucket:
        #print everylist
        dic.extend(everylist)
    print dic
    return dic
if __name__=='__main__':
    a=[13,13,132,9817391,1237,1231,131]
    #a=[170, 45, 75, 90, 2, 24, 802, 66]
    print  noDigit(a)
    a=radix(a,0,noDigit(a))
    print a
    
