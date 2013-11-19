def gen(a,j):
    if j>=len(a):
        print a
        return
    i=j
    while i<9:
        a[j]=i+1
        gen(a,j+1)
        j-=1
def main():
    a=['0','0']
    #print len(a)
    gen(a,0)
if __name__=='__main__':
    main();
