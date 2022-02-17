"""TODO: A fractal tree landscape with a sun."""

__author__ = "730514879"

# L-System recursion information http://paulbourke.net/fractals/lsys/

from turtle import Turtle, colormode, done, bgcolor, update, tracer
colormode(255) 
wine: Turtle = Turtle()


def mountain():
    wine.fillcolor(114, 76, 76)
    wine.begin_fill()
    wine.hideturtle()
    wine.penup()
    wine.goto(-360, -180)
    wine.pendown()

    wine.left(45)
    wine.forward(510)
    wine.right(90)
    wine.forward(510)
    wine.right(135)
    wine.forward(720)
    wine.end_fill()

    wine.penup()
    wine.goto(0.62, 180.62)
    wine.setheading(0)
    wine.pendown()

    wine.fillcolor("white")
    wine.begin_fill()
    wine.right(45)
    wine.forward(110)
    wine.right(135)
    wine.forward(156)
    wine.right(135)
    wine.forward(110)
    wine.end_fill()


def branch(width: int, sze: float, lvl: float, angl: float):
    """Creates a cool tree with leaves."""
    wine.color("black")
    if lvl == 0:
        wine.color(187, 129, 195)
        wine.dot(6)
        wine.color("black")
        return

    wine.pensize(width)
    wine.forward(sze)
    wine.right(angl)

    branch(width - 1, sze * 0.8, lvl - 1, angl)

    wine.left(angl * 2)

    branch(width - 1, sze * 0.8, lvl - 1, angl)

    wine.right(angl)
    wine.backward(sze)


def sun(wid: float, lvl: int):
    """Creates the sides for the sun."""
    if lvl == 0:
        wine.forward(wid)
        return
    
    wid /= 3.0
    sun(wid, lvl - 1)
    wine.left(60)
    sun(wid, lvl - 1)
    wine.right(120)
    sun(wid, lvl - 1)
    wine.left(60)
    sun(wid, lvl - 1)


def make_sun(sides: int, wid: int):
    """Actually makes the sun with side peram."""
    wine.pensize(1)
    wine.penup()
    wine.goto(-300, 200)
    wine.pendown()
    wine.pencolor(240, 132, 23)
    wine.fillcolor(240, 23, 23)

    wine.begin_fill()

    for i in range(sides):
        sun(wid, sides)
        wine.right(360 / sides)
    
    wine.end_fill()


def make_axiom(numIters: int, axiom: str):
    start = axiom
    end = ""
    for i in range(numIters):
        end = create_sen(start)
        start = end

    return end


def create_sen(oldStr: str):
    newstr = ""
    for ch in oldStr:
        newstr = newstr + rules(ch)

    return newstr


def rules(ch: str):
    newstr = ""
    if ch == 'F':
        newstr = 'FF+[+F-F-F]-[-F+F+F]'   
    else:
        newstr = ch    

    return newstr


def commands(wine, rule, angl: float, dis: float):
    pos = []
    wine.fillcolor(187, 129, 195)
    wine.pencolor("black")
    
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


def draw(x: int, y: int):
    inst = make_axiom(3, "F")              

    wine.penup()
    wine.goto(x, y)
    wine.pendown()
    # print(inst)
    wine.up()
    wine.back(200)
    wine.down()
    wine.speed(0)
    commands(wine, inst, 32, 3)   


def main():

    tracer(0, 0)
    wine.hideturtle()
    wine.speed(0)
    bgcolor("grey")

    mountain()

    wine.setheading(0)
    wine.left(90)
    wine.penup()
    wine.goto(0, -180)
    wine.pendown()

    draw(300, 20)
    draw(200, 20)

    wine.penup()
    wine.goto(0, -180)
    wine.pendown()

    branch(10, 100, 10, 30)  # width needs to be 1/4 of sze
    make_sun(3, 80)

    draw(-200, 20)
    draw(-300, 20)

    update()
    done()


main()