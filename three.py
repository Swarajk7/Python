from Tkinter import *
def greet():
    print 'Welcome'

win=Frame()
win.pack()
Label(win,text='Frame').pack(side=LEFT)
Button(win,text='Hello',command=greet).pack(side=LEFT)
Button(win,text='Quit',command=win.quit).pack(side=RIGHT)
win.mainloop()
