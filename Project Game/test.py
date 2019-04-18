from random import randint
from tkinter import *
root = Tk()
root.geometry("1300x720")
p=[[""]*15]*15
array_buttons=[]
i=0   
#def single_button(x1,x2,y1,y2)
def creatarrbuttons(x1,y1,x2,y2):
    iy=0
    def creat_button(root,n,y,x):
        nonlocal iy
        f = Frame(root, height=60, width=60)
        f.pack_propagate(0) # don't shrink
        array_buttons.append(Button(f, width=4, height=2, bg='#ffffff',fg="#f54f00", text="1",activebackground='#38DF64',activeforeground='#f54f00'))
        array_buttons[iy].pack(fill=BOTH, expand=1)
        iy+=1
        f.grid(row = x, column = y)
    for y in range(y1,y2+1):
        for x in range(x1,x2+1):
            creat_button(root,iy,x,y)

#p=create(15,15,1)
creatarrbuttons(6,0,2,14)
creatarrbuttons(0,6,4,9)

'''
cleararr(,,,)
cleararr(,,,)
cleararr(,,,)
cleararr(,,,)
cleararr(,,,)
cleararr(,,,)
cleararr(,,,)
cleararr(,,,)

cleararr(0,10,4,14)
cleararr(10,10,14,14)
cleararr(4,4,5,5)
cleararr(9,9,10,10)
cleararr(9,4,10,5)
cleararr(4,9,5,10)
clear(5,1)
'''

for x in range(15):
    for y in range(15):
        pass
      #  p[14-x][14-y]=p[y][x]
        #p[x][14-y]=p[14-x][y]
       # p[x][14-y]=p[x][y]
#printarray(p)
i=0
j=0
#while j==p[i][j]:
'''
out1=Label(width=10, height=1, bg='#ffffff', text="Кубики:")
out1.grid(row = 0, column = 16,columnspan = 3)'''
root.mainloop() 


