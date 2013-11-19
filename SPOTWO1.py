from math import log
import sys
def init():
    ar=[]
    i=1
    while i<=10010010011111000000:
        ar.append(pow(2,i,1000000007))
        i*=10
    return ar

f=[2, 1024, 976371285L, 688423210L, 905611805L, 607723520L, 235042059L,
   255718402L, 494499948L, 140625001L, 291251492L, 25600497L, 959366170L,
   836339738L, 621966918L, 264444359L, 271283348L, 952065854L, 719476260L,
   28918236L]

def call(n):
    global f
    if n==0:
        return 1
    if n==1:
        return 2
    else:
        p=len(str(n))-1
        q=n%(10**p)
        #print p,q
        return (f[p]*(call(q)%1000000007))%1000000007
t=int(sys.stdin.readline())
for i in range(t):
    n=int(sys.stdin.readline())
    b=bin(n)[2:]
    n=int(b)
    print (call(n)**2)%1000000007
