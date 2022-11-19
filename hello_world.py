from tkinter import *
parent = Tk()
redbutton = Button(parent, text = 'Red', fg = "green").grid(row = 0, column = 0)
e1 = Entry(parent).grid(row = 0, column = 1)
oassword = Label(parent, text ="Password").grid(row = 1, column = 0)
e2 = Entry(parent).grid(row = 1, column = 1)
parent.mainloop()