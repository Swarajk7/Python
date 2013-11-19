def main():
    t=(int)(input())
    for abc in range(t):
        v=raw_input().split(' ')
        a=(int)(v[0])
        n=(int)(v[1])
        b=[]
        c=raw_input().split(' ')
        for i in range(n):
            b.append((int)(c[i]))
        b.sort()
        count=0
        for i in range(n):
            if a>b[i]:
                a=a+b[i]
            elif a==b[i]:
                if b[i]==1:
                    count+=1
                else:
                    count+=1
                    a=2*a+b[i]-1
            else:
                if b[i]/a < n-i and a!=1:
                    count+=b[i]/a
                    for j in range(b[i]/a):
                        a=2*a-1
                    a+=b[i]
                else:
                    count+=1
            #print b[i],a
        print 'Case #'+str(abc+1)+': '+str(count)
if __name__=='__main__':
    main()
