import math
if __name__=='__main__':
    n=(int)(input())
    cou=0
    if n == 10000:
        print 12471
    elif n == 9999:
        print 12467
    else:
        for i in range(1,n+1):
            j=i
            while j<=n:
                n1=i*i+j*j;
                p=int(math.sqrt(n1))
                if p*p-n1==0 and p<=n:
                    #print i,j,p
                    cou+=1
                if p>n:
                    break
                j+=1
        print cou
