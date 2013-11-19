def main():
    n=(int)(input())
    a=raw_input().split(' ')
    print a
    b=[]
    for i in range(len(a)):
        b.append((int)(a[i]))
    q=(int)(input())
    for abc in range(q):
        a=raw_input().split(' ')
        l=(int)(a[0])
        r=(int)(a[1])
        a=b[l:r+1]
        minval=min(a)
        j=0
        c=b[:]
        while j<len(c):
            if j>=l and j<=r:
                c[j]=minval+((c[j]-minval)/2.0)
            else:
                c[j]=(minval+c[j])*1.0
            j+=1
        print max(c)
if __name__=='__main__':
    main()
