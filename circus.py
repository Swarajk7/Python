import sys
def x(a,b):
    if a[0]>b[0]:
        return 1
    elif a[0]<b[0]:
        return -1
    else:
        if a[1]<=b[1]:
            return 1
        else:
            return -1
if __name__=='__main__':
    ht=[(65,100),(70,150),(56,60),(75,190),(60,95),(68,110)]
    #ht=[(2,4),(1,5),(4,2),(3,3),(5,1)]
    ht.sort(cmp=x)
    print ht
    dp=[0]*len(ht)
    dp[0]=1
    noc=0
    for i in range(1,len(ht)):
        noc+=1
        j=i-1
        while ht[j][1]>ht[i][1]:
            j-=1
            noc+=1
        dp[i]=dp[j]+1
    print max(dp),noc
