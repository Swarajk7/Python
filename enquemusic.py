import sys
def get(a,j,m):
    i=j
    while i<len(a):
        #print a[i],i
        if a[i]==m:
            return i
        elif a[i]<m:
            i+=1
        else:
            return i
    return i-1
if __name__=='__main__':
    n,m=sys.stdin.readline().split()
    n=int(n)
    m=int(m)
    a=[]
    p,q=sys.stdin.readline().split()
    a.append(int(p)*int(q))
    for abc in range(n-1):
        p,q=sys.stdin.readline().split()
        a.append(a[-1]+(int(p)*int(q)))
    j=0
    m=sys.stdin.readline().split()
    for i in m:
        j=get(a,j,int(i))
        print j+1
        #print ''
    #print a
