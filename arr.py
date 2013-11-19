def one(a,i,x,y):
    a[i-1]=x-y
    return a

def two(a,b):
    for i in range(len(a)):
        a[i]+=b
    #print a
    return a



if __name__=='__main__':
    n,m=raw_input().split()
    n=int(n)
    m=int(m)
    a=raw_input().split()
    y=0
    for i in range(n):
        a[i]=int(a[i])
    for i in range(m):
        x=raw_input().split()
        if x[0]=='1':
            a=one(a,int(x[1]),int(x[2]),y)
        elif x[0]=='2':
            y+=int(x[1])
        elif x[0]=='3':
            print a[int(x[1])-1]+y
