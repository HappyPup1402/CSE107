# Import pillow
from PIL import Image, ImageOps
# Import numpy
import numpy as np
from numpy import asarray
# Read the image from file.
im = Image.open('Beginnings.jpg')
# Show the image.
im.show()
# Convert image to gray sc ale.
im_gray = ImageOps.grayscale(im)
# Show the grayscale image.
im_gray.show()
#<the rest of your code>

#Create a numpy matrix that has the pixel values from the image. 
#Use nested for loops to compute the maximum pixel value in the numpy matrix and print this value out to the terminal. 
im_gray_pixels = asarray(im_gray)
rows, cols = im_gray_pixels.shape
max = 0
for i in range(rows):
    for j in range(cols):
        if(im_gray_pixels[i, j] > max):
            max = im_gray_pixels[i, j]

print("max pixel value: " + str(max))

#Create a new numpy matrix which is the original matrix rotated by 90 degrees counterclockwise. 
#Create a new blank numpy matrix. 
#Use nested for loops to copy the pixel values from the original matrix image to the counterclockwise rotated one.

im_gray_pixels_rotate = np.zeros(shape=(cols,rows))

for j in range(cols):
    for i in range(rows):
        im_gray_pixels_rotate[j, i] = im_gray_pixels[i, j]
        
#Create an image from the rotated matrix.
#Display the counterclockwise rotated image on the screen.
#Write the counterclockwise rotated image to a file.
im_gray_pixels_rotate = Image.fromarray(np.uint8(im_gray_pixels_rotate))
im_gray_pixels_rotate.show()
im_gray_pixels_rotate.save("Beginnings_grayscale_CCWrotated.jpg")

#Create a new numpy matrix which is the original matrix rotated by 90 degrees clockwise.
im_gray_pixels_rotate2 = np.zeros(shape=(cols,rows))
for j in range(cols):
    for i in range(rows):
        im_gray_pixels_rotate2[j, i] = im_gray_pixels[rows-i-1, cols-j-1]

#Create an image from the rotated matrix.
#Display the clockwise rotated image on the screen.
#Write the clockwise rotated image to a file.
im_gray_pixels_rotate2 = Image.fromarray(np.uint8(im_gray_pixels_rotate2))
im_gray_pixels_rotate2.show()
im_gray_pixels_rotate2.save("Beginnings_grayscale_CWrotated.jpg")

#Compute and print the maximum pixel value of the clockwise rotated image. Again, you must compute the maximum value yourself using nested for loops.
cwMax = 0
im_cw_pixels = asarray(im_gray_pixels_rotate2)
rows, cols = im_cw_pixels.shape
for i in range(rows):
    for j in range(cols):
        if(im_cw_pixels[i, j] > cwMax):
            cwMax = im_cw_pixels[i, j]

print("max pixel value of clockwise image: " + str(cwMax))