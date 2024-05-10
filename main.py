import turtle as t


t.pensize(5)
t.speed(0)
t.bgcolor('black')


t.penup()
t.left(90)
t.forward(500)
t.pendown()


t.color('red')
t.begin_fill()
t.left(90)
t.circle(500)
t.end_fill()


t.penup()
t.left(90)
t.forward(100)
t.pendown()


t.color('white')
t.begin_fill()
t.right(90)
t.circle(400)
t.end_fill()


t.penup()
t.left(90)
t.forward(100)
t.pendown()


t.color('red')
t.begin_fill()
t.right(90)
t.circle(300)
t.end_fill()


t.penup()
t.left(90)
t.forward(100)
t.pendown()


t.color('blue')
t.begin_fill()
t.right(90)
t.circle(200)
t.end_fill()

t.color('white')
t.left(70)
t.begin_fill()

for I in range(5):
    t.forward(370)
    t.left(145)
t.end_fill()


t.done()