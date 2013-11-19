def init():
    ar=[]
    ar.append(1)
    ar.append(2)
    while ar[-1]<=10**18:
        ar.append(ar[-1]+ar[-2])
    return ar

def gcd(a,b):
    if a<b:
        return gcd(b,a)
    elif b==0:
        return a
    else:
        return gcd(b,a%b)

def search(x):
    a=init()
    for i in a:
        #print i
        if gcd(i,x)!=1:
            return (i,gcd(i,x))

def main():
    a=int(input())
    for i in range(a):
        p=int(input())
        ax=search(p)
        print ax[0],ax[1]

if __name__=='__main__':
    main()
