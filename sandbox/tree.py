from turtle import *
from random import *
from math import *

 
def tree(n, l):
    pd() # pen
    t = cos(radians(heading() + 45)) / 8 + 0.25  # Shadow effect
    pencolor(t, t, t)
    pensize(n)
    forward(l) # draw branches

    if n > 0:
        b = random() * 15 + 10 # right branch deflection angle
        c = random() * 15 + 10 # left branch deflection angle
        d = l * (random() * 0.25 + 0.7) # length of next branch
        right(b) # Turn right at a certain angle, draw right branch
        tree(n - 1, d)  # Turn left at a certain angle, draw left branch        
        left(b + c)
        tree(n - 1, d)       
        right(c)   # Turn back

    else:  # leaves
        right(90)
        n = cos(radians(heading() - 45)) / 4 + 0.5
        pencolor(n, n * 0.8, n * 0.8)
        circle(3)
        left(90)
 
                 
        if(random() > 0.7):  # Add 0.3 times the falling leaves
            pu() 
            t = heading()
            an = -40 + random()*40
            setheading(an)
            dis = int(800 * random() * 0.5 + 400 * random() * 0.3 + 200 * random() * 0.2)
            forward(dis)
            setheading(t)  
            pd()  # Draw leaves
            right(90)
            n = cos(radians(heading() - 45)) / 4 + 0.5
            pencolor(n * 0.5 + 0.5, 0.4 + n * 0.4, 0.4 + n * 0.4)
            circle(2)
            left(90)
            pu()#Return   
            t = heading()
            setheading(an)
            backward(dis)
            setheading(t)
 
    pu()
    backward(l)# Back

    
bgcolor(0.5, 0.5, 0.5)  # background color
ht()  # hide turtle
speed(7)  # speed, 1-10 progressive, 0 is the fastest
tracer(0, 0)
pu()  # Lift the pen
backward(100)
left(90)  # Turn left 90 degrees
pu()  # Lift the pen
backward(300)  # backward 300
tree(12, 100)  # Recursive 7 layers
done()