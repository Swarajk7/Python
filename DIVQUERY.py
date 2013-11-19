import sys
if __name__=='__main__':
    n,q=sys.stdin.readline().split()
    n=int(n)
    q=int(q)
    a=sys.stdin.readline().split()
    i=0
    for x in a:
        a[i]=int(x)
        i+=1
    for i in range(q):
        l,r,k=sys.stdin.readline().split()
        l=int(l)
        k=int(k)
        r=int(r)
        l-=1
        r-=1
        count=0
        while l<=r:
            if a[l]%k==0:
                count+=1
            l+=1
        print count
    
