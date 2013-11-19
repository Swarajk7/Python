import sys
def getmin(s):
    k=0
    minx=s[0]
    for i in range(1,len(s)):
        if s[i]<=minx:
            k=i
            minx=s[i]
    return k
def getmax(s):
    k=0
    maxx=s[0]
    for i in range(1,len(s)):
        if s[i]>=maxx:
            k=i
            maxx=s[i]
    return k
if __name__=='__main__':
    t=int(sys.stdin.readline())
    area=[]
    for i in range(t):
        x1,y1,x2,y2,x3,y3=sys.stdin.readline().strip().split()
        x1=int(x1)
        x2=int(x2)
        x3=int(x3)
        y1=int(y1)
        y2=int(y2)
        y3=int(y3)
        s=0.5*abs(x1*y2-x1*y3+x2*y3-x2*y1+x3*y1-x3*y2)
        area.append(s)
    print getmin(area)+1,getmax(area)+1
