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
    n=10**18-1
    a=[]
    while n>0:
        if isprime(n):
            a.append(n)
        n-=2
    print a
if __name__=='__main__':
    main()
