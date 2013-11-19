import sys,math
if __name__=='__main__':
    t=int(sys.stdin.readline())
    for abc in range(t):
        n=int(sys.stdin.readline())
        i=2
        c=n
        p=math.sqrt(n)
        mul=1
        while i<=p and i<c:
            if n%i==0:
                c=n/i
                if i!=c:
                    mul*=c
                mul*=i
            i+=1
        if mul<10000:
            print mul
        else:
            print str(mul)[-5:-1]
            
            
            
