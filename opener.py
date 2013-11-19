def removeall(c,a):
    while a in c:
        c.remove(a)

def main():
    n=(int)(input())
    A=[]
    B=[]
    C=[]
    for abc in range(n):
        a,b=raw_input().split()
        a=int(a)
        b=int(b)
        A.append(a)
        B.append(b)
        C.append(a)
    for i in range(n):
        if A[i]!=B[i]:
                removeall(C,B[i])
        elif A[i]==B[i]:
            removeall(C,B[i])
            C.append(B[i])
    print len(C)

if __name__=='__main__':
    main()
