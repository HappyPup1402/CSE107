# MyHEFunctions.py

# Import numpy
import numpy as np

def compute_histogram( image_pixels ):
    # compute_histogram computes the histogram of the input image.
    # Syntax:
    #   compute_histogram( image_pixels )
    #
    # Input:
    #   image_pixels = The input image pixels.
    #
    # Output:
    #   return = The histogram of the input image.
    
    #
    # History:
    #   I. Ramirez     11/13/2022   created
    
    histogram = np.zeros(shape=(256))
    rows,cols = image_pixels.shape
    for x in range(rows):
        for y in range(cols):
            histogram[int(image_pixels[x][y])] += 1
    histogram = histogram / np.sum(histogram)

    return histogram

def equalize( in_image_pixels ):
    # equalize  Performs histogram equalization on the input image.
    # Syntax:
    #   equalize( in_image_pixels )
    #
    # Input:
    #   in_image_pixels = The input image pixels.
    #
    # Output:
    #   return = The equalized image pixels.
    #
    # History:
    #   I. Ramirez     11/13/2022   created
    
    histogram = compute_histogram(in_image_pixels)
    sum = np.cumsum(histogram)
    transform = (256-1) * sum / sum[-1]
    equalized_image = np.interp(in_image_pixels.flatten(), range(256), transform)
    equal_img = equalized_image.reshape(in_image_pixels.shape)
    return equal_img


def plot_histogram( hist ):
    # plot_histgram  Plots the length 256 numpy vector representing the normalized
    # histogram of a grayscale image.
    #
    # Syntax:
    #   plot_histogram( hist )
    #
    # Input:
    #   hist = The length 256 histogram vector..
    #
    # Output:
    #   none
    #
    # History:
    #   S. Newsam     11/13/2022   created

    # Import plotting functions from matplotlib.
    import matplotlib.pyplot as plt

    plt.bar( range(256), hist )

    plt.xlabel('intensity value')

    plt.ylabel('PMF'); 

    plt.show()