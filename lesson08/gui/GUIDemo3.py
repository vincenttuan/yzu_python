import tkinter
from tkinter import messagebox

def mymessage():
    messagebox.showinfo('Message', 'Hello')

def myexit():
    win.quit()

win = tkinter.Tk()
win.geometry('300x300')

button = tkinter.Button(win, text='OK', command=mymessage)
button.pack()

button2 = tkinter.Button(win, text='Exit', command=myexit)
button2.pack()

win.mainloop()