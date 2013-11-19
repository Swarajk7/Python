import sys
flag=True
line=sys.stdin.readline()
while line:
    if flag:
        p=line.strip()
        if int(p)!=42:
            print p
        else:
            flag=False
    line=sys.stdin.readline()
