import sys
if __name__=='__main__':
    n=int(sys.stdin.readline())
    s=''
    for xx in range(n):
        p=sys.stdin.readline()
        s+=p+' '
    t=int(sys.stdin.readline())
    for xx in range(t):
        a=sys.stdin.readline().strip()
        tt=s.count(a)
        c=a[:len(a)-2]+'se'
        print s.count(c)+tt
    
