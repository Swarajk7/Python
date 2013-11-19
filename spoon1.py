import math
def y(n):
    p=n/2
    q=n-p
    return math.factorial(n)/(math.factorial(p)*math.factorial(q))
def main():
    a=[]
    a.append(y(2))
    i=3
    while i>0:
        k=y(i)
        #print k
        if k<=10**18:
            a.append(k)
        else:
            break
        i+=1
    print a,len(a)
if __name__=='__main__':
    print y(64)
