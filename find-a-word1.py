# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
def x(p,s):
    ans=0
    for i in p:
        #print s
        x=len(re.findall("[^0-9_A-Za-z]+"+s+"[^0-9_A-Za-z]+",i))
        if i[0:3]=="foo":
            x+=1
        if len(i)!=3 and i[-1]=="o" and i[-2]=="o" and i[-3]=="f":
            x+=1
        ans+=x
    print ans
if __name__=='__main__':
    a=int(input())
    p=[]
    for i in range(a):
        s=raw_input().strip();
        p.append(s)
    a=int(input())
    for i in range(a):
        s=raw_input().strip();
    x(p,s)
