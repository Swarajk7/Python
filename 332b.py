import sys
if __name__=='__main__':
    n,k=sys.stdin.readline().split()
    n=int(n)
    k=int(k)
    a=sys.stdin.readline().split()
    for i in range(n):
        a[i]=int(a[i])
    dp=[]
    tmpsum=0
    for i in range(k):
        tmpsum+=a[i]
    i=k
    j=0
    dp.append(tmpsum)
    while i<=n-k+1:
        print a[i]
        tmpsum=tmpsum-a[j]+a[i]
        i+=1
        j+=1
        dp.append(tmpsum)
    print dp
