import sys
if __name__=='__main__':
    n=int(input())
    a=sys.stdin.readline().split()
    b=[]
    for i in a:
        b.append(int(i))
    b.sort()
    x=0
    y=0
    su=0
    p=0
    i=0
    while i<2*n-1:
        #print i,su,x,y
        if p!=n:
            if b[i]>0:
                y+=b[i]
            else:
                x+=b[i]
            p+=1
        else:
            if abs(x)>y:
                su+=abs(x)-y
            else:
                su+=y-abs(x)
            x=0
            y=0
            p=0
            i-=1
        i+=1
    #print i,su,x,y
    su+=x+y
    print su
