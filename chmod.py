import sys
if __name__=='__main__':
    n=int(sys.stdin.readline())
    a=sys.stdin.readline().split()
    m=1
    for i in range(n):
        m*=int(a[i])
        a[i]=m
    t=int(sys.stdin.readline())
    for j in range(t):
        l,r,m=sys.stdin.readline().split()
        l=int(l)
        r=int(r)
        m=int(m)
        if l==1:
            print a[r-1]%m
        else:
            print (a[r-1]/a[l-1])%m
        
