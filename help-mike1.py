import sys
if __name__=='__main__':
    t=int(sys.stdin.readline())
    for xyz in range(t):
        n,k=sys.stdin.readline().split()
        n=int(n)
        k=int(k)
        ans=0
        p=(2*n-1)/k
        x=(k*p*(p+1))/4
        print x,
        x-=(p/2)
        print x,
        x-=(p/2)
        print x
