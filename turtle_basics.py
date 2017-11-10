
# From http://www.openbookproject.net/thinkcs/archive/python/thinkcspy3e_abandoned/ch03.html

import turtle

turtle.setup(800, 600)      # set the window size to 800 by 600 pixels
wn = turtle.Screen()        # set wn to the window object
wn.bgcolor("white")    # set the window background color
wn.title("Hello, Tess!")    # set the window title

tess = turtle.Turtle()
tess.color("red")           # make tess red
tess.pensize(3)              # set the width of her pen

tess.forward(300)
tess.left(120)
tess.forward(300)

wn.exitonclick()