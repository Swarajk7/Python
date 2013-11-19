if __name__=='__main__':
    p=float(input())
    q=1-p
    if p*(1+2*q)>q*(1+2*p):
        print 10000*p*(1+2*q)
    else:
        print 10000*q*(1+2*p)
