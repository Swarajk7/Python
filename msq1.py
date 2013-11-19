import sys
if __name__=='__main__':
    t=int(sys.stdin.readline())
    for i in range(t):
        a=[]
        p=sys.stdin.readline()
        p=p.strip()
        c=0
        x=0
        while not (ord(p[x])>=65 and ord(p[x])<=90):
            x+=1
            #print x
        p=p[x:].lower()
        for i in p:
            if i not in a:
                a.append(i)
                c+=1
        print c
