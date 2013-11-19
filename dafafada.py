def main():
    t=(int)(input())
    vow=['a','e','i','o','u']
    for abc in range(t):
        a,n=raw_input().split(' ')
        n=int(n)
        i=0
        con=0
        while i<len(a)-n:
            j=i
            co=0
            while j<n+i:
                if a[j] not in vow:
                    co+=1
                j+=1
            if co==n:
                con+=1
            i+=1
        print con
if __name__=='__main__':
    main()
