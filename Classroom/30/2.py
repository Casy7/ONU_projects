from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox as mb
import pyperclip

def delText():
    answer = mb.askokcancel('Удаление текста', 'Реально удалить?')
    if answer == True:
        text.delete(1.0, END)


def іnsertText():
    file_name = fd.askopenfilename()
    global file_path
    file_path = file_name
    try:

        f = open(file_name,"r")
    except:

        mb.showinfo("Открытие файла", "Файл не выбран")
    else:

        s = f.read()
        text.insert(1.0, s)
        f.close()

def saveTextAs():
    file_name = fd.asksaveasfilename()
    global file_path
    file_path = file_name    
    try:

        f = open(file_name, 'w')
    except (FileNotFoundError, TypeError):

        mb.showinfo("Сохранение файла", "Файл не сохранён")
        global is_saved
        is_saved = False
    else:

        s = text.get(1.0, END)
        f.write(s)
        f.close()
        global saved_text
        saved_text = s


def extractText():
    global file_path
    if file_path == None:
        file_name = fd.asksaveasfilename()
        file_path = file_name
    else:
        file_name = fd.asksaveasfilename()

    try:

        f = open(file_path, 'w')
    except (FileNotFoundError, TypeError):

        mb.showinfo("Сохранение файла", "Файл не сохранён")
        global is_saved
        is_saved = False
    else:

        s = text.get(1.0, END)
        f.write(s)
        f.close()
        global saved_text
        saved_text = s


def on_closing():
    if saved_text != text.get(1.0, END):
        quli = mb.askokcancel("Выход", "Изменения не сохранены. Сохранить?")
        if quli:
            extractText()
            if is_saved:
                root.destroy()
        else:
            root.destroy()  
    else:
        root.destroy()

def paste():
    s = pyperclip.paste()
    text.insert(float(text.index(INSERT)), s)


is_saved = True
saved_text = ""
file_path = None


root = Tk()

mainmenu = Menu() 
root['menu'] = mainmenu
mainmenu.add_command(label = "Открыть", command=іnsertText) 
mainmenu.add_command(label="Сохранить", command=extractText)
mainmenu.add_command(label="Сохранить как", command=saveTextAs)



text = Text()
text.pack()


popupmenu = Menu()
text.bind('<Button-3>', lambda event: popupmenu.post(event.x_root, event.y_root))
popupmenu.add_command(label="Очистить всё", command=delText)
popupmenu.add_command(label="Вставить", command=paste)



# text = Text(width=50, height=25)
# text.grid(row=1, columnspan=4)

# b3 = Button(text="СОХРАНИТЬ КАК", command=saveTextAs) 
# b3.grid(row=2, column=2, sticky=W)


# b4 = Button(text="ОЧИCТИТЬ", command=delText)
# b4.grid(row=2, column=3, sticky=E)

root.protocol("WM_DELETE_WINDOW", on_closing)
# root.geometry("555*444")
root.mainloop()