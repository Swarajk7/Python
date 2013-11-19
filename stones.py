def main():
    import psyco
    psyco.full()
    t=(int)(input())
    for abc in range(t):
        a=raw_input()
        b=[]
        for i in range(len(a)):
            b.append(a[i])
        a=raw_input()
        count=0
        for i in range(len(a)):
            if a[i] in b:
                count+=1
        print count
if __name__=='__main__':
    main()
