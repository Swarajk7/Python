def getdiff(h1,m1,t1,h2,m2,t2):
    return (h2-h1)*3600+(m2-m1)*60+(t2-t1)
import sys
if __name__=='__main__':
    t=int(sys.stdin.readline())
    for i in range(t):
        h1,m1,t1=sys.stdin.readline().split()
        h2,m2,t2=sys.stdin.readline().split()
        diff=getdiff(int(h1),int(m1),int(t1),int(h2),int(m2),int(t2))
        ans=diff/100
        if ans%2==0:
            print 'S'
        else:
            print 'C'
        
        
