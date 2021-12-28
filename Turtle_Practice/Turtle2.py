'''
@Author:Yohannes Assebe(John Assebe)
'''
import turtle 
t=turtle.Turtle()
t.speed(3000)
for i in range(360):
  t.right(60)
  t.forward(350)
  t.right(120)
  t.forward(350)

  t.right(120)
  t.forward(350)
  t.right(1)
##for i in range(360):
##    t.setposition(0,0)
##    t.forward(100)
##    t.right(1)
t.penup()
for i in range(120):
    t.setposition(0,200)
    t.pendown()
    t.forward(100)
    t.right(3)
t.penup()
for i in range(120):
    t.setposition(0,-200)
    t.pendown()
    t.forward(100)
    t.right(3)
t.penup()
for i in range(120):
    t.setposition(200,0)
    t.pendown()
    t.forward(100)
    t.right(3)
t.penup()
for i in range(120):
    t.setposition(-200,0)
    t.pendown()
    t.forward(100)
    t.right(3)
t.hideturtle()
    
turtle.done()
