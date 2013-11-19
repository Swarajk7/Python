from Tkinter import *
import sys
def quit():
    print 'exiting'
    sys.exit()
root=Tk()
Button(root,text='click',command=quit).pack(side=LEFT,expand=YES,fill=X)
root.mainloop()
