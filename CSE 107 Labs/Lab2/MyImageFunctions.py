#MyImageFunctions.py
# Import pillow
from PIL import Image, ImageOps
# Import numpy
import numpy as np
from numpy import asarray
def myImageInverse( inImage_pixels ):
    #Determine the size of the input matrix. 
    #Create a new numpy matrix of the same size. 
    im_inverse = asarray(inImage_pixels)
    rows, cols = im_inverse.shape
    #use nested for loops to copy the values from the input matrix to the output matrix using the 
    #equation  out_value  =  255–in_value.  This  is  the  image  inverse  of  a  grayscale image. 
    for i in range(rows):
        for j in range(cols):
            im_inverse[i, j] = 255 - im_inverse[i, j]
            
    max = 0
    for i in range(rows):
        for j in range(cols):
            if(im_inverse[i, j] > max):
                max = im_inverse[i, j]

    print("max pixel value: " + str(max))
    
    
    return im_inverse
    
    
# This function takes as input a numpy matrix representing a grayscale image and
# outputs another numpy matrix which is the image inverse of the input.
# That is, for each pixel, output_value = 255 - input_value
#
# Syntax:
#   out_numpy_matrix = myImageInverse( in_numpy_matrix )
#
# Input:
#   in_numpy_matrix = the grayscale values of the input image
#
# Output:
#   out_numpy_matrix = the grayscale of the inverse image
#
# History:
#   S. Newsam   9/10/22     Created
#   S. Newsam   9/11/22     Modified to use numpy instead of PIL image