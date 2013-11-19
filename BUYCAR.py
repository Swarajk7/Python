def main():
    t=int(input())
    for xx in range(t):
        n=int(input())
        maxp=0
        maxpmaxb=0
        a=[]
        ind=-1
        for j in range(n):
            name,price,i=raw_input().split()
            a.append(name)
            price=int(price[1:])
            i=int(i[:-1])
            if j==0:
                maxp=price+(price*i)/100
                maxpmaxb=price
                ind=0
            else:
                x=price+(price*i)/100
                if x>=maxp:
                    if price>=maxpmaxb:
                        maxpmaxb=price
                        ind=j
        print a[ind]
                
if __name__=='__main__':
    main()
