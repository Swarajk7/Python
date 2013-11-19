import sys
def ans(n):
    if n==1:
        return 0
    else:
        if n%2==0:
            return ans(n/2)
        else:
            return ans(n/2+1)+1
if __name__=='__main__':
    t=int(sys.stdin.readline())
    for i in range(1,t):
        #n=int(sys.stdin.readline())
        print i,'-->',ans(i)
