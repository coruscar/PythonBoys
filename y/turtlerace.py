# This looks fun! 
from turtle import *
from random import randint

#write(0)
#forward(20)
#write(1)
#forward(20)
#wrire(2)
#forward(20)
#write(3)
#forward(20)
#write(4)
#forward(20)
#write(5)
#forward(20)

speed(10)
pendown()
penup()
goto(-140, 140)

# Counts from 0.
for step in range(15):
    write(step, align='center')
    right(90)
    forward(10)
    pendown()
    forward(150)
    penup()
    backward(160)
    left(90)
    forward(20)

# goto(140, 140)
# for step in range(6):
#    write(step, align='center')
#    left(90)
#    backward(10)
#    pendown()
#    backward(150)
#    penup()
#    forward(160)
#    right(90)
#    backward(20)

# Turtle A.
a = Turtle()
a.color('red')
a.shape('turtle')

a.penup()
a.goto(-160, 100)
a.pendown()

# Turtle B.
b = Turtle()
b.color('blue')
b.shape('turtle')

b.penup()
b.goto(-160, 70)
b.pendown()

# Turtle C.
c = Turtle()
c.color('green')
c.shape('turtle')

c.penup()
c.goto(-160, 40)
c.pendown()

# Turtle D.
d = Turtle()
d.color('purple')
d.shape('turtle')

d.penup()
d.goto(-160, 10)
d.pendown()

# Race.
for turn in range(100):
    a.forward(randint(1, 5))
    b.forward(randint(1, 5))
    c.forward(randint(1, 5))
    d.forward(randint(1, 5))

a.right(180)
b.right(180)
c.right(180)
d.right(180)

for turn in range(100):
    a.forward(randint(1, 5))
    b.forward(randint(1, 5))
    c.forward(randint(1, 5))
    d.forward(randint(1, 5))
