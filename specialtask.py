import sys
if __name__=='__main__':
    ques=0
    count=0
    p=0
    ans=1
    c=sys.stdin.readline()
    a=[0]*26
    if c[0]=='?':
        ans=9
    s=''
    if ord(c[0])>=65 and ord(c[0])<=91:
        ans=9
        for i in c:
            if i==c[0]:
                s+='1'
            else:
                s+=i
        p=1
    if s=='':
        s=c
    for i in range(1,len(s)):
        #print s[i]
        if s[i]=='?':
            ques+=1
        elif ord(s[i])>=65 and ord(s[i])<=91:
            if a[ord(c[i])-65]==0:
                a[ord(c[i])-65]=1
                count+=1
    #print count,ques,s
    for i in range(ques):
        ans*=10
    for i in range(count):
        ans*=(10-i-p)

    print ans
        
