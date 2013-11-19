def check(b,ind,c):
    i=ind
    while i<len(b):
        if b[i]==c:
            return i
        i+=1
    return -1
a=raw_input()
b=raw_input()
i=0
index=0
co=0
if a[0]==b[0]:
    co+=1
i+=1
while i<len(a):
    index1=check(b,index+1,a[i])
    print a[i],index1
    if index1!=-1:
        index=index1
        co+=1
        #print index
    i+=1
print co
        
    
