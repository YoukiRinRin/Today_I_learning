from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Checkbutton 1')

# Frame
frame1 = ttk.Frame(root, padding=(10))
frame1.grid()

# Checkbutton 1
v1 = StringVar()
v1.set('0') # 初期化
cb1 = ttk.Checkbutton(
    frame1, padding=(10), text='Option 1',
    variable=v1,
    command=lambda: print('v1 = %s' % v1.get()))

# Checkbutton 2
v2 = StringVar()
# v2.set('B') # 初期化しない
cb2 = ttk.Checkbutton(
    frame1, padding=(10), text='Option 2',
    onvalue='A', offvalue='B',
    variable=v2,
    command=lambda: print('v2 = %s' % v2.get()))

# Button
button1 = ttk.Button(
    frame1, text='Show values',
    command=lambda: print('v1 = %s, v2 = %s' % (v1.get(), v2.get())))

# Layout
cb1.grid(row=0, column=0)
cb2.grid(row=0, column=1)
button1.grid(row=1, column=0, columnspan=2)

root.mainloop()