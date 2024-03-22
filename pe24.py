#Name: Robert Doherty
#Email: robert.doherty24@myhunter.cuny.edu
#Date: 2/21/24
#A program that controls a turtle graphic with user commands

import turtle

tess = turtle.Turtle()
myWin = turtle.Screen()     #The graphics window
commands = input("Please enter a command string: ")

for ch in commands:
    #perform action indicated by the character
    if ch == 'B':            #move forward
        tess.backward(50)
    elif ch == 'F':            #move forward
        tess.forward(50)
    elif ch == 'L':          #turn left
        tess.left(90)
    elif ch == 'R':          #turn right
        tess.right(90)
    elif ch == '^':          #lift pen
        tess.penup()
    elif ch == 'v':          #lower pen
        tess.pendown()
    elif ch == 'S':          #turn left
        tess.stamp()
    elif ch == 'l':          #turn right
        tess.left(45)
    elif ch == 'r':          #lift pen
        tess.right(45)
    elif ch == 'p':          #lower pen
        tess.pencolor('purple')
    else:                   #for any other character, print an error message 
        print("Error: do not know the command:", ch) #typo, was c before

print("See graphics window for your image")
myWin.exitonclick()         #Close the window when clicked
