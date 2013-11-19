a=[]
from math import sqrt
hsh=[0]*1001
for i in range(1,32):
    a.append(i*i)

def sqr2(n):
    for i in a:
        for j in a:
            if i+j==n:
                return True
    return False

def sqr3(n):
    for i in a:
        for j in a:
            for k in a:
                if i+j+k==n:
                    return True
    return False

for j in range(1,1001):
    if int(sqrt(j))==sqrt(j):
        hsh[j]=1
    elif sqr2(j):
        hsh[j]=2
    elif sqr3(j):
        hsh[j]=3
    else:
        hsh[j]=4
print hsh
