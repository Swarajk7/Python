def main():
    N=(int)(input())
    abc=0;
    for akjhdkafka in range(N):
        abc+=1
        s="Case #"+str(abc)+": "
        C=(int)(input())
        I=(int)(input())
        A=raw_input().split(' ')
        P=[]
        for x in range(len(A)):
            P.append((int)(A[x]))
        a=-1
        b=-1
        for x in range(len(P)):
            if C-P[x] in P:
                a=x;
                b=P.index(C-P[x],x);
                break;
        if(a>b):
            s+=str(b+1)+' '+str(a+1)
        else:
            s+=str(a+1)+' '+str(b+1)
        print s
if __name__=='__main__':
    main()
