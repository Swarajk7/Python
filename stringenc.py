if __name__=='__main__':
    a=raw_input()
    d={}
    for i in a:
        if i in d: 
            d[i]+=1
        else:
            d[i]=1
    s=''
    for i in a:
        if d[i]!=0:
            s+=i+str(d[i])
            d[i]=0
    print s
            
