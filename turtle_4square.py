import turtle

myTurtle = turtle.Turtle()
win = turtle.Screen()

def square(side, line, fillcolor):
    myTurtle.hideturtle()
    myTurtle.speed(0)
    myTurtle.width(3)
    myTurtle.color(line, fillcolor)
    myTurtle.begin_fill()
    myTurtle.forward(side)
    myTurtle.right(90)
    myTurtle.forward(side)
    myTurtle.right(90)
    myTurtle.forward(side)
    myTurtle.right(90)
    myTurtle.forward(side)
    myTurtle.end_fill()

def main():
    square(40, "black", "yellow")
    square(50, "black", "blue")
    square(60, "black", "red")
    square(70, "black", "green")
    win.listen()
    win.exitonclick()


if __name__ == '__main__':
    main()

