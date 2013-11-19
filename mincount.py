def main():
    t=(int)(input())
    n=(int)(input())
    b=raw_input().split(' ')
    c=[]
    i=0
    while 1==1:
        c.append(b.count(b[i]))
        b.remove(b[i])
        print b,len(b)
        i+=1
        if len(b)==0:
            break
    print c
if __name__=='__main__':
    main()
