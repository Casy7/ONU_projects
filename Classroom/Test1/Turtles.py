'''from turtle import *
from random import randint 
speed(100)
penup()
x=-140
y=140
goto(x, y)
for step in range(15):
	write(step)
	forward(20)
	pendown()
	forward(400)
	penup()
	backward(420)
	right(90)
	forward(30)
	left(90)
t=[0]*4
v=[0]*4
x=250
y=130
for i in range(4):
	t[i]=Turtle()
	t[i].penup()
	t[i].shape('turtle')
	t[i].goto(x,y)
	y-=30
	t[i].pendown()
	t[i].right(135)
t[0].color("red")
t[1].color("blue")
t[2].color("green")
t[3].color("orange")
for i in range(4):
	v[i]=(randint(3,10)/10)
for j in range(600):
	for i in range(4):
		t[i].forward(v[i])
done()'''