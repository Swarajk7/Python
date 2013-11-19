def f(n,k,a,o,arr,a1):
    for i in range(k):
        if o=='XOR':
            a=a1^a
        elif o=='AND':
            a=a1&a
        elif o=='OR':
            a=a1|a
    return a
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
        for i in arr:
            if o=='XOR':
                a1=a1^i
            elif o=='AND':
                a1=a1&i
            elif o=='OR':
                a1=a1|i
        print f(n,k,a,o,arr,a1)
