if __name__=='__main__':
    a=[0]*26
    print a
    t=(int)(input())
    b=raw_input()
    for i in b:
        print i
        if i>=65 and i<=91:
            a[int(i)-65]+=1
        elif i>=97 and i<=119:
            a[int(i)-97]+=1
    print a
