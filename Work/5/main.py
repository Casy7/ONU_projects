# TODO Create function "get_product" wich gets properties by ID
import sys
import csv
import json
import functions
import pyperclip
from tkinter import *
from tkinter import ttk
import sys

SID = functions.get_key()
counter_btn_clicked = [0]
settings = {"mode": "black_list", "categories": ""}

def format_cats():
    condition.configure(text = "---")
    categories = txt.get(1.0, 999.74567)
    categories = "\n".join(categories.splitlines())
    categories = categories.split('\n')
    while categories[-1] == '':
        categories = categories[:-1]
    for index in range(len(categories)):
        categories[index].strip()
        if categories[index] == '':
            categories.pop(index)
        else:
            while categories[index][0] == ' ':
                categories[index] = categories[index][1:]
            while categories[index][-1] == ' ':
                categories[index] = categories[index][:-1]
    categories[-1].replace('\n', '')
    while categories[-1][-1] == '\n':
        categories[-1] = categories[-1][:-1]
    return categories

def check_cats():
    # TODO Исправить: пустые строки между категориями
    # ведут к ошибке
    with open("settings.json", "r", encoding="UTF8") as file:
        all_cats = json.load(file)["categories"]


    cats = format_cats()
    index = 1
    mistakes_pos = []
    for cat in cats:
        if cat not in all_cats:
            mistakes_pos.append(index)
            condition.configure(text = "Есть ошибки в именах категорий")
        index += 1
    cats_text = cats[0]
    for index in range(1, len(cats)):
        cats_text += '\n'+cats[index]

    txt.delete(1.0, 999.99)
    txt.insert(END, cats_text)
    for mistake in mistakes_pos:
        txt.tag_add(str(mistake), str(mistake)+".0", str(mistake)+".999")
        txt.tag_config(str(mistake), background="yellow")
    if mistakes_pos==[]:
        return True
    else:
        return False

def get_text_clipboard():
    category = pyperclip.paste()+"\n"
    # txt.delete(0, END)
    txt.insert(999.6, category)


def del_text_from_txt():
    txt.delete(0, END)


def start_import():
    # TODO Разобраться, почему импорт одной категории не идёт
    # TODO Сделать систему поиска дочерних категорий
    # (только листов веток)
    categories = txt.get(1.0, 999.74567)
    lbl.configure(text="Мдяя...")
    # counter_btn_clicked[0] += 1
    categories = categories.split('\n')
    for index in range(len(categories)):
        categories[index].strip()
        if categories[index] == '':
            categories.pop(index)
        elif categories[index][0] == ' ':
            categories[index] = categories[index][1:]
    if(check_cats()):
        export_list = []
        for category in format_cats():
            condition.configure(text=category+"- загружается")
            cat_to_export = functions.ids_to_list(
                functions.import_category(category), SID=SID)
            condition.configure(text="Категория \""+category+"\" загружена")
            export_list.append(cat_to_export)
        with open("import_2.csv", "w", encoding="UTF8") as write_file:
            writer = csv.writer(write_file, delimiter=',')
            for line in export_list:
                writer.writerow(line)
            



window = Tk()
window.geometry('450x300')
window.title("CoolImporter V.3.14.15 pro super max etc.")
lines = Canvas(window)
tabs = ttk.Notebook(window)
tab1 = ttk.Frame(tabs)
tab2 = ttk.Frame(tabs)
tabs.add(tab1, text='Основной лист')
tabs.add(tab2, text='Доп. настройки')

######### Categories frame #############

cat_frame = Frame(tab1)
scrollbar = Scrollbar(cat_frame)
scrollbar.pack(side=RIGHT, fill=Y)

txt = Text(cat_frame, width=35, yscrollcommand=scrollbar.set)
scrollbar.config(command=txt.yview)
txt.pack()
cat_frame.place(x=5, y=50, width=230, height=150)

#########  Mode of import  #############


def set_mode():
    mode = var.get()
    if mode == 1:
        black_list.deselect()
        white_list.select()
        settings["mode"] = "white_list"
    else:
        black_list.select()
        white_list.deselect()
        settings["mode"] = "black_list"


var = IntVar()
black_list = Radiobutton(tab1, variable=var, value=0, text="Чёрный список",
                         command=set_mode)
white_list = Radiobutton(tab1, variable=var, value=1, text="Белый список",
                         command=set_mode)

black_list.place(x=5, y=0)
white_list.place(x=280, y=0)

#########     Main UI    #############

lbl = Label(tab1, text="Категории (с новой строки):")
text_cond = Label(tab1, text="СОСТОЯНИЕ:")
condition = Label(tab1, text="---")

#########     Buttons   #############

import_btn = Button(tab1, text="Импорт", command=start_import)
paste_btn = Button(tab1, text="Буфер", command=get_text_clipboard)
del_btn = Button(tab1, text="Очистить", command=del_text_from_txt)
check_btn = Button(tab1, text="Проверить", command=check_cats)

paste_btn.place(x=5, y=200, width=80)
check_btn.place(x=85, y=200, width=80)
import_btn.place(x=385, y=245)


text_cond.place(x=5, y=225)
condition.place(x=85, y=225)
lbl.place(x=5, y=28)
tabs.pack(expand=1, fill='both')


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
