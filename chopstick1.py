import sys
if __name__=='__main__':
    n,d=sys.stdin.readline().split()
    n=int(n)
    d=int(d)
    count=0
    a=[]
    for abc in range(n):
        a.append(int(sys.stdin.readline()))
    a.sort()
    i=0
    while i<n-1:
        if a[i+1]-a[i]<=d:
            count+=2
            i+=2
        else:
            i+=1
    print count/2
            
