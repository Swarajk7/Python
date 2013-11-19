def pri(c):
    s=''
    for val in c:
        s+=str(val)+' '
    print s

if __name__=='__main__':
    m=int(input())
    a=raw_input().split()
    for i in range(len(a)):
        a[i]=int(a[i])
    c=[a[0],a[1]]
    diff=a[1]-a[0]
    for i in range(2,len(a)):
        if a[i]-c[-1]!=diff:
            diff=a[i]-c[-1]
            #print c,a[i],diff
            c.append(a[i])
            
    print len(c)
    pri(c)
