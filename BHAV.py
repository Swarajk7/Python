from math import ceil
def main():
    n=int(input())
    for xxx in range(n):
        a,b,c=map(int,raw_input().split())
        x=a-b
        y=ceil(x/2.0)
        if y<=c:
            print "YES",int(y)
        else:
            print "NO"
if __name__=='__main__':
    main()
