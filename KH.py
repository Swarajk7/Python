def f(n):
    if n%2==0:
        return 3*pow(2,n/2,1000000007)-2
    else:
        return pow(2,(n+1)/2+1,1000000007)-2
if __name__=='__main__':
    t=(int)(input())
    for abc in range(t):
        n=(int)(input())
        ans=f(n)
        ans = (ans+MOD)%MOD;
        print ans
        
