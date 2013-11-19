def main():
    t=(int)(input())
    for nnn in range(t):
        a=raw_input().split(' ')
        n=(int)(a[0])
        k=(int)(a[1])
        b=[]
        a=raw_input().split(' ')
        for i in range(n):
            b.append((int)(a[i]))
        b.sort()
        sum1=0
        sum2=0
        for i in range(k):
            sum1+=b[i]
        i=k;
        while i<n:
            sum2+=b[i]
            i+=1
        print sum2-sum1
if __name__=='__main__':
    main()
        
