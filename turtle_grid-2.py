import turtle

myTurtle = turtle.Turtle()
win = turtle.Screen()
x = 390
y = 10
myTurtle.speed(400)
myTurtle.penup()
myTurtle.pensize(1)
myTurtle.hideturtle()
myTurtle.setpos(-200,-200)

def rectangle(x, y):
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

def main():
    for i in range(20):
        myTurtle.pendown()
        rectangle(x, y)
    myTurtle.right(90)
    myTurtle.setpos(-200, 190)
    for i in range(20):
        myTurtle.pendown()
        rectangle(x, y)
    win.listen()
    win.exitonclick()

if __name__ == '__main__':
        main()



