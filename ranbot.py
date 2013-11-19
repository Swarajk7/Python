import sys
if __name__=='__main__':
    n=int(sys.stdin.readline())
    ar=set([])
    for i in range(n):
        inp=sys.stdin.readline().split()
        if inp[0].strip()=='add':
            ar.add((int(inp[1]),int(inp[2])))
        elif inp[0].strip()=='erase':
            ar.remove((int(inp[1]),int(inp[2])))
        else:
            q=1
        print ar
