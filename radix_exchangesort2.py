import time
s2b=['0']*52
def init():
    global s2b
    for i in range(97,123):
        s2b[i-97]=bin(i)[2:]
    for i in range(65,91):
        s2b[i-65+26]=bin(i)[2:]
        #print s2b[i-97]
def noDigit(b):
    return len(max(b))
def stobin(val,leng):
    s=''
    global s2b
    for i in val:
        p=ord(i)
        if p>=97:
            s+=s2b[p-97]
        else:
            s+=s2b[p-65+26]
    mylen=len(val)
    while mylen<=leng:
        s+='0000000'
        mylen+=1
    return s
def getStr(a):
    i=0
    s=''
    while i<len(a):
        s+=chr(int(a[i:i+7],2))
        i+=7
    return s
def radixExc(a,l,h,k,n):
    i=l
    j=h
    #print k
    if l>=h:
        return
    if k>=n:
        return
    while i<j:
        while i<len(a) and a[i][k]=='0':
            i+=1
        while j>0 and a[j][k]=='1':
            j-=1
        if i<j: 
            a[i],a[j]=a[j],a[i]
        #print a
        #break
    radixExc(a,l,j,k+1,n)
    radixExc(a,i,h,k+1,n)
if __name__=='__main__':
    init()
    a=['abc','bca','cab','b','ba','sumit','Ankit','Swaraj']
    global s2b
    #print s2b
    j=0
    print time.time()
    maxnum=noDigit(a)
    for i in a:
        a[j]=stobin(i,maxnum)
        #print a[j]
        j+=1
    #print a
    #a=['0','0','1','1','0']
    radixExc(a,0,len(a)-1,0,maxnum*7)
    print time.time()
    print 'sorted'
    for i in a:
        print getStr(i)
