from random import randint
from tkinter import *
root = Tk()
root.geometry("1300x720")
def create(m=0,n="Err",r=9):
    if(n=="Err"):
        n=m
    g=[]
    for i in range(m):
        m1=[]
        for j in range(n):
            m1.append(Button(width=7, height=3, bg='#ffffff', text=str(i)+" "+str(j)))
        g.append(m1)   
    return g	
def clear(x,y):
    p[x][y]=Button(width=7, height=3, bg='#000000', text="1",activebackground='#000000',activeforeground='#000000')
def cleararr(x1,y1,x2,y2):
    for y in range(y1,y2+1):
        for x in range(x1,x2+1):
            clear(y,x)
def printarray(c=[]):
	for x in range(len(c)):
		for i in range(len(c[0])):
			c[x][i].grid(row = x, column = i)
p=create(15,15,1)
cleararr(0,0,4,4)
cleararr(10,0,14,4)
cleararr(0,10,4,14)
cleararr(10,10,14,14)
cleararr(4,4,5,5)
cleararr(9,9,10,10)
cleararr(9,4,10,5)
cleararr(4,9,5,10)

clear(5,1)
printarray(p)

out1=Label(width=10, height=3, bg='#ffffff', text="Кубики:")
out1.grid(row = 0, column = 16,columnspan = 3)

root.mainloop() 
