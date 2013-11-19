import sys
def getmark(a,mark,j,d):
    for i in range(len(a)):
        if(not mark[i]) and (a[i]-a[j]>=d) and(i!=j):
            mark[i]=True
            return True
    return False
if __name__=='__main__':
    n,d=sys.stdin.readline().split()
    n=int(n)
    d=int(d)
    count=0
    mark=[False]*n
    a=[]
    for abc in range(n):
        a.append(int(sys.stdin.readline()))
    for i in range(len(a)):
        if not mark[i]:
            mark[i]=getmark(a,mark,i,d)
            if mark[i]:
                count+=2
    print count/2
