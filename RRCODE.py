import sys
if __name__=='__main__':
    t=int(sys.stdin.readline())
    for xyz in range(t):
        n,k,a=sys.stdin.readline().split()
        n=int(n)
        k=int(k)
        a=int(a)
        p=sys.stdin.readline().split()
        arr=[int(i) for i in p]
        o=sys.stdin.readline().strip()
        a1=a
        if k!=0:
            for i in arr:
                if o=='XOR':
                    a1=a1^i
                elif o=='AND':
                    a1=a1&i
                elif o=='OR':
                    a1=a1|i
        if k%2==0 and o=='XOR':
            a1=a
        print a1
