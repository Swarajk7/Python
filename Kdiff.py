N,K=raw_input().split(' ')
N=int(N)
K=int(K)
a=raw_input()
b=[]
for number in a.split(' '):
    b.append((int)(number))
i=0
j=0
count=0
while i<len(b):
    j=i+1
    while j<len(b):
        if abs(b[j]-b[i])==K:
            count+=1
        j+=1
    i+=1
print count
