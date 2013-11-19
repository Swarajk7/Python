# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
for i in range(n):
    a=raw_input().strip()
    if len(a)%2!=0:
        print "-1"
        continue
    else:
        p=len(a)
        p=p/2
        print p
        a1=list(a[:p])
        a2=list(a[p:])
        q=len(set(a1).intersection(set(a2)))
        print p-q
