from Tkinter import *
import sys
def x(event):
    print 'X'
def y(event):
    print 'Y'
    sys.exit(0)
wid=Button(None,text='abc')
wid.pack()
wid.bind('<Button-1>',x)
wid.bind('<Double-1>',y)
wid.mainloop()
