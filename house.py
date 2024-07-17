import turtle as t

t.shape("turtle")

while True:
    t.fd(100)
    t.left(90)
    if abs(t.pos()) < 1:
        break

t.exitonclick()