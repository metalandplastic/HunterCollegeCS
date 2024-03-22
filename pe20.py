#Name: Robert Doherty
#Email: robert.doherty24@myhunter.cuny.edu
#Date: 2/15/24
#A program that does a count of snow based on pixel color

import matplotlib as plt
import numpy as np

import matplotlib.pyplot as plt
import numpy as np

# Prompt the user to enter the filename of the image
file_name = input("Enter the filename of the image: ")

# Load the image
image = plt.imread(file_name)

# Initialize the count for nearly white pixels
countSnow = 0
# Threshold for nearly white pixels
t = 0.75

# Iterate over every pixel in the image
for i in range(image.shape[0]):
    for j in range(image.shape[1]):
        # Check if red, green, and blue are > t
        if (image[i, j, 0] > t) and (image[i, j, 1] > t) and (image[i, j, 2] > t):
            countSnow += 1

# Print the snow count
print("Snow count is", countSnow)

