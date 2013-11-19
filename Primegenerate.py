from math import sqrt,ceil
def seive(l,h):
    le=h-l+10
    a=[False]*le
    p=int(ceil(sqrt(h)))
    prime=[]
    b=[False]*(p+1)
    q=int(sqrt(p))+1
    #print p,q
    for i in range(2,q):
        #print i
        j=2*i
        while j<=p:
            if not b[j]:
                #print j,p
                b[j]=True
            j+=i
    for i in range(2,len(b)):
        if not b[i]:
            prime.append(i)
            if i>=l:
                print i
    #print prime
    #print "x-x-x-x-x-x-x"
    for i in prime:
        #print i
        j=l-(l%i)
        if j<=l:
            j+=i
        #print i,j
        a[j-l]=True
        while j<=h:
            if not a[j-l]:
                a[j-l]=True
                #print i,j
            j+=i
    '''for i in prime:
        #print i,i*i
        a[i*i-l]=False'''
    cnt=0
    for i in range(1,len(a)):
        if not a[i] and i+l<=h:
            print i+l
            cnt+=1
    return cnt+len(prime)
        
t=int(input())
for i in range(t):
    a,b=map(int,raw_input().split())
    a=int(a)
    b=int(b)
    seive(a,b)
    print ''
 
