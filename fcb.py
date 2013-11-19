def main():
    t=(int)(input())
    for xasdada in range(t):
        a=raw_input().split(' ')
        n=(int)(a[0])
        k=(int)(a[1])
        i=1
        if(n==2):
            ans=0
        else:
            ans=1
        while i<=(n-2):
            ans=(ans*k)%1000000007
            i+=1
        ans=(ans+k)%1000000007
        print ans
if __name__=='__main__':
    main()
        
