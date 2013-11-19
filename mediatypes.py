import sys
if __name__=='__main__':
    n,q=sys.stdin.readline().split()
    n=int(n)
    q=int(q)
    ext=[]
    val=[]
    for abc in range(n):
        a=sys.stdin.readline().split()
        ext.append(a[0])
        val.append(a[1])
    length=len(ext)
    for i in range(q):
        a=sys.stdin.readline().split('.')
        stat=True
        for j in range(length):
            #print a[-1]+'>'
            if ext[j]==a[-1].strip():
                print val[j]
                stat=False
                break
        if stat:
            print 'unknown'
                        
