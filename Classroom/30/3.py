from tkinter import *
from random import randint


def move():
    b.place(relx=randint(10,90)/100, rely=randint(10,90)/100)


root = Tk()
root['bg'] = 'white'

root.geometry('300x200')

img = PhotoImage(format='gif',file='theCaribeanSea2.gif')#, height=50, width=50)

b = Button(image=img, command=move)
b.place(relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()
