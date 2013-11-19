if __name__=='__main__':
    import sys
    n=int(sys.stdin.readline())
    lucky=[4,7,47,74,447,474,477,744,774,444,777,747]
    stat=False
    for i in lucky:
        if n%i==0:
            stat=True
            break
    if stat:
        print 'YES'
    else:
        print 'NO'
