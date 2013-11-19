def israone(n):
    e=0
    o=0
    while n>0:
       o+=n%10
       n=n/10
       e+=n%10
       n=n/10
    return e-o
if __name__=='__main__':
    #t=(int)(input())
    i=10
    a=[]
    while i<=10**8:
        if israone(i)==1:
            a.append(i)
            print i
        i+=11
        #print i
    print a
