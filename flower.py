N, K = raw_input().split()
N = int(N)
K = int(K)
C = []

numbers = raw_input()

i = 0
for number in numbers.split():
   C.append( int(number) )
   i = i+1
C.sort(reverse=True)
#print C,i
x=1
s=0
j=0
while j<i:
    for p in range(K):
        if j+p<N:
            s+=x*C[j+p]
    j=j+K
    x+=1
result = s
print result
