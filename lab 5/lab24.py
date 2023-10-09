import turtle as t


def drawCircle(color, radius, x, y):
    t.penup()
    t.fillcolor(color)
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    t.circle(radius)
    t.end_fill()


def drawEye(color, radius, x, y):
    drawCircle(color, radius, x, y)


def drawNose(color, radius, x, y):
    drawCircle(color, radius, x, y)


def drawMouth(radius, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.setheading(270)
    t.circle(radius, 180)

t.speed(5)
t.bgcolor("lightblue")

#head
drawCircle("white", 29, 0, -20)

# mid
drawCircle("white", 40, 0, -100)

#foot
drawCircle("white", 60, 0, -180)

# eye
drawEye("black", 5, -10, 0)
drawEye("black", 5, 10, 0)

# nose
drawNose("orange", 3, 0, -5)

#rot
drawMouth(5, 0, -10)


#hat
t.penup()
t.goto(-25, 20)
t.pendown()
t.color("black")
t.begin_fill()
t.goto(25, 20)
t.goto(0, 50)
t.end_fill()


t.hideturtle()
t.done()
