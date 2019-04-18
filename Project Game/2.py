from tkinter import *
root = Tk()
b1 = Button(text="Изменить", width=4, height=4)
 
def change():
    b1[''] = "Изменено"
    b1['bg'] = '#ffffff'
    b1['activebackground'] = '#ffffff'
    b1['fg'] = '#ffffff'
    b1['activeforeground'] = '#ffffff'
 
b1.config(command=change)
 
b1.pack()
root.mainloop()