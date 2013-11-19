def f3(a):
    return list(filter(lambda t: t[1]==max(a.values()), a.items()))
def getmax(a):
    temp=a[0][0]
    for i in a:
        if i<temp:
            temp=i
    return i
def main():
    m,n=raw_input().split()
    m=int(m)
    n=(int)(n)
    man=[]
    con=[]
    req=[]
    for i in range(m):
        a,b=raw_input().split()
        man.append((a,0))
        con.append((b,0))
        req.append((a,b))
    a=dict(man)
    b=dict(con)
    req=dict(req)
    for j in range(n):
        x=raw_input()
        a[x]+=1
        b[req[x]]+=1
    print getmax(f3(b))
    print getmax(f3(a))
if __name__=='__main__':
    main()
