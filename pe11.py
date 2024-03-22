#Name: Robert Doherty
#Email: robert.doherty24@myhunter.cuny.edu
#Date: 2/4/24
#A program that demonstrates the shades of blue

import turtle				

user_color = input("enter hex code:")

rob = turtle.Turtle()
rob.shape("turtle")
rob.color(user_color)

for i in range(10):
     print(rob)				



# turtle.colormode(255)		
# turt = turtle.Turtle()		
# turt.shape("turtle")		
# turt.backward(100)			

# #For 0,10,20,...,250
# for i in range(0,255,10):
#      turt.forward(10)		
#      turt.pensize(i)		
#      turt.color(0,0,i)		
