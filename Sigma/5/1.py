import turtle
def goto(turt,x,y):
    turt.penup()
    turt.goto(x,y)
    turt.pendown()
    
x=0
y=0
def right(t):
    t.right(90)

def drawField(turt,x,y):
    y-=50
    goto(turt,x,y)
    turt.forward(150)
    y-=50
    goto(turt,x,y)
    turt.forward(150)
    x=100
    y=0
    turt.left(270)
    goto(turt,x,y)
    turt.forward(150)
    x-=50
    goto(turt,x,y)
    turt.forward(150)


turt=turtle.Turtle()

turt.penup()
turt.goto(x,y)
def drawSign(turt,x,y,sign):
    defaultFont=("Arial",40,"normal")
    turt.goto(x,y)
    turt.write(sign,font = defaultFont)
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
def game(turt,startX,startY):
    drawField(turt, startX,startY)
    for turn in range(5):
        player_choose = int(input("Игрок крестик выбрал: "))
        makeTurn(turt,startX,startY,player_choose,"x")

        player_choose = int(input("Игрок нолик выбрал: "))
        makeTurn(turt,startX,startY,player_choose,"o")
x=150
y=150    

game(turt,x,y)
turtle.done()