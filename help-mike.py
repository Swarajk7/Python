import sys
if __name__=='__main__':
    t=int(sys.stdin.readline())
    for xyz in range(t):
        n,k=sys.stdin.readline().split()
        n=int(n)
        k=int(k)
        ans=0
        ss=k
        while k<2*n:
            #print k
            if k%2==0:
                ans+=(k-1)/2
            else:
                ans+=k/2
            if k>n:
                ans-=(k-n-1)
            k+=ss
        print ans
