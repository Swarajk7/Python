import sys
def getQ(size):
    bucket=[[] for i in range(size)]
    return bucket
def noDigit(b):
    return len(max(b))
def getHash(val,i):
    if i>=len(val):
        return 26
    return ord(val[i])-97
def radix(b,i,no):
    if i>=no:
        return b
    if len(b)<=1:
        return b
    bucket=getQ(27)
    for elem in b:
        p=getHash(elem,i)
        #print p,elem,i
        bucket[p].append(elem)
    for j in range(len(bucket)):
        #print eachar
        bucket[j]=radix(bucket[j],i+1,no)
    dic=[]
    dic.extend(bucket[26])
    bucket[26]=[]
    for everylist in bucket:
        #print everylist
        dic.extend(everylist)
    #print dic
    return dic
if __name__=='__main__':
    a=['swaraj','india','hello','b','ba','abc']
    #a=['abc','bac','cba','aab','acde','bca','a','aa','abca','aaa']
    #a=['asdfasdf','adfasdf','asdfr']
    print  noDigit(a)
    a=radix(a,0,noDigit(a))
    print a
