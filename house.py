import turtle as t

t.shape("turtle")

while True:
    t.fd(100)
    t.left(90)
    if abs(t.pos()) < 1:
        break

t.penup()
t.fd(50)
t.pendown()
t.left(90)
t.fd(50)
t.left(90)
t.fd(50)
t.penup()
t.left(180)
t.fd(50)
t.pendown()
t.fd(50)
t.penup()
t.left(180)
t.fd(50)
t.right(90)
t.pendown()
t.fd(50)

t.exitonclick()