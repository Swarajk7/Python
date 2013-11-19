import sys
if __name__=='__main__':
    n,q=sys.stdin.readline().split()
    n=int(n)
    q=int(q)
    row=[0]*n
    col=[0]*n
    for abc in range(q):
        a=sys.stdin.readline().split()
        if a[0]=='RowAdd':
            row[int(a[1])-1]+=int(a[2])
        else:
            col[int(a[1])-1]+=int(a[2])
    print max(row)+max(col)
