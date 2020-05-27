import tkinter

def myadd():
    num.set(num.get() + 1)


win = tkinter.Tk()
win.geometry('300x300')

num = tkinter.IntVar()
num.set(0)

label = tkinter.Label(win, textvariable=num)
label.pack()

button = tkinter.Button(win, text='Add', command=myadd)
button.pack()


win.mainloop()