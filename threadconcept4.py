import sys,threading
lock=threading.Lock()
a=[]
class myclass(threading.Thread):
    def __init__(self,tname):
        threading.Thread.__init__(self)
        self.name=tname
    def run(self):
        lock.acquire()
        if self.name=='One':
            p=float(sys.stdin.readline())
            a.append(p)
        else:
            if len(a)!=0:
                p=a[0]
                a.remove(a[0])
                q=1-p
                x=p*(1+2*q)
                y=q*(1+2*p)
                if x>y:
                    print 10000*x
                else:
                    print 10000*y
        lock.release()
if __name__=='__main__':
    t=(int)(sys.stdin.readline())
    for abc in range(t):
        t1=myclass('One')
        t2=myclass('Two')
        t1.start()
        t2.start()
        t1.join()
        t2.join()
