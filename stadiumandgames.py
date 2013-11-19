def f(n):
    if n<=0:
        return 0
    if n%2==0:
        return n/2+f(n/2)
    else:
        return (n*(n-1))/2
import math
if __name__=='__main__':
    n=int(input())
    x=math.log(n+1,2)
    p=n
    if int(x)==x:
        p=n+1
    i=1
    while i<=30:
        """if f(i)==n:
            print i"""
        print i,f(i)
        i+=1
    
