import sys
if __name__=='__main__':
    n=int(sys.stdin.readline())
    for xx in range(n):
        a=sys.stdin.readline().strip()
        p=a.split()
        if p[0].lower()=='hi':
            if len(p)>1:
                if p[1][0]!='d' and p[1][0]!='D':
                    print a.strip()
            else:
                print a.strip()
