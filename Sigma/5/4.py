import turtle
def goto(turt, x, y):
    turt.penup()
    turt.goto(x, y)
    turt.pendown()

def right(t):
    t.right(90)
def drawField(t, x, y):
    y-=50
    goto(t, x, y)
    t.forward(150)
    y-=50
    goto(t, x, y)
    t.forward(150)
    y+=100
    x+=50
    goto(t, x, y)
    right(t)
    t.forward(150)
    x+=50
    goto(t, x, y)
    t.forward(150)

def drawSign(turt, x, y, sign):
    goto(turt, x, y)
    turt.write(sign, font = defaultFont)

def makeTurn(turt, fieldX, fieldY, position, sign):
    if position == 0:
        fieldX+=15
        fieldY-=50
    elif position == 1:
        fieldX+=65
        fieldY-=50
    elif position == 2:
        fieldX+=115
        fieldY-=50
    if position == 3:
        fieldX+=15
        fieldY-=100
    elif position == 4:
        fieldX+=65
        fieldY-=100
    elif position == 5:
        fieldX+=115
        fieldY-=100
    if position == 6:
        fieldX+=15
        fieldY-=150
    elif position == 7:
        fieldX+=65
        fieldY-=150
    elif position == 8:
        fieldX+=115
        fieldY-=150
    drawSign(turt, fieldX, fieldY, sign)

def win_check():
	if (poly[0]==poly[1]==poly[2]=="x" 
    or poly[3]==poly[4]==poly[5]=="x" 
    or poly[6]==poly[7]==poly[8]=="x" 
    or poly[0]==poly[3]==poly[6]=="x" 
    or poly[1]==poly[4]==poly[7]=="x" 
    or poly[2]==poly[5]==poly[8]=="x" 
    or poly[0]==poly[1]==poly[2]=="x" 
    or poly[3]==poly[4]==poly[5]=="x" 
    or poly[6]==poly[7]==poly[8]=="x" 
    or poly[0]==poly[4]==poly[8]=="x" 
    or poly[2]==poly[4]==poly[6]=="x"):
		return("Крестики победили")
	elif (poly[0]==poly[1]==poly[2]=="o" or 
    poly[3]==poly[4]==poly[5]=="o" 
    or poly[6]==poly[7]==poly[8]=="o" 
    or poly[0]==poly[3]==poly[6]=="o" 
    or poly[1]==poly[4]==poly[7]=="o" 
    or poly[2]==poly[5]==poly[8]=="x" 
    or poly[0]==poly[1]==poly[2]=="x"
    or poly[3]==poly[4]==poly[5]=="o" 
    or poly[6]==poly[7]==poly[8]=="o" 
    or poly[0]==poly[4]==poly[8]=="o" 
    or poly[2]==poly[4]==poly[6]=="o"):
		return("Нолики победили")
def turn(x_or_o,startX, startY):
	check_result=win_check()
	if(check_result!="Крестики победили" and check_result!="Нолики победили"):
		if x_or_o=="x":
			player="крестик"
		else:
			player="нолик"
		player_choose = int(input("Игрок "+player+" выбрал: "))
		if(poly[player_choose]=="-"):
			poly[player_choose]=x_or_o
			makeTurn(turt, startX, startY, player_choose, x_or_o)
			if whose_turn[0]=="x":
				whose_turn[0]="o"
			else:
				whose_turn[0]="x"
		else:
			print("Ошибка ввода")
			game(turt, startX, startY,poly)	
	else:
		win_animation(0,0,check_result)
def game(turt, startX, startY,poly):
	for i in range(9):
		turn(whose_turn[0],startX, startY)
def win_animation(x,y,win_check):
	import turtle
	animatoin=turtle.Turtle()
	animatoin.penup()
	animatoin.goto(x+80,y)
	animatoin.write(win_check+"!!!", align="center",font=("Arial", 16, "normal"))
	'''
	for h in range(1000):
		animatoin.shape('turtle')
		animatoin.goto(x,y)
		animatoin.speed(1000000)
		animatoin.color('red')
		animatoin.shape('turtle')
		for i in range(200):
			animatoin.forward(0.2*i+2)
			animatoin.right(4)
		animatoin.penup()
		animatoin.goto(x,y)
		animatoin.right(5)
		animatoin.pendown()
	'''
	#Попытка анимации в случае победы. Лучше не трогать
poly=["-"]*9
whose_turn=["x"]
x=0
y=0
defaultFont = ("Arial", 40, "normal")
turt = turtle.Turtle()
drawField(turt, x, y)
game(turt, x, y,poly)
turtle.done()