import sys
if __name__=='__main__':
    n,m,k=sys.stdin.readline().split()
    n=int(n)
    m=int(m)
    k=int(k)
    a=sys.stdin.readline().split()
    b=sys.stdin.readline().split()
    s1=0
    s2=0
    for i in a:
        s1+=int(i)
    for i in b:
        s2+=int(i)

    if s1>s2:
        print 'YES'
    else:
        print 'NO'
