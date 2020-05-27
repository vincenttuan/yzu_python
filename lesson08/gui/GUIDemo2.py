import tkinter

win = tkinter.Tk()

win.title('我的小視窗')
label1 = tkinter.Label(win, text='Hello1')
label2 = tkinter.Label(win, text='Hello2')
label3 = tkinter.Label(win, text='Hello3')
label4 = tkinter.Label(win, text='Hello4')
label5 = tkinter.Label(win, text='Hello5')
label1.grid(column=0, row=0)
label2.grid(column=1, row=0)
label3.grid(column=1, row=1)
label4.grid(column=2, row=2)
label5.grid(column=2, row=0)

win.geometry('300x300')

win.mainloop()