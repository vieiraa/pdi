import yiq
import numpy as np
import histogram as hst
from math import floor
from PIL import Image

def cdf(i, hist):
    keys = list(hist.keys())
    values = list(hist.values())
    p = 0
    
    for j in range(len(keys)):
        if i == keys[j]:
            break
        
        p += values[j]
    
    return p

def equalize(img, width, height):
    hist = hst.make_histogram(img, width, height)
    num_pixels = width * height
    h = {}
    
    for key in hist:
        h[key] = floor(((cdf(key, hist) - 1)/(num_pixels - 1))*255)
            
    for j in range(height):
        for i in range(width):
            img[j, i, 0] = h[int(img[j, i, 0])]
                
    return img
