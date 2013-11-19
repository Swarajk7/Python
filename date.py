def getday(m,d):
    month=[31,28,31,30,31,30,31,31,30,31,30,31]
    i=0
    day=0
    while i<m-1:
        day+=month[i]
        i+=1
    return day+d
def check(x,y):
    leap=0
    c=1
    #print x,y
    if x>y:
        t=x;
        x=y;
        y=t;
    while x<=y:
        if (x%4==0 and x%100!=0) or x%400==0:
            leap+=1
            c=4
            #print x
        x+=c
    #print leap
    return leap
def main():
    d1=raw_input()
    d2=raw_input()
    y1,m1,d1=d1.split(':')
    y2,m2,d2=d2.split(':')
    y1=int(y1)
    d1=int(d1)
    m1=int(m1)
    y2=int(y2)
    d2=int(d2)
    m2=int(m2)
    leap=0
    x=min(y1,y2)
    y=max(y1,y2)
    if y1<y2:
        if m1>2:
            x=y1+1
        if m2<2:
            y=y2-1
    elif y1>y2:
        if m2>2:
            x=y2+1
        if m1<2:
            y=y1-1
    if y1==y2:
        if m1<2 and m2>2:
            leap=1
        elif m1>2 and m2<2:
            leap=1
        elif min(m1,m2)==2 and max(m1,m2)!=2:
            leap=1
    if x!=y:
        leap=check(x,y)
    #print leap
    #print getday(m1,d1),getday(m2,d2)
    if y1>y2:
        print abs(y1-y2)*365+getday(m1,d1)-getday(m2,d2)+leap
    elif y1<y2:
        print abs(y1-y2)*365-getday(m1,d1)+getday(m2,d2)+leap
    else:
        print leap+abs(getday(m1,d1)-getday(m2,d2))
if __name__=='__main__':
    main()
