def x(s):
    p=''
    for i in s:
        p+=i
    return p
n=int(input())
a=[]
for i in range(n):
    s=list(raw_input().strip())
    s.sort()
    a.append(s)
arr=map(x,a)
arr.sort()
tmp=arr[0]
c=0
for i in range(1,n):
    if arr[i]!=tmp:
        tmp=i
        c+=1
print c
