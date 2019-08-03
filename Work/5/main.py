# TODO Create function "get_product" wich gets properties by ID
import sys
import csv
import functions
import pyperclip
from tkinter import *
from tkinter import ttk
import sys

SID = functions.get_key()
counter_btn_clicked = [0]

def get_text_clipboard():
    category = pyperclip.paste()
    txt.delete(0, END)
    txt.insert(0, category)


def del_text_from_txt():
    txt.delete(0, END)


def clicked():
    category = txt.get()
    lbl.configure(text=category+"? Тяжёлый случай...")
    btn.configure(text="Ну, типа, всё?")
    counter_btn_clicked[0] += 1

    if functions.check_category_existing(category):
        example_ssd = functions.ids_to_list(
            functions.import_category(category), SID=SID)
        with open("import_2.csv", "w", encoding="UTF8") as write_file:
            writer = csv.writer(write_file, delimiter=',')
            for line in example_ssd:
                writer.writerow(line)
        lbl_after.configure(text="ЗАВЕРШЕНО")
    else:
        lbl_after.configure(text="Такой категории нет.")


window = Tk()
window.geometry('450x300')
window.title("CoolImporter V.3.14.15 pro super max etc.")
lines = Canvas (window)
tabs = ttk.Notebook(window)
tab1 = ttk.Frame(tabs)
tab2 = ttk.Frame(tabs)
tabs.add(tab1, text='Основной лист')
tabs.add(tab2, text='Доп. настройки')

black_list = Radiobutton (tab1, text = "Чёрный список")
white_list = Radiobutton (tab1, text = "Белый список")
# line1 = lines.create_line(1,18,180,18)
lbl = Label(tab1, text="Категории (через\"/\" или с помощью \"Add\"):")
lbl_after = Label(tab1, text="")
cat_frame = Frame(tab1)
scrollbar = Scrollbar(cat_frame)
txt = Text (cat_frame, width=35, bd = 2, yscrollcommand=scrollbar.set)
txt.config(yscrollcommand=scrollbar.set)


scrollbar.config(command=txt.yview)
btn = Button(tab1, text="Импорт", command=clicked)
btn_paste = Button(tab1, text="Буфер", command=get_text_clipboard)
btn_del = Button(tab1, text="Очистить", command=del_text_from_txt)

black_list.place(x=5, y=0)
white_list.place(x=280, y=0)
lbl.place(x=5, y=30)
cat_frame.place(x=5, y=50,width = 300, height = 150)
tabs.pack(expand=1, fill='both')
txt.pack(side=LEFT, fill=Y)
scrollbar.pack(side=RIGHT, fill=Y)
btn.place(x=320, y=245)
# txt.place(column=0, row=1, rowspan=2, columnspan=2)
# btn_del.grid(column=3, row=1)
# btn_paste.grid(column=2, row=2)
# lbl_after.grid(column=0, row=3)
txt.focus()
window.mainloop()

# print(functions.get_IDs())
# print(functions.get_props(525078, SID))
# functions.good_view(525078)
# print(functions.get_categories(SID))
# functions.good_view(functions.get_props(47, SID), SID)
