# In this script i just plaing with buttons and try to do like push form or some thing else

import tkinter
from tkinter import *
import tkinter.messagebox
import os

def sayHi():
    message = 'Hi ' + str(entName.get()) + '!'
    tkinter.messagebox.showinfo("Here a message for you", message)
def ext():
    page.quit()

page = Tk(className = 'Duddles with boobles')
name = Label(page, text = 'Enter your name here please: ').grid(row = 0, column = 0)
entName = Entry(page)
entName.grid(row = 0, column = 1)
#entName.pack()
button_submit = Button(page, text = 'Submit', command = sayHi)
button_submit.grid(row = 1, column = 0)
#button_submit.pack()
button_exit = Button(page, text = 'Press to close', command = ext)
button_exit.grid(row = 2, column = 0)


page.mainloop()