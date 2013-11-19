import threading
import time
exitFlag=0
class myThread(threading.Thread):
    def __init__(self,threadId,threadName,delay):
        threading.Thread.__init__(self)
        self.Id=threadId
        self.name=threadName
        self.delay=delay
    def run(self):
        print "Strating "+self.name
        print_time(self.name,self.delay)
        print "Exiting  "+self.name
def print_time(name,delay):
    count=5
    while count:
        if exitFlag:
            thread.exit()
        #time.sleep(delay)
        print "%s: %s" %(name,time.ctime(time.time()))
        count-=1
thread1=myThread(1,"One",0.2)
thread2=myThread(1,"Two",0.2)
thread1.start()
thread2.start()
print "Exiting Main Thread"
