def main():
    import math,sys
    t=(int)(sys.stdin.readline())
    for abc in range(t):
        n=(int)(input())
        i=math.log(n,2)
        i=int(i)
        print 2**i
if __name__=='__main__':
    main()
