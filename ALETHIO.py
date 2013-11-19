import sys
def main():
    a=sys.stdin.readline()
    maxc=0
    tmp=0
    stat=True
    rind=0
    for i in range(len(a)-1):
        j=i
        tmp=0
        stat=0
        while j<len(a):
            #print a[j],stat
            if ord(a[j])>=65:
                stat+=1
            if stat>1:
                break
            tmp+=1
            j+=1
        print 'i=',ord(a[i])
        print i,tmp
        print ' '       
        if maxc<tmp:
            maxc=tmp
            rind=i
    b=''
    i=0
    while i<maxc:
        print a[rind+i]
        if ord(a[rind+i])>65:
            b+='9'
        else:
            b+=a[rind+i]
        i+=1
    print b,rind
if __name__=='__main__':
    main()
            
