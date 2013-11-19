def isprime(n):
    if n == 2: return True
    if n == 3: return True
    if n % 2 == 0: return False
    if n % 3 == 0: return False
    i = 5
    w = 2
    while i * i <= n:
       if n % i == 0:
          return False
       i += w
       w = 6 - w
    return True

def main():
    t=(int)(input())
    for abc in range(t):
        n=(int)(input())
        #n=10**2-1
        if n==2:
            print 2
            continue
        #a=[]
        elif n%2==0:
            n-=1
        while n>0:
            if isprime(n):
                break
            n-=2
        print n
if __name__=='__main__':
    main()
