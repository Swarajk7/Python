def check(n):
    k=n
    s=0
    while(n>0):
       s=s*10+(n%10)
       n/=10
    n=k*k
    p=0
    if(k==s):
        p=1
    s=0
    while(n>0):
       s=s*10+(n%10)
       n/=10
    if k*k==s and p==1:
        return True
    else:
        return False
        
def main():
    n=1
    a=[]
    count=0
    while n<=10**5:
        if(check(n)):
            count+=1
            a.append(n)
        n+=1
    print count
    print a
if __name__=='__main__':
    main();
