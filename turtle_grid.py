import turtle

myTurtle = turtle.Turtle()
win = turtle.Screen()
x = 390
y = 10
z = 1
myTurtle.speed(500)
myTurtle.width(10)
myTurtle.penup()
myTurtle.setpos(-200,-200)
dofill = True

def rectangle(x, y, line, fillcolor):
    myTurtle.hideturtle()
    myTurtle.pensize(1)
    myTurtle.pendown()
    if dofill:
        myTurtle.color(line, fillcolor)
        myTurtle.begin_fill()
    else:
        z = 3
    myTurtle.forward(x)
    myTurtle.left(90)
    myTurtle.forward(y)
    myTurtle.left(90)
    myTurtle.forward(x)
    myTurtle.left(90)
    myTurtle.forward(y)
    myTurtle.right(180)
    myTurtle.penup()
    myTurtle.forward(2*y)
    myTurtle.right(90)
    if dofill:
        myTurtle.end_fill()
    else:
        z = 3
def main():
    for i in range(5):
        rectangle(x, y, "black", "yellow")
        rectangle(x, y, "black", "blue")
        rectangle(x, y, "black", "red")
        rectangle(x, y, "black", "green")
    myTurtle.right(90)
    myTurtle.setpos(-200, 190)
    for i in range(5):
        rectangle(x, y, "black", "yellow")
        rectangle(x, y, "black", "blue")
        rectangle(x, y, "black", "red")
        rectangle(x, y, "black", "green")
    win.listen()
    win.exitonclick()


if __name__ == '__main__':
        main()



