import sys
flag=False
for line is sys.stdin:
    s=line.strip()
    l=len(s)
    s=''
    while i<l:
        if not flag:
            if a[i]=='/' and a[i+1]=='/':
                s+=a[i:]
                break
            if a[i]=='/' and a[i+1]=='*':
                s+=a[i]+a[i+1]
                i+=1
                flag=True
        else:
            if a[i]=='*' and a[i+1]=='/':
                s+=a[i]+a[i+1]
                flag=False
            else:
                s+=a[i]
        i+=1
    print s
                
                
        
    
        
