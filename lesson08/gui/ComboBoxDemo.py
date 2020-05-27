import tkinter
from tkinter import ttk

win = tkinter.Tk()
win.geometry('300x300')

label = tkinter.Label(win, text='品項 : ')
#fruits = ['apple', 'banana', 'mango', 'melonwater']
fruits = {'apple':50, 'banana':60, 'mango':70, 'melonwater':25}
combo = ttk.Combobox(win, values=list(fruits.keys()), state="readonly") # readonly, disabled
combo.current(2)
label2 = tkinter.Label(win, text='甜度 : ')

rdio1 = tkinter.Radiobutton(win, text='正常', value=1.0)
rdio2 = tkinter.Radiobutton(win, text='少糖', value=0.7)
rdio3 = tkinter.Radiobutton(win, text='半糖', value=0.5)
rdio4 = tkinter.Radiobutton(win, text='微糖', value=0.3)
rdio5 = tkinter.Radiobutton(win, text='無糖', value=0)

# UI 布局
label.grid (column=0, row=0, padx=10, pady=10)
combo.grid (column=1, row=0, padx=10, pady=10)
label2.grid(column=0, row=1, padx=10, pady=10)


win.mainloop()