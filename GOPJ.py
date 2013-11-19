import sys
def ans(n,b,i,val):
    if n==i or n==0:
        return val+i
    if b==val+i:
        return ans(n,b,i+1,val)
    else:
        return ans(n,b,i+1,val+i)
def main():
    t=int(sys.stdin.readline())
    for i in range(t):
        n,b=sys.stdin.readline().split()
        print ans(int(n),int(b),0,0)
if __name__=='__main__':
    main()
