class Test:
    def __init__(self):
        self.value=0
    def __init__(self,val):
        self.value=val
    def __add__(self,val):
        return Test(self.value+val)
t=Test(5)
t1=t+9
t2=Test(2)+t1.value
print t2.value
