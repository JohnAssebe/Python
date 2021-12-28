'''
@Author:Yohannes Assebe(John Assebe)
'''
import turtle
t=turtle.Turtle()
t.speed(100)
t.penup()
t.setposition(-600,-300)
t.pendown()
for i in range(80):
        t.left(60)
        t.forward(400-(10*i+30))
        t.right(120)
        t.forward(400-(10*i+30))
        t.right(120)
        t.forward(400-(10*i+30))
        t.penup()
        if i==1:
            t.setposition(-680,-380)
            
        t.setposition(-600+(15*i+5),-300+(5*i+10))
        t.right(180)
        t.pendown()
t.hideturtle()
turtle.done()
