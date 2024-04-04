#Name: Robert Doherty
#Email: robert.doherty24@myhunter.cuny.edu
#Date: 2/29/24
#A program that asks the user for the name of an image, the name of an output file and saves the lower left quarter of the image to the output file specified by the user.

import matplotlib.pyplot as plt
import numpy as np

inF = input('Enter file name: ')
userOutput = input("Enter name of output file: ")

img = plt.imread(inF)
height = img.shape[0]
width = img.shape[1]
img2 = img[height//2:, :width//2] 
# plt.imshow(img2) 
# plt.show() 
plt.imsave(userOutput, img2)
