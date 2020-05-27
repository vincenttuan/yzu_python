import tkinter

win = tkinter.Tk()

win.title('我的小視窗')
label = tkinter.Label(win, text='Hello')
label.pack(side=tkinter.LEFT)
label2 = tkinter.Label(win, text='Hello2')
label2.pack(side=tkinter.RIGHT)

win.geometry('300x300')

win.mainloop()