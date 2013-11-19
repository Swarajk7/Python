import sys
def x(s,val):
    #print s
    global p
    if len(val)==6:
        y(val)
    else:
        i=s
        while i<len(a):
            val.append(a[i])
            x(i+1,val)
            val.remove(a[i])
            i+=1
def y(xx):
    for i in xx:
        print i,
    print ' '
if __name__=='__main__':
    a=map(int,sys.stdin.readline().strip().split())
    while a[0]!=0:
        a=a[1:]
        val=[]
        s=0
        x(s,val)
        a=map(int,sys.stdin.readline().strip().split())
