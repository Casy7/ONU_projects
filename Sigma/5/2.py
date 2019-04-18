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