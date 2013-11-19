if __name__=='__main__':
    a,b,c,d=raw_input().split()
    a=float(a)
    b=int(b)
    c=float(c)
    d=int(d)
    r=(1-a/b)*(1-c/d)
    s=(1/(1-r))*(a/b)
    print s
