import threading,time
lock=threading.Lock()
class myThread(threading.Thread):
    def __init__(self,threadId,name,delay):
        threading.Thread.__init__(self)
        self.tid=threadId
        self.name=name
        self.delay=delay
    def run(self):
        print "Starting Thread  "+self.name+'\n'
        lock.acquire()
        print_time(self.name,self.delay)
        lock.release()
def print_time(name,delay):
    count=5
    while count:
        time.sleep(delay)
        print "%s: %s" %(name,time.ctime(time.time()))
        count-=1

myth=[]
#create new threads
thread1=myThread(1,"One",1)
thread2=myThread(2,"Two",1)
#start threads
thread1.start()
thread2.start()
#add threads to list
myth.append(thread1)
myth.append(thread2)

for t in myth:
    t.join()
print "Exiting Main Thread"
