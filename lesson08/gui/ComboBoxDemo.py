import tkinter
from tkinter import ttk

win = tkinter.Tk()
win.geometry('300x300')

fruits = ['apple', 'banana', 'mango', 'melonwater']
combo = ttk.Combobox(win, values=fruits, state="readonly") # readonly, disabled
combo.current(2)
combo.pack()

win.mainloop()