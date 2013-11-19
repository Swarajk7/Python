import sys
if __name__=='__main__':
    xx=[0]*(10**9+2)
    for i in range(1000):
        for j in range(1000):
            p=i*i+j*j
            if p<=10**9:
                xx[p]=1
    print xx
    
