import sys
def get(stat):
    if stat:
        return 'YES'
    else:
        return 'NO'
if __name__=='__main__':
    n=int(sys.stdin.readline())
    for i in range(n):
        a=sys.stdin.readline()
        stat=True
        for i in range(5):
            p=ord(a[i])
            if p>=65 and p<=90:
                stat=True
            else:
                stat=False
                break
        i=5
        if stat:
            while i<=8:
                p=ord(a[i])
                if p>=48 and p<=57:
                    stat=True
                else:
                    stat=False
                    break
                i+=1
        if stat:
            p=ord(a[i])
            if p>=65 and p<=90:
                stat=True
            else:
                stat=False
        print get(stat)
                
            
        
