import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image

def open_img(x):
    img = Image.open(x + '.png')
    img = img.resize((150, 250), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panel = tk.Label(app, image=img)
    panel.image = img
    panel.grid(column=0, row=6, padx=70, pady=10)

def submit():
    bag = lambda m: '要' if m else '不要'
    extra = lambda m: 1*nums.get() if m else 0 # 手提袋費用
    print(nums.get(), comboExample.get(), radioValue.get(), chkValue.get())
    labelValue.set("數量：{0}\n品名：{1}\n單價：{2}\n糖分：{3}\n提袋：{4}\n小計：{5}".format(nums.get(), comboExample.get(), drinks[comboExample.get()], sugar[radioValue.get()], bag(chkValue.get()), nums.get() * drinks[comboExample.get()] + extra(chkValue.get())))
    open_img(comboExample.get())

app = tk.Tk()
app.geometry('400x500')

labelTop = tk.Label(app, text="請填寫飲料單")
labelTop.grid(column=0, row=0, padx=10, sticky="W")

tk.Label(app, text="數量:").grid(column=0, row=1, padx=10, sticky="W")

nums = tk.IntVar()
nums.set(1)
entry = tk.Entry(app, width=20, textvariable=nums)
entry.grid(column=0, row=1, padx=50, sticky="W")

drinks = {'珍奶': 50, '綠茶': 30, '芒果汁': 70, '西瓜汁': 25}

tk.Label(app, text="品項:").grid(column=0, row=2, padx=10, sticky="W")
comboExample = ttk.Combobox(app,
                            values=list(drinks.keys()),
                            state="readonly")  # or disabled

comboExample.grid(column=0, row=2, padx=50, sticky="W")
comboExample.current(0)

radioValue = tk.StringVar()

sugar = {'A': '正常', 'B': '少糖', 'C': '半糖', 'D': '無糖'}
deltaX = 10
for k, v in sugar.items():
    rdio = tk.Radiobutton(app, text=v, variable=radioValue, value=k)
    rdio.grid(column=0, row=3, padx=deltaX, sticky="W")
    deltaX = deltaX + 60

chkValue = tk.BooleanVar()
chkValue.set(False)

chkExample = tk.Checkbutton(app, text='手提袋(每杯1元)', var=chkValue)
chkExample.grid(column=0, row=4, padx=10, sticky="W")

btn = tk.Button(app, text="submit", command=submit)
btn.grid(column=0, row=5, sticky="W", padx=10, pady=10)

labelValue = tk.StringVar()
label = tk.Label(app, text="", textvariable=labelValue)
label.grid(column=0, row=6, padx=30, pady=10, sticky="W")

app.mainloop()