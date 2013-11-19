class BinaryCode:
    def decode(self,message):
        if len(message)==1:
            return ("NONE","NONE")
                
        a=''
        b=''
        s='0'
        flag=True
        q=int(message[0])
        x=q-int(s[0])
        if x==0 or x==1:
                s+=str(x)
        else:
                flag=False
        if flag:
            for i in range(1,len(message)-1):
                    q=int(message[i])
                    x=q-int(s[i-1])-int(s[i])
                    if x==0 or x==1:
                            s+=str(x)
                    else:
                            flag=False
                            break
            if int(message[-1])!=int(s[-1])+int(s[-2]):
                flag=False
            else:
                flag=True
        if flag:
            a=s
        else:
            a='NONE'
        s='1'
        flag=True
        q=int(message[0])
        x=q-int(s[0])
        if x==0 or x==1:
                s+=str(x)
        else:
                flag=False
        if flag:
            for i in range(1,len(message)-1):
                    q=int(message[i])
                    x=q-int(s[i-1])-int(s[i])
                    if x==0 or x==1:
                            s+=str(x)
                    else:
                            flag=False
                            break
            if int(message[-1])!=int(s[-1])+int(s[-2]):
                flag=False
            else:
                flag=True
        if flag:
            b=s
        else:
            b='NONE'
        return (a,b)

a=BinaryCode()
print a.decode("123210120")
print a.decode("11")
print a.decode("22111")
print a.decode("3")
print a.decode("12221112222221112221111111112221111")
