from turtle import Turtle, colormode, done
colormode(255)

leo: Turtle = Turtle()
bob: Turtle = Turtle()

###

bob.penup()
bob.goto(-160, -160)
bob.pendown()

bob.speed(50)
bob.hideturtle()

# bob.color(166, 129, 195)
bob.pencolor("pink")
bob.fillcolor(100, 0, 0)

side_length: float = 300

i: int = 0
while (i < 3):
    bob.forward(side_length)
    bob.left(120)
    i = i + 1

###

leo.penup()
leo.goto(-160, -160)
leo.pendown()

leo.speed(50)
leo.hideturtle()

# leo.color(166, 129, 195)
leo.pencolor("pink")
leo.fillcolor(100, 0, 0)

i: int = 0

leo.begin_fill()
while (i < 3):
    leo.forward(side_length)
    leo.left(120)
    side_length = side_length * 0.97  # decrease side length each time
    i = i + 1

leo.end_fill()

done()