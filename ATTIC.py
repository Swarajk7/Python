import sys
if __name__=='__main__':
    n=int(sys.stdin.readline())
    for abc in range(n):
        a=sys.stdin.readline()
        tmp=0
        maxt=0
        c=0
        for i in a:
            if i=='.':
                tmp+=1
            else:
                if tmp>maxt:
                    c+=1
                    maxt=tmp
                tmp=0
        print c
