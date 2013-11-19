def main():
    T=(int)(input())
    for aaa in range(T):
        a=raw_input().split(' ')
        E=(int)(a[0])
        R=(int)(a[1])
        N=(int)(a[2])
        b=[]
        c=raw_input().split(' ')
        for i in range(N):
            b.append((int)(c[i]))
        gain=0
        b.sort(reverse=True)
        for i in range(N):
            gain+=b[i]*E
            #print gain
            if(R<E):
                E=R
        print 'Case #'+str(aaa+1)+': '+str(gain)
if __name__=='__main__':
    main()
