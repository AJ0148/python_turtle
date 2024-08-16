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

t.exitonclick()

# t.goto(100, 100)
# buildroof()

# t.hideturtle()
# t.exitonclick()