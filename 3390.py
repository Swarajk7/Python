import sys
if __name__=='__main__':
    a=sys.stdin.readline().split('+')
    s=''
    a.sort()
    for i in range(len(a)-1):
        s+=a[i].strip()+'+'
    s+=a[-1].strip()
    print s
