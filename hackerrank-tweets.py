import sys
if __name__=='__main__':
    n=int(sys.stdin.readline())
    count=0
    for i in range(n):
        a=sys.stdin.readline()
        a=a.lower()
        if a.find('hackerrank')!=-1:
            count+=1
    print count
