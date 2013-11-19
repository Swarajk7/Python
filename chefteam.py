import sys,math
def C(n,r):
	return math.factorial(n)/(math.factorial(r)*math.factorial(n-r))
if __name__=='__main__':
    t=int(sys.stdin.readline())
    for i in range(t):
        a,b=sys.stdin.readline().split()
        if int(b)>int(a) :
            print '1'
        else:
            print C(int(a),int(b))
