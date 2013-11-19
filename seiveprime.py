def sieve2(n):
    loops = 0
    numbers = range(0, n)
    for prime in numbers:
        if prime < 2:
            continue
        elif prime > n ** 0.5:
            break
        for i in range(prime ** 2, n, prime):
            numbers[i] = 0
            loops += 1
    return [x for x in numbers if x > 1], loops
def main():
    (a,lo)=sieve2(10**5)
    print a,lo
if __name__=='__main__':
    main()
