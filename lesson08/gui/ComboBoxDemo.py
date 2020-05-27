import tkinter
from tkinter import ttk

win = tkinter.Tk()
win.geometry('300x300')

label = tkinter.Label(win, text='品項 : ')
#fruits = ['apple', 'banana', 'mango', 'melonwater']
fruits = {'apple':50, 'banana':60, 'mango':70, 'melonwater':25}
combo = ttk.Combobox(win, values=list(fruits.keys()), state="readonly") # readonly, disabled
combo.current(2)

# UI 布局
label.grid(column=0, row=0, padx=10, pady=10)
combo.grid(column=1, row=0, padx=10, pady=10)


win.mainloop()