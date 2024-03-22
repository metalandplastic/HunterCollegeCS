#Name: Robert Doherty
#Email: robert.doherty24@myhunter.cuny.edu
#Date: 2/1/24
#This program draws an octagon.

import turtle

octaturtle = turtle.Turtle()

for i in range (8):
    octaturtle.forward(100)
    octaturtle.left(360/8)
