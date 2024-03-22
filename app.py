# hi = 'hello, world'
# print(hi.find('d'))

# user_info = input('enter user name: ')
# print('your name:',user_info)

# mess = input('Enter a message: ')
# print(mess)
# print(mess.upper())
# print(mess.lower())

# myString = 'Hello, my good sir'

# user_string = input('Enter a phrase: ')
# print('In ASCII:')
# for c in user_string:
#     print(ord(c))
    
# for i in range(25):
#     print(myString)

# my_string = "Hi Mom!"
# for c in my_string:
#     print(c)

# import matplotlib.pyplot as plt
# import numpy as np

# color = int(input('enter a color: '))

# img = np.zeros((20,10,3))

# if color > 2:
#     exit()
# elif color < 0:
#     exit()
# else:
#     img[:,0:5,color] = 1.0

# plt.imshow(img)
# plt.show()

# import turtle				#Import the turtle drawing package

# turtle.colormode(255)		#Allows colors to be given as 0...255
# tess = turtle.Turtle()		#Create a turtle
# tess.shape("turtle")		#Make it turtle shaped
# tess.backward(100)			#Move her backwards, to give more space to draw

# #For 0,10,20,...,250
# for i in range(0,255,10):
#      tess.forward(10)		#Move forward
#      tess.pensize(i)		#Set the drawing size to be i (larger each time)
#      tess.color(0,0,i)		#Set the red channel to be i (brighter each time)
	#Predict what will be printed:
# for c in range(65,90):
#     print(chr(c))
	    
# message = "I love Python"
# newMessage = ""

# for c in message:
# 	print(ord(c))   #Print the Unicode of each number
# 	print(chr(ord(c)+1))    #Print the next character
# 	newMessage = newMessage + chr(ord(c)+1) #add to the new message
# 	print("The coded message is", newMessage)
	
# 	word = "zebra"
# 	codedWord = ""
# 	for ch in word:
# 	    offset = ord(ch) - ord('a') + 1 #how many letters past 'a'
# wrap = offset % 26  #if larger than 26, wrap back to 0
# newChar = chr(ord('a') + wrap)  #compute the new letter
# print(wrap, chr(ord('a') + wrap))    #print the wrap & new letter
# codedWord = codedWord + newChar #add the newChar to the coded word    
# print("The coded word (with wrap) is", codedWord)
# user_color= input("enter hex color: ")


# import turtle				#Import the turtle drawing package

# turt = turtle.Turtle()
# turt.shape("turtle")
# turt.color(user_color)

# print(turt)



# km = float(input("enter distance in kilometers: "))

# miles = km * 0.621371

# print("you biked",miles,"miles!")


message = input("Enter a message: ")

reversed_message = message[::-1]

for c in reversed_message:
    print(c, c)
