import numpy as np
from PIL import Image
from math import ceil

def image_to_array(image):
    img = np.zeros((image.height, image.width, 3), 'uint8')
    
    for j in range(image.height):
        for i in range(image.width):
            r, g, b = image.getpixel((i, j))
            
            img[j, i, 0] = r
            img[j, i, 1] = g
            img[j, i, 2] = b
            
    return img

def rgb_to_yiq(image):
    yiq = np.zeros((image.height, image.width, 3), 'float32')

    for j in range(image.height):
        for i in range(image.width):
            r, g, b = image.getpixel((i, j))
            
            yiq[j, i, 0] = (0.299*r + 0.587*g + 0.114*b)
            yiq[j, i, 1] = (0.596*r - 0.274*g - 0.322*b)
            yiq[j, i, 2] = (0.211*r - 0.523*g + 0.312*b)

    return yiq

def yiq_to_rgb(yiq, width, height):
    rgb = np.zeros((height, width, 3), 'uint8')

    for j in range(height):
        for i in range(width):
            y = yiq[j, i, 0]
            ii = yiq[j, i, 1]
            q = yiq[j, i, 2]
            
            r = ceil(y + 0.956*ii + 0.621*q)
            r = min(r, 255)
            r = max(r, 0)
            g = ceil(y - 0.272*ii - 0.647*q)
            g = min(g, 255)
            g = max(g, 0)
            b = ceil(y - 1.106*ii + 1.703*q)
            b = min(b, 255)
            b = max(b, 0)
            
            rgb[j, i, 0] = r
            rgb[j, i, 1] = g
            rgb[j, i, 2] = b

    return rgb

def rgb_to_gray(img):
    yiq = rgb_to_yiq(img)
    grey = np.zeros((img.height, img.width, 3), 'uint8')
    for j in range(img.height):
        for i in range(img.width):
            grey[j,i,0] = yiq[j,i,0]
            grey[j,i,1] = yiq[j,i,0]
            grey[j,i,2] = yiq[j,i,0]
            
    return grey



