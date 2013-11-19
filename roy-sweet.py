n=int(input())
sweet={}
mx=0
for i in range(n):
    a,b=raw_input().split()
    a=int(a)
    b=int(b)
    if b>mx:
        mx=b
    sweet[a]=b
fam=[]
g=int(input())
for i in range(g):
    fam.append(int(input()))
R=0
for i in fam:
    j=i
    while True:
        if j in sweet:
            if sweet[j]>i:
                R+=(sweet[j]/i)*100
                break
        j+=1
        if j>mx:
            break
print R
