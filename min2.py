t=(int)(input())
for abc in range(t):
    c=(int)(input())
    n=(int)(input())
    l=[]
    a=raw_input().split(' ')
    for x in a:
        l.append((int)(x))
    for i in range(n):
        if c-l[i] in l:
            try:
                p=l.index(c-l[i],i+1)
                if p>i:
                    print i+1,p+1
                    cc+=1
                    break
            except: 
                p=l.index(c-l[i],i)
                if p==i:
                    print i+1,p+1
                    break
