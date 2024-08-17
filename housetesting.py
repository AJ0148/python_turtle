import turtle as t

t.shape("turtle")
t.pencolor("green")
t.color("green")

#build house
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

t.exitonclick()