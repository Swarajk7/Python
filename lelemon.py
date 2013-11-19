import sys
if __name__=='__main__':
    t=int(sys.stdin.readline())
    for abc in range(t):
        n,m=sys.stdin.readline().split()
        n=int(n)
        m=int(m)
        myarr=[]
        mar=sys.stdin.readline().split()
        for ax in range(n):
            val=sys.stdin.readline().split()
            val.remove(val[0])
            val=[int(x) for x in val]
            myarr.append(val)
        ans=0
        for i in mar:
            if len(myarr[int(i)])!=0:
                j=max(myarr[int(i)])
                myarr[int(i)].remove(j)
            else:
                j=0
            ans+=j
        print ans
