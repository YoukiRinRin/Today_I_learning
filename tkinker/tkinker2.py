from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Button 練習')

# Frame as Widget Container
frame1 = ttk.Frame(
    root,
    padding=10)
frame1.grid()

# Label 1

label1 = ttk.Label(
    frame1)
label1.grid(row=0, column=0)

# Label 2
label2 = ttk.Label(
    frame1,
    text='あいうえお?',
    width=100,
    anchor=E,
    padding=(100))
label2.grid(row=0, column=1)

# ボタン
button1 = ttk.Button(
    frame1,
    text='OK',
    command=lambda: root.quit())
button1.grid(row=1, column=0, columnspan=2)

root.mainloop()
