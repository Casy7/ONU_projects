from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox as mb


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


is_saved = True
saved_text = ""
file_path = None


root = Tk()


text = Text(width=50, height=25)
text.grid(row=1, columnspan=4)

b1 = Button(text="ОТКРЫТЬ", command=іnsertText)
b1.grid(row=2, column=0, sticky=E)

b2 = Button(text="СОХРАНИТЬ", command=extractText) 
b2.grid(row=2, column=1, sticky=W)

b3 = Button(text="СОХРАНИТЬ КАК", command=saveTextAs) 
b3.grid(row=2, column=2, sticky=W)


b4 = Button(text="ОЧИCТИТЬ", command=delText)
b4.grid(row=2, column=3, sticky=E)

root.protocol("WM_DELETE_WINDOW", on_closing)
# root.geometry("555*444")
root.mainloop()