import random
def p():
    a=random.randint(1,10)
    s=str(a)+'\n'
    k=100000
    for j in range(a):
        k=random.randint(1,k)
        s+=str(k)+' '
    return s

if __name__=='__main__':
    fil=open('testmandi.txt','w')
    fil.write(str(1)+'\n')
    fil.write(p()+'\n')
    fil.close()
