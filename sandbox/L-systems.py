"""TODO: A cool mathematical landscape."""

__author__ = "730514879"

from turtle import Turtle, colormode, done, bgcolor, update, tracer
wine: Turtle = Turtle()
colormode(255)


def make_axiom(numIters, axiom):
    startString = axiom
    endString = ""
    for i in range(numIters):
        endString = create_sen(startString)
        startString = endString

    return endString


def create_sen(oldStr):
    newstr = ""
    for ch in oldStr:
        newstr = newstr + rules(ch)

    return newstr


def rules(ch):
    newstr = ""
    if ch == 'F':
        newstr = 'FF+[+F-F-F]-[-F+F+F]'   
    else:
        newstr = ch    

    return newstr


def commands(wine, rule, angl, dis):
    pos = []
    wine.fillcolor("green")
    wine.pencolor(101, 67, 33)
    
    for cmd in rule:
    
        if cmd == "F":
            wine.forward(dis)
        if cmd == "G":
            wine.penup()
            wine.forward(dis)
            wine.pendown()
        elif cmd == "[":
            wine.begin_fill()
            pos.append(wine.position())
        elif cmd == "]":
            # wine.penup()
            wine.setposition(pos.pop())
            wine.end_fill()
            # wine.pendown()
        elif cmd == "+":
            wine.right(angl)
        elif cmd == "-":
            wine.left(angl)


def draw():
    inst = make_axiom(4, "F")       
    wine.left(90)       
    bgcolor("grey")
    print(inst)
    wine.up()
    wine.back(200)
    wine.down()
    wine.speed(0)
    commands(wine, inst, 32, 5)   


wine.hideturtle()
tracer(0, 0)
draw()
update()
done()