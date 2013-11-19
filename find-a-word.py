import sys
if __name__=='__main__':
    n=int(sys.stdin.readline())
    s=''
    for i in range(n):
        a=sys.stdin.readline().strip()
        s+=a+' '
    t=int(sys.stdin.readline())
    for i in range(t):
        a=sys.stdin.readline().strip()
        p=s.count(a)
        for i in range(48,58):
            p-=s.count(a+chr(i))
            p-=s.count(chr(i)+a)
            print p
        for i in range(65,91):
            p-=s.count(a+chr(i))
            p-=s.count(chr(i)+a)
            print p
        for i in range(91,123):
            p-=s.count(a+chr(i))
            p-=s.count(chr(i)+a)
            print p
        p-=s.count(a+'_')
        p-=s.count('_'+a)
        print p
