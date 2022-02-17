"""TODO: A fractal tree landscape with a sun."""

__author__ = "730514879"

# L-System recursion information http://paulbourke.net/fractals/lsys/

from turtle import Turtle, colormode, done, bgcolor, update, tracer
colormode(255) 
wine: Turtle = Turtle()


def mountain() -> None:
    """Makes a mountain in the background."""
    # this code is really simple. It just draws one big triangle then one small triangle and fills each with a color to make a mountain
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


def branch(width: int, sze: float, lvl: float, angl: float) -> None:
    """Creates a cool tree with leaves."""
    # this uses factorial to create a branching tree
    # if lvl is 0 it exits the function but if the lvl is not 0 it choses a path to draw based on the given instructions
    wine.color("black")
    if lvl == 0:
        wine.color(187, 129, 195)
        wine.dot(6)
        wine.color("black")
        return

    wine.pensize(width)
    wine.forward(sze)
    wine.right(angl)

    branch(width - 1, sze * 0.8, lvl - 1, angl)  # width of pen gets smaller, length of stroke gets shorter, the level goes down, and the angle stays the same

    wine.left(angl * 2)

    branch(width - 1, sze * 0.8, lvl - 1, angl)

    wine.right(angl)
    wine.backward(sze)


def sun(wid: float, lvl: int) -> None:
    """Creates the sides for the sun."""
    # like branch, this creates one side of a fractal triangle based on level of detail. lots of triangle creating triangles on triangles
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


def make_sun(sides: int, wid: int) -> None:
    """Actually makes the sun with side peram."""
    # takes in the sun peram and multiplies it by the number of sides i want. Changes the angl based on number of sides so it connects at the end
    wine.pensize(1)
    wine.penup()
    wine.goto(-300, 200)
    wine.pendown()
    wine.pencolor(240, 132, 23)
    wine.fillcolor(240, 23, 23)

    wine.begin_fill()

    for i in range(sides):  # function  to turn triangle sides
        sun(wid, sides)
        wine.right(360 / sides)
    
    wine.end_fill()


def make_axiom(numIters: int, axiom: str) -> str:
    """Takes in the axiom str and remeats it x number of times."""  # this tree formation is made useing Lindenmayer Systems generation
    start = axiom
    end = ""
    for i in range(numIters):  # multiplies the str len by wanted number to get a higher LOD
        end = create_sen(start)
        start = end

    return end


def create_sen(oldStr: str) -> str:
    """Sentense building function."""
    newstr = ""
    for ch in oldStr:
        newstr = newstr + rules(ch)  # adds to the new str with the rules

    return newstr


def rules(ch: str) -> str:
    """Replaces items withen the sentence str."""
    newstr = ""
    if ch == 'F':
        newstr = 'FF+[+F-F-F]-[-F+F+F]'   # all F's are replaced by this sentence and this is what is multipled and read off of
    else:
        newstr = ch    

    return newstr


def commands(rule: str, angl: float, dis: float) -> None:
    """Gives the commands for turtle based on the sentence."""
    pos = []
    wine.fillcolor(187, 129, 195)
    wine.pencolor("black")
    
    for cmd in rule:  # the entire string of rules is read through and at each one a command is given and read then executed
    
        if cmd == "F":
            wine.forward(dis)
        if cmd == "G":
            wine.penup()
            wine.forward(dis)
            wine.pendown()
        elif cmd == "[":
            wine.begin_fill()
            pos.append(wine.position())  # the open bracket takes in the pos of the turtle and saves it to a list 
        elif cmd == "]":
            # wine.penup()
            wine.setposition(pos.pop())  # the closed bracket takes the save pos form the list and moves the turtle there then removes the pos from the list 
            wine.end_fill()
            # wine.pendown()
        elif cmd == "+":
            wine.right(angl)
        elif cmd == "-":
            wine.left(angl)


def draw(x: int, y: int) -> None:
    """Takes in the commands and draws the actual function."""
    inst = make_axiom(3, "F")  # 3 is the LOD of the tree. DON'T MAKE HIGHER THAN 4!!!! otherwise it tanks the pc, F is the start of the str            

    wine.penup()
    wine.goto(x, y)
    wine.pendown()
    # print(inst)  # this shows the rules
    wine.up()
    wine.back(200) 
    wine.down()
    wine.speed(0)
    commands(inst, 32, 3)   
    # inst is rule book, 32 is the angle the branches form on, and 3 is the pen stroke length


def main() -> None:
    """Main function for drawing everything"""

    tracer(0, 0)  # tracer and update just mek the pic show up instantly w/o screen refresh
    wine.hideturtle()  
    wine.speed(0)
    bgcolor("grey")  # canvass color is grey 

    mountain()

    wine.setheading(0)   # this block resets the turtle to a starting pos from which all the other math works out
    wine.left(90)
    wine.penup()
    wine.goto(0, -180)
    wine.pendown()

    draw(300, 20)  # drawn cords 300, 20
    draw(200, 20) 

    wine.penup()
    wine.goto(0, -180)  # resets the turtle pos again
    wine.pendown()

    branch(10, 100, 10, 30)  # width needs to be 1/4 of sze
    # 10 is initial pen size, 100 is initial pen stroke len, 10 is the LOD (DON'T  GO HIGHER THAN 15), 30 is the angle the branches form at
    make_sun(3, 80)

    draw(-200, 20)
    draw(-300, 20)

    update()
    done()  # allows the screen to stay on after drawing is done


main()