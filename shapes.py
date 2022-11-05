import turtle


def move(distance):
    turtle.forward(distance)


def turn_left():
    turtle.left(90)


def turn_right():
    turtle.right(90)


def small_circle():
    turtle.circle(10)


def ears():
    turn_right()
    turtle.circle(30)
    turtle.circle(20)

def small_triangle(edge=10):
    turtle.forward(edge)
    turtle.right(120)
    turtle.forward(edge)
    turtle.right(120)
    turtle.forward(edge)
    turtle.right(120)
    turtle.forward(edge)

def triangle(edge=100):
    turtle.forward(edge)
    turtle.right(120)
    turtle.forward(edge)
    turtle.right(120)
    turtle.forward(edge)
    turtle.right(120)
    turtle.forward(edge)
    turtle.right(60)

triangle()
triangle()
triangle()
triangle()
triangle()
triangle()
turtle.left(180)
turtle.penup()
turtle.forward(200)
turtle.left(180)
turtle.pendown()

move(100)
turn_left()
move(100)
ears()
turtle.left(180)
move(100)
turn_right()
ears()
turn_right()
move(100)
turtle.penup()
turtle.left(180)
move(60)
turn_right()
move(20)
turtle.pendown()
small_circle()
turtle.penup()
move(60)
turtle.pendown()
small_circle()
turtle.penup()
turn_right()
move(20)
turn_right()
move(30)
turtle.pendown()
small_triangle()
turtle.penup()
move(10)
turn_left()
move(10)
turtle.pendown()
turtle.circle(20, 180)


turtle.mainloop()
