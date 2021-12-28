'''
@Author:Yohannes Assebe(John Assebe)
This program draws two triangles that are inverted each other
'''
import turtle
t=turtle.Turtle()
t.speed(100)
for i in range(6):
    t.forward(100)
    t.right(60)
    t.forward(100)
    t.right(120)
    t.forward(100)
    t.right(120)
    t.forward(100)
    t.penup()
    t.setposition(i,i)
    t.pendown()
turtle.done()
