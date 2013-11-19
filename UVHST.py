from math import ceil
n=int(input())
for i in range(n):
    a,b=raw_input().split()
    a=float(a)
    b=float(b)
    print int(ceil(a/b))-1
