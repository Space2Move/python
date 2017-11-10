import turtle

painter = turtle.Turtle()
win = turtle.Screen()

painter.speed(0)

painter.pencolor("blue")

for i in range(50):
    painter.forward(50)
    painter.left(123)  # Let's go counterclockwise this time

painter.pencolor("red")

for i in range(50):
    painter.forward(100)
    painter.left(123)

painter.pencolor("green")

for i in range(50):
    painter.forward(150)
    painter.left(123)

win.listen()
win.exitonclick()

turtle.done()