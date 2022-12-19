#MyImageFunctions.py

#Import pillow
from PIL import Image, ImageOps

#Import numpy
import numpy as np
from numpy import asarray

import math

def myImageResize(inImage_pixels, M, N, interpolation_method):
    rows,cols = inImage_pixels.shape
    
    #new numpy matrix for the transformed image
    trans_im_pixels = np.zeros(shape=(M,N)) 
    
    for m in range(M+1):
        for n in range(N+1):
            m_inter = (((m-0.5)/M)*rows) + 0.5
            n_inter = (((n-0.5)/N)*cols) + 0.5
            
            if interpolation_method == 'nearest':
                m_inter = round(m_inter)
                n_inter = round(n_inter)
                trans_im_pixels[m-1,n-1] = inImage_pixels[m_inter-1,n_inter-1]
            elif interpolation_method == 'bilinear':
                
                #this if and else statements are how i find the correct m1 and m2 for the x axis
                if isinstance(m_inter, int):
                    m1 = m_inter-1
                    m2 = m_inter-1
                else:
                    if m_inter < 1:
                        m1 = 0
                        m2 = 1
                    elif m_inter > rows-1:
                        m1 = rows-2
                        m2 = rows-1
                    else:
                        m1 = math.floor(m_inter-1)
                        m2 = math.ceil(m_inter-1)
                        
                #this if and else statements are how i find the correct n1 and n2 for the y axis
                if isinstance(n_inter, int):
                    n1 = n_inter-1
                    n2 = n_inter-1
                else:
                    if n_inter < 1:
                        n1 = 0
                        n2 = 1
                    elif n_inter > cols-1:
                        n1 = cols-2
                        n2 = cols-1
                    else:
                        n1 = math.floor(n_inter-1)
                        n2 = math.ceil(n_inter-1)
            
                #after finding the correct corrdinates, I find the pixels of the original image
                #with the coordinates found and set them to the correct p values to send to the bilinear function to find p5
                p1 = inImage_pixels[m1,n1]
                p2 = inImage_pixels[m1,n2]
                p3 = inImage_pixels[m2,n1]
                p4 = inImage_pixels[m2,n2]
                p5 = 0

                p5 = mybilinear(m1,n1,p1,m1,n2,p2,m2,n1,p3,m2,n2,p4,m_inter-1,n_inter-1,p5)
                
                trans_im_pixels[m-1,n-1] = p5
    
    return trans_im_pixels
    
def myRMSE(first_im_pixels, second_im_pixels):
    #Both pictures are the same size so I only took the shape of the first image
    M, N = first_im_pixels.shape
    sum = 0
    
    #this double for loop represents the intergral going through both pictures to find the pixels
    #value at M and N. this is shown in the lab 03 pdf
    for m in range (M-1):
        for n in range(N-1):
            sum += (first_im_pixels[m,n] - second_im_pixels[m,n])**2
    
    #after finding the sum we multiple it by 1/MN, then square root it.
    sum = math.sqrt(sum/(M*N))
    return sum

def mybilinear(x1,y1,p1,x2,y2,p2,x3,y3,p3,x4,y4,p4,x5,y5,p5):
    
    #eq to find p5' as shwon in the hw
    prime1 = (p3-p1)*((x5-x1)/(x3-x1)) + p1
    
    #eq to find p5'' as shwon in the hw
    prime2 = (p4-p2)*((x5-x2)/(x4-x2)) + p2
    
    ##eq to find the actual value of p5 as shwon in the hw
    p5 = (prime2-prime1)*((y5-y1)/(y2-y1)) + prime1
    
    
    return p5
