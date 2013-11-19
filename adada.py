import math
def main():
    T=(int)(input())
    for aaa in range(T):
        a=raw_input().split(' ')
        r=(int)(a[0])
        t=(int)(a[1])
        strin='Case #'+str(aaa+1)+': '
        ar1=(2*r)+1
        t1=(ar1-2)**2+(4*2*t)
        t1=t1**0.5
     #   print t1
        k=t1-ar1+2
        p=k/4
      #  print p
        k=(int)(k/4)
        print strin+str(k)
if __name__=='__main__':
    main()
            
