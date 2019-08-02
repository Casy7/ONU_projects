# TODO Create function "get_product" wich gets properties by ID

import csv
import functions
import pyperclip
from tkinter import *
import sys

SID = functions.get_key()
counter_btn_clicked= [0]
def get_text_clipboard():
    category = pyperclip.paste()
    txt.delete(0,END)
    txt.insert(0,category)

def del_text_from_txt():
    txt.delete(0,END)

def clicked():
    category = txt.get()
    lbl.configure(text=category+"? Тяжёлый случай...")
    btn.configure(text="Ну, типа, всё?")
    counter_btn_clicked[0] +=1
    try:
        example_ssd = functions.category_to_list(
            functions.numb_of_category(category), SID=SID)
        with open("import_2.csv", "w", encoding="UTF8") as write_file:
            writer = csv.writer(write_file, delimiter=',')
            for line in example_ssd:
                writer.writerow(line)      
    except:
        lbl_after.configure(text = "Такой категории нет.")
        pass


window = Tk()
window.geometry('400x250')
window.title("CoolImporter V.3.14.15 pro super max etc.")
lbl = Label(window, text="Введите точное название категории:", padx = 5)
lbl_after = Label(window, text="")
txt = Entry(window, width=30)
btn = Button(window, text="Импорт", command=clicked)
btn_copy = Button(window, text="Буфер", command=get_text_clipboard)
btn_del = Button(window, text="Очистить", command=del_text_from_txt)
lbl.grid(column=0, row=0)
btn.grid(column=0, row=2)
txt.grid(column=0, row=1)
btn_del.grid(column=3, row=1)
btn_copy.grid(column=1, row=1)
lbl_after.grid(column=0, row=3)
txt.focus()
window.mainloop()

# print(functions.get_IDs())
# print(functions.get_props(525078, SID))
# functions.good_view(525078)
# print(functions.get_categories(SID))
# functions.good_view(functions.get_props(47, SID), SID)
