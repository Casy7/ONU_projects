from tkinter import Tk, Label, Entry, Frame, Button, LEFT, CENTER, END, X


class Color ():
    def __init__(self, id):
        self.id = id
        self.button = Button(
            frame, bg=tuple_of_colors[id][0], padx=11, pady=4, command=self.get_color)
        self.button.pack(side=LEFT, fill=X)

    def get_color(self):
        lbl['text'] = tuple_of_colors[self.id][1]
        hex_of_color.delete(0, 999)
        hex_of_color.insert(0, tuple_of_colors[self.id][0])

root = Tk()
tuple_of_colors = (('#ff0000', 'Красный'),
                   ('#ff7d00', 'Оранжевый'),
                   ('#ffff00', 'Жёлтый'),
                   ('#00ff00', 'Зелёный'),
                   ('#007dff', 'Голубой'),
                   ('#0000ff', 'Синий'),
                   ('#7d00ff', 'Фиолетовый'))

lbl = Label(width=10)
hex_of_color = Entry(width=30)
frame = Frame()


lbl.pack(pady=5)
hex_of_color.pack(pady=5)
frame.pack()


for color_id in range(7):
    Color(color_id)


root.mainloop()