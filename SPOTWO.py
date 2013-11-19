n=int(input())
for i in range(n):
    a=int(input())
    a=int(bin(a)[2:])
    a*=2
    print pow(2,a,1000000007)
    
