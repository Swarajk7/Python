def ax(a,n,i):
    ans=0
    for j in range(1,i):
        ans+=a[j-1]*(j-1)-(n-i)*a[i-1]
    return ans
def check(a):
    for i in a:
        if i!=0:
            return False
    return True
if __name__=='__main__':
    a=[5,3,4,1,2]
    n=5
    k=0
    mx=-10**10
    hit=-1
    while n>0:
        stat=True
        for i in range(1,len(a)+1):
            xyz=ax(a,n,i)
            if xyz==0:
                stat=stat*True
            else:
                stat=stat*False
            if xyz>mx and xyz<k:
                mx=xyz
                hit=i-1
        print hit+1,a,n
        a.remove(a[hit])
        n-=1
        if stat:
            break
    print a
