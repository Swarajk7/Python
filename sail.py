import sys
if __name__=='__main__':
    m,sx,sy,ex,ey=sys.stdin.readline().split()
    d=sys.stdin.readline()
    sx=int(sx)
    sy=int(sy)
    ex=int(ex)
    ey=int(ey)
    c=0
    stat=False
    for i in d:
        #print i,sx,sy
        if sx==ex and sy==ey:
            stat=True
            break
        if i=='N':
            if ey>sy:
                sy+=1
        elif i=='S':
            if ey<sy:
                sy-=1
        elif i=='W':
            if ex<sx:
                sx-=1
        else:
            if ex>sx:
                sx+=1
        c+=1
    if stat:
        print c
    else:
        print '-1'
