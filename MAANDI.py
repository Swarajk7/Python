import sys
from math import sqrt,ceil
def check(n):
    k=str(n)
    #print k
    for i in k:
        if i=='4' or i=='7':
            return 1
    return 0
def x(n):
    p=int(ceil(sqrt(n)))
    c=0
    #print p
    for i in range(1,p):
        #print i
        if n%i==0:
            if check(i):
                c+=1
                #print i,n/i
            if check(n/i):
                c+=1
    if n%p==0 and check(p):
        c+=1
    print c
if __name__=='__main__':
    t=int(sys.stdin.readline())
    a=[]
    for i in range(t):
        n=int(sys.stdin.readline())
        a.append(n)
    map(x,a)
