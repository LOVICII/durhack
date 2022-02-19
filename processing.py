import cv2
import numpy as np
import os
import glob
import requests

def enlarge(img):
    scale_percent = 200 
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    
    # resize image
    img = cv2.resize(img, dim, interpolation = cv2.INTER_CUBIC)

    return img

def noise_removel(img):
    # bilateral filter
    img = cv2.bilateralFilter(img, 1, 100, 100)
    return img

def sharpen(img):
    # laplacian sharpening
    kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
    img = cv2.filter2D(img, -1, kernel=kernel)
    return img

def bright_contrast(img):
    # CLAHE
    clahe = cv2.createCLAHE(clipLimit=1, tileGridSize=(3, 3))
    # For ease of understanding, we explicitly equalize each channel individually
    colorimage_b = clahe.apply(img[:,:,0])
    colorimage_g = clahe.apply(img[:,:,1])
    colorimage_r = clahe.apply(img[:,:,2])
    # Next we stack our equalized channels back into a single image
    img = np.stack((colorimage_b,colorimage_g,colorimage_r), axis=2)

    return img


path = 'coloured_imgs/*.jpg'
dest = 'results/'


# Recursive through all images
for filename in glob.iglob(path):
    print(filename)
    img = cv2.imread(filename)

    img = enlarge(img) 
    img = noise_removel(img)    
    img = sharpen(img)   
    img = bright_contrast(img) 
  
    cv2.imwrite(os.path.join(dest , filename.split("\\")[1]), img)

