import re
n=int(input())
#p=re.compile('\([+-]?\d{2,}.\d*, [+-]?\d{2,}.\d*\)')
p=re.compile('\([+-]?[1-9][0-9]?(.\d+)?, [+-]?[1-9][0-9][0-9]?(.\d+)?\)')
p1=re.compile('[+-]?[1-9][0-9]?(.\d+)?..[+-]?[1-9][0-9][0-9]?(.\d+)?')
for i in range(n):
    s=raw_input().strip()
    m=p.search(s)
    if m:
        m1=p1.search(s)
        s=m1.group(0)
        s=map(float,s.split(','))
        #print s[0],s[1]
        if s[0]>90 or s[0]<-90:
            print 'Invalid'
        elif s[1]>180 or s[1]<-180:
            print 'Invalid'
        else:
            print 'Valid'
    else:
        print 'Invalid'
