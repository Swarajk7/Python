import math

def nCr(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)

if __name__ == '__main__':
    t=(int)(input())
    for absda in range(t):
        s,n,m,k=raw_input().split()
        s=int(s)-1
        n=int(n)-1
        m=int(m)-1
        k=int(k)
        if s<=k:
            print "0.000000"
            continue
        result=nCr(m,k)*nCr(n-k,s-k)/nCr(n,s)
        print result
