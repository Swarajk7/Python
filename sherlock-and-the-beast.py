import sys
if __name__=='__main__':
    t=int(sys.stdin.readline())
    for xyz in range(t):
        n=int(sys.stdin.readline())
        n5=n
        n3=0
        while n5>=0:
            if n5%3==0 and n3%5==0:
                break
            else:
                n5-=1
                n3+=1
        if n5<0:
            print -1
        else:
            s=''
            for i in range(n5):
                s+='5'
            for i in range(n3):
                s+='3'
            print s
