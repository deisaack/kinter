from tkinter import *
from tkinter import ttk

root = Tk()

Label(root, text="Description").grid(row=0, sticky=W, column=0)
Entry(root, width=50).grid(row=0, column=1)

Button(root, text="Submit").grid(row=0, column=8)

Label(root, text="Quality").grid(row=1, sticky=W, column=0)
Radiobutton(root, text="New", value=1).grid(row=2, column=0, sticky=W)
Radiobutton(root, text="Good", value=2).grid(row=3, column=0, sticky=W)
Radiobutton(root, text="Poor", value=3).grid(row=4, column=0, sticky=W)
Radiobutton(root, text="Damaged", value=4).grid(row=5, column=0, sticky=W)

root.mainloop()
