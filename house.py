import turtle as t

t.shape("turtle")
t.pencolor("green")
t.color("green")

def buildroof():
    t.right(225)
    t.pencolor("black")
    t.fillcolor("black")
    t.pendown()
    t.begin_fill()
    t.fd(70)
    t.left(90)
    t.fd(70)
    t.left(135)
    t.fd(100)
    t.end_fill()
    t.penup()

def fixroofcolors():
    t.pencolor("green")
    t.color("green")
    t.pendown()

#first house
t.penup()
t.goto(-175, 0)
t.pendown()

for i in range(4):
    t.fd(100)
    t.left(90)

for i in range(4):
    t.penup()
    t.goto(-125, 50)
    t.pendown()
    t.left(90)
    t.fd(50)

t.goto(-75, 100)
buildroof()
t.home()
t.pendown()
fixroofcolors()

#second house
while True:
    t.fd(100)
    t.left(90)
    if abs(t.pos()) < 1:
        break

for i in range(4):
    t.penup()
    t.goto(50, 50)
    t.pendown()
    t.left(90)
    t.fd(50)

#top right window
t.penup()
t.goto(50, 50)
t.fd(15)
t.left(90)
t.fd(15)
t.pencolor("black")
t.pendown()
t.fillcolor("lightblue")
t.begin_fill()
for i in range(4):
    t.fd(20)
    t.right(90)
t.end_fill()
t.penup()
t.goto(75, 75)
t.pendown()
t.pencolor("black")
for i in range(4):
    t.goto(75, 75)
    t.right(90)
    t.fd(10)
t.penup()

#bottom left window
t.goto(50, 50)
t.bk(15)
t.left(90)
t.fd(15)
t.pendown()
t.begin_fill()
for i in range(4):
    t.fd(20)
    t.left(90)
t.end_fill()
t.penup()
t.goto(25, 25)
t.pendown()
for i in range(4):
    t.goto(25, 25)
    t.right(90)
    t.fd(10)
t.penup()

#top left window
t.goto(50, 50)
t.fd(15)
t.right(90)
t.fd(15)
t.pendown()
t.begin_fill()
for i in range(4):
    t.fd(20)
    t.left(90)
t.end_fill()
t.penup()

#door
t.home()
t.fd(80)
t.left(90)
t.fillcolor("#814f46")
t.begin_fill()
t.pendown()
t.fd(25)
t.right(90)
t.fd(20)
t.right(90)
t.fd(25)
t.right(90)
t.fd(20)
t.end_fill()
t.penup()

t.goto(100, 100)
t.left(180)
buildroof()

#third house
t.goto(175, 0)
fixroofcolors()

for i in range(4):
    t.fd(100)
    t.left(90)

for i in range(4):
    t.penup()
    t.goto(225, 50)
    t.pendown()
    t.left(90)
    t.fd(50)

t.goto(275, 100)
buildroof()

t.hideturtle()
t.exitonclick()