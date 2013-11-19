def main():
    t=(int)(input())
    for abc in range(t):
        N=(int)(input())
        if N<3:
            print 0
            continue
        res=(N+1)*(N-2)+3-(N*(N+1))/2
        print res%(10**9+7)
if __name__=='__main__':
    main()
