#Name: Robert Doherty
#Email: robert.doherty24@myhunter.cuny.edu
#Date: 2/5/24
#This program draws a 5-pointed star.

import turtle

turtlestar = turtle.Turtle()
turtlestar.shape("turtle")
turtlestar.color("#0000cd")
for i in range (5):
    turtlestar.forward(100)
    turtlestar.right(360/2.5)
