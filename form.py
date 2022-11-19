from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import os

def button1():
    tkMessageBox.showinfo('Thanks for like!')

top = Tk()
top.geometry('300x520')
name = Label(top, text = 'Hi', background = 'green', fg = 'white').place(x = 30, y = 50)
place = Label(top, text = 'Press', background = 'green', fg = 'white').place(x = 30, y = 90)
lol = Label(top, text = 'Like', background = 'green', fg = 'white').place(x = 30, y = 130)
img = Image.open('cat2.jpg')
img = ImageTk.PhotoImage(img)
button = Button(top, text = 'Like', fg = 'pink', bg = 'red', height = '3', width = '5', command = lambda: top.quit()).place(relx = '0.5', rely= '0.9')
cat = Label(top, image = img).place(x = 20, y = 200)
e1 = Entry(top).place(x = 90, y = 50)
e2 = Entry(top).place(x = 90, y = 90)
e3 = Entry(top).place(x = 90, y = 130)

top.mainloop()