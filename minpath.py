def main():
    t=(int)(input())
    for abc in range(t):
        X,Y=raw_input().split()
        x=int(X)
        y=int(Y)
        i=0
        j=0
        n=1
        s=''
        co=0
        while 1:
            print i
            if x>=i+n:
                s+='E'
                if x==i+n:
                    n+=1
                    break
                i=i+n
            elif x<i or x<i+n:
                s+='W'
                if x==i+n:
                    break
                i=i-n
            else:
                break
            n+=1
            print s,i
            print ''
            co+=1
            if co>=500:
                break
        while 1:
            print j
            if y>j and y>=j+n:
                s+='N'
                if y==j+n:
                    break
                j=j+n
            elif y<j or y<j+n:
                s+='S'
                if y==j+n:
                    break;
                j=j-n
            else:
                break
            print s,n+j
            print ''
            n+=1
            co+=1
            if co>=500:
                break
        print 'Case #'+str(abc+1)+': '+s
if __name__=='__main__':
    main()
                
                
