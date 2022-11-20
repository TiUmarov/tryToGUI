import tkinter
from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import PIL
from PIL import *
from PIL import Image, ImageTk
import os

page = Tk(className = "Hello there..")
page.geometry('700x500')

img = Image.open('cat2.jpg')
img = ImageTk.PhotoImage(img)

def showBest():
    tkinter.messagebox.showinfo("Who is the best?", "I'm the best coder on python, for real!")
def quadroAnswer():
    answer = int(entryQuadro.get()) ** 4
    answer = "Quadro of this number is " + str(answer) +  "          "
    message = tkinter.messagebox.showinfo("How you get it?", answer , icon='warning')
def openCat():
    global my_img
    top = Toplevel()
    top.title("Got ya")
    my_img = ImageTk.PhotoImage(Image.open(r'cat2.jpg'))
    Label(top, image=my_img).pack()


firstText = Label(page, text = "That is my try to create something interesting", font = '24').place(relx = 0.2, rely = 0.1)

best = Label(page, text = "First you must to know that is ")
best.place(relx = 0.08, rely = 0.2)
bestButton = Button(page, text = 'Show', command = showBest)
bestButton.place(relx = 0.35, rely = 0.2)

tryMe = Label(page, text = 'You may to distruct my opinion, so lets try me').place(relx = 0.08, rely = 0.28)
quadroNum = Label(page, text = "Enter a number and press a button 'Give me an answer'").place(relx = 0.08, rely = 0.36)
entryQuadro = Entry(page)
entryQuadro.place(relx = 0.5, rely = 0.36)
tryMeButton = Button(page, text = "Give me an answer", command = quadroAnswer).place(relx = 0.08, rely = 0.42)

quitButton = Button(page, text = 'Quit?', command = page.quit, bg = 'red')
quitButton.place(relx = '0.01', rely = '0.9')
surpButton = Button(page, text = 'Quit?', command = openCat, bg = 'green')
surpButton.place(relx = '0.1', rely = '0.9')

page.mainloop()
