def main():
    t=(int)(input())
    for abc in range(t):
        N=(int)(input())
        arr=[[0]*8]*N
        for i in range(N):
            a=raw_input().split()
            for j in range(8):
                arr[i][j]=int(a[j])
        print arr
if __name__=='__main__':
    main()
