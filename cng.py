def y(a,b,n):
	if n==0:
		return True
	if n<0:
		return False
	return y(a,b,n-a) or y(a,b,n-b)
import sys
if __name__=='__main__':
    t=int(sys.stdin.readline())
    for i in range(t):
        a,b=sys.stdin.readline().split()
        a=int(a)
        b=int(b)
        p=(a*b)-1
        while p>0:
            if not y(a,b,p):
                print p
                break
            p-=1
            
