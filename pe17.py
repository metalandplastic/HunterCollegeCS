#Name: Robert Doherty
#Email: robert.doherty24@myhunter.cuny.edu
#Date: 2/11/24
#This program makes a striped box using user input and the saves the image for viewing

import matplotlib.pyplot as plt
import numpy as np

num= int(input("Enter the size: "))
file= input("Enter file name: ")

img=np.zeros((num,num,3))

img[::2,:,0::2]=1
img[1::2,:,0:2]=1



plt.imshow(img)
plt.show()

