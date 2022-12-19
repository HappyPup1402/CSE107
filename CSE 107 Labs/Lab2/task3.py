# Import pillow
from PIL import Image, ImageOps
# Import numpy
import numpy as np
from numpy import asarray
# The size of the gradient image.
rows = 100
cols = 256
# Create a numpy matrix of this size.
im_pixels = np.zeros(shape=(rows, cols))
#<the rest of your code>

for i in range(rows):
    for j in range(cols):
        im_pixels[i-1,j-1] = j

#Display the image on the screen. 
#Save the image as a .tif file. 
im_gradient = Image.fromarray(np.uint8(im_pixels))
im_gradient.show()
im_gradient.save("Graysacle_gradient.tif")

#Compute the average pixel value of the gradient image. You must use nested forloops to do this. You are not allowed to use any built-in functions to compute the average.
sum = 0
for i in range(rows):
    for j in range(cols):
        sum = sum + int(im_pixels[i, j])
        
average = sum / (rows*cols)
print("The average pixel is: " +str(average))