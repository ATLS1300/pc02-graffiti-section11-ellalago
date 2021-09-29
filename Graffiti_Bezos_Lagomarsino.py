#!/usr/bin/env python
# coding: utf-8

'''
Turtle starter code
ATLS 1300
Author: Ella
Author: Lagomarsino
September 07, 2021
'''

import turtle #import the library of commands that you'd like to use

turtle.colormode(255)

# Create a panel to draw on. 
panel = turtle.Screen()
w = 750 # width of panel
h = 750 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

# Create a colorful background and add Bezos image to it
image = "Bezos.gif"
panel.bgcolor("OliveDrab")
panel.bgpic(image)

#=======Add your code here==========
turtle.up()
turtle.goto(250,100)
turtle.color("OliveDrab1")
turtle.pensize(10)
turtle.down()
turtle.circle(10)
turtle.up()

turtle.goto(-68,52)
turtle.down()
turtle.color("MediumBlue")
turtle.backward(7)
turtle.left(90)
turtle.forward(5)
turtle.backward(10)
for i in range(4):
    turtle.forward(100)
    turtle.right(90)
turtle.up()
    
turtle.goto(39,5)
turtle.down()
        















#=======Clean up code (do not change)======
# this code ensures that your script runs correctly each time
turtle.done()
