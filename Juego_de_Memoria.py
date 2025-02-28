from random import *
from turtle import *
from freegames import path

car = path('car.gif')
tiles = list(range(32)) * 2
state = {'mark': None}
hide = [True] * 64
click = {'taps': 0}
contNum = 0
writer = Turtle(visible=False)
turned_cards = 0

def square(x, y):
    "Draw white square with black outline at (x, y)."
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()

def index(x, y):
    "Convert (x, y) coordinates to tiles index."
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)

def xy(count):
    "Convert tiles count to (x, y) coordinates."
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200

def tap(x, y):
    "Update mark and hidden tiles based on tap."
    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
        global turned_cards
        turned_cards += 1

    print(click)
    click['taps'] +=1
    update()

def draw():
    "Draw image and tiles."
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        #Centrar texto
        if tiles[mark] > 9:
            goto(x+3,y+2)
        elif tiles[mark] > 19:
            goto(x+5,y+2)
        elif tiles[mark] > 29:
            goto(x+7,y+2)
        else:
            goto(x+15,y+2)
        color('black')
        write(tiles[mark], font=('Arial', 30, 'normal'))

    goto(-40,210) 
    write (click,font=("Arial",20))
    update()
    if turned_cards==32: 
        up()
        goto(0, 0)
        color('green')
        write("GANASTE",  align="center", font=("Arial", 20, "bold")) 
    ontimer(draw, 100)

shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()