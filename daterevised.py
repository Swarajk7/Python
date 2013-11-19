def isleap(x):
    if (x%4==0 and x%100!=0) or x%400==0:
        return True
    else:
        return False

def getday(y,m,d):
    month=[31,28,31,30,31,30,31,31,30,31,30,31]
    i=0
    day=0
    while i<m-1:
        day+=month[i]
        i+=1
    if isleap(y) and m>2:
        d+=1
    return day+d

def getcday(y,m,d,p):
    leap=0
    c=1
    day=0
    x=p
    while x<y:
        if isleap(x):
            leap+=1
            c=4
        x+=c
    #print leap
    day+=(-p+y)*365+leap+getday(y,m,d)
    return day

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
    if y1>y2:
        print abs(getcday(y1,m1,d1,y2)-getday(y2,m2,d2))
    else:
        print abs(getcday(y2,m2,d2,y1)-getday(y1,m1,d1))

if __name__=='__main__':
    main()
