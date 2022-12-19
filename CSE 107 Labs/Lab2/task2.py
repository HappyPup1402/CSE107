# Import pillow
from PIL import Image, ImageOps
# Import numpy
import numpy as np
from numpy import asarray
# Read the image from file.
im = Image.open('Watertower.tif')
# Show the image.
im.show()
# Print the image mode.
print("image mode is:", im.mode)
# Create numpy matrix to access the pixel values.
im_pixels = asarray(im)
# Import myImageInverse from myImageInverse
from MyImageFunctions import myImageInverse
im_inv_pixels = myImageInverse(im_pixels)
# Create an image from im_inv_pixels.
im_inv = Image.fromarray(np.uint8(im_inv_pixels))
# Show the inverse image.
im_inv.show()
# Save the inverse image to a file.
im_inv.save("Watertower_inv.tif")