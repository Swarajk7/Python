if __name__=='__main__':
    t=(int)(input())
    for abc in range(t):
        p=float(input())
        q=1-p
        x=p*(1+2*q)
        y=q*(1+2*p)
        if x>y:
            print 10000*x
        else:
            print 10000*y
