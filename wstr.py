def check(a):
    from array import array
    c=[0]*26
    for i in range(len(a)):
        #print a[i]
        c[ord(a[i])-97]+=1
    #print c
    return max(c)
if __name__=='__main__':
    t=int(input())
    for abc in range(t):
        a=raw_input()
        for i in range(len(a)):
            if a[i]!='#':
                break
        a=a[i:]
        a=a.split('#')
        b=[]
        if len(a)<4:
            print 0
            continue
        s=''
        for i in range(len(a)):
            s+=a[i]
            b.append(check(a[i]))
        print b
        if 0 in b:
            print 0
            continue
        mx=0
        for i in range(len(b)-3):
            x=b[i]+b[i+1]+b[i+2]+b[i+3]
            #print x
            if x>mx:
                mx=x
        print mx+3
            
