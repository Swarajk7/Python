if __name__=='__main__':
    m,n,a=raw_input().split()
    import math
    m=int(m)
    n=int(n)
    a=float(a)
    print int(math.ceil(m/a)*math.ceil(n/a))
    
