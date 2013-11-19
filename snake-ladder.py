import sys
l1=[]
s1=[]
xyz=0
def get(s,l,k,val):
    #if val>90:
        #print val
    p=val+k
    if p==100:
        return 1
    global l1,s1,xyz
    if len(l1)==0 and len(s1)==0 and val>=100:
        return -1
    #xyz+=1
    #if xyz>=1000:
        #exit(0)
    #print val
    if val>100:
        return -1
    if p in l0:
        #print p,val
        x=l0.index(p)
        val=l1[x]
        l0.remove(p)
        l1.remove(val)
        return get(s,l,k,val-k)
    elif p in s0:
        #print p,val 
        x=s0.index(p)
        val=s1[x]
        s0.remove(p)
        s1.remove(val)
        return get(s,l,k,val-k)
    else:
        return get(s,l,k,p)
if __name__=='__main__':
    t=int(sys.stdin.readline())
    for xyz in range(t):
        s,l=sys.stdin.readline().split()
        s=int(s)
        l=int(l)
        s0=[]
        l0=[]
        for i in range(s):
            a,b=sys.stdin.readline().split()
            a=int(a)
            b=int(b)
            s0.append(a)
            s1.append(b)
        for i in range(l):
            a,b=sys.stdin.readline().split()
            a=int(a)
            b=int(b)
            l0.append(a)
            l1.append(b)
        k=int(sys.stdin.readline())
        p=get(s,l,k,0)
        print p
