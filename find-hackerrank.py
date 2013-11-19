import sys
if __name__=='__main__':
    n=int(sys.stdin.readline())
    for x in range(n):
        s=sys.stdin.readline().split()
        p=-1
        q=-1
        if s[0].strip()=='hackerrank':
            p=1
        if s[-1].strip()=='hackerrank':
            q=1
        if p==1 and q==1:
            print '0'
        elif p==1:
            print '1'
        elif q==1:
            print '2'
        else:
            print '-1'
