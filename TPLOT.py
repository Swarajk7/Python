a=map(int,raw_input().split())
val=a.pop()
for i in range(5):
    reg=0
    bon=0
    b=map(int,raw_input().split())
    for i in b:
        if i in a:
            reg+=1
        if i==val:
            bon+=1
    if reg==6:
        print "First Parking slot"
    elif reg==5 and bon==1:
        print  "Second Parking slot"
    elif reg==5:
        print  "Third Parking slot"
    elif reg==4:
        print "Fourth Parking slot"
    elif reg==3:
        print "Fifth Parking slot"
    else:
        print "No Parking slot"
    
