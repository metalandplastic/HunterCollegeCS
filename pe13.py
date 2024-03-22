#Name: Robert Doherty
#Email: robert.doherty24@myhunter.cuny.edu
#Date: 2/4/24
#A program that creates a cornflowerblue turtle that stamps as it draws a shape

import turtle

kev = turtle.Turtle()

kev.shape("turtle")
kev.color("#6495ed")

for i in range(5):
    kev.forward(100)
    kev.left(360/5)
    kev.stamp()

    

