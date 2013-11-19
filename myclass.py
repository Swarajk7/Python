class C:
    def __init__(self,who):
        self.name=who
    def __init__(self):
        self.name=''
    def setdata(self,nam):
        self.name=nam
    def hello(self):
        print self.name
class A(C):
    def hello(self,nam):
        print 'Hello '+self.name+' and to you also '+self.nam
i=A()
i.setdata('Swaraj')
i.hello()
