import sys
def binarySearch(dic,a,l,h):
    i=l
    j=h
    while i<=j:
        mid=(i+j)/2
        #print i,mid,j
        if dic[mid]==a:
            return True
        elif dic[mid]>a:
            j=mid-1
        else:
            i=mid+1
    return False
if __name__=='__main__':
    n,k=sys.stdin.readline().split()
    n=int(n)
    k=int(k)
    a=sys.stdin.readline().split()
    b=[int(i) for i in a]
    b.sort()
    flag=0
    for i in range(n):
        x=b[i]
        if binarySearch(b,x+k,i+1,n-1):
            flag+=1
    print flag
