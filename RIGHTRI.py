import sys
def get(a,b):
    return (a[0]-b[0])**2+(a[1]-b[1])**2
if __name__=='__main__':
    t=int(sys.stdin.readline())
    count=0
    for abc in range(t):
        x1,y1,x2,y2,x3,y3=sys.stdin.readline().split()
        x1=int(x1)
        x2=int(x2)
        x3=int(x3)
        y1=int(y1)
        y2=int(y2)
        y3=int(y3)
        len1=get((x1,y1),(x2,y2))
        len2=get((x3,y3),(x2,y2))
        len3=get((x1,y1),(x3,y3))
        if len1+len2==len3 or len1+len3==len2 or len2+len3==len1:
            count+=1
    print count
