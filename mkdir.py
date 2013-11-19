def main():
    t=(int)(input())
    for abc in range(t):
        a=raw_input().split(' ')
        n=(int)(a[0])
        m=(int)(a[1])
        b=[]
        for i in range(n):
            a=raw_input()
            a=a.split('/')
            s=''
            j=1
            while j<len(a):
                s+=a[j]
                if s not in b:
                    b.append(s)
                j+=1
        count=0
        for i in range(m):
            a=raw_input()
            a=a.split('/')
            s=''
            j=1
            while j<len(a):
                s=s+a[j]
                if s not in b:
                    count+=1
                    b.append(s)
                j+=1
        print 'Case #'+str(abc+1)+': '+str(count)
if __name__=='__main__':
    main()
        
