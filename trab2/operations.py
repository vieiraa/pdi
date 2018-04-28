import yiq
import sys
import numpy as np
import histogram as hst
from math import floor
from PIL import Image

def cdf(i, hist):
    keys = list(hist.keys())
    values = list(hist.values())
    p = 0
    
    for j in range(len(keys)):
        p += values[j]
        
        if i == keys[j]:
            break
    
    return p
    
def expand(img, width, height):
    hist = hst.make_histogram(img, width, height)
    num_pixels = width * height
    h = {}
    rmax = max(hist)
    rmin = min(hist)

    for r in hist:
        h[r] = floor((r - rmin)*255/(rmax - rmin))

    for j in range(height):
        for i in range(width):
            img[j, i, 0] = h[int(img[j, i, 0])]

    return img

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
    
def main():
    if len(sys.argv) < 2:
        print("Usage: python " + sys.argv[0] + " image_name")
        sys.exit(1)
        
    img = Image.open(sys.argv[1])
    im = yiq.rgb_to_yiq(img)
    
    print("1 - Aplicar expansão de histograma")
    print("2 - Aplicar equalização de histograma")
    print("0 - Sair")
    
    option = int(input("\nSelecione uma opção:"))
    
    if option == 1:
        expand(im, img.width, img.height)
        im = yiq.yiq_to_rgb(im, img.width, img.height)
        im = Image.fromarray(im)
        im.show()
        
    elif option == 2:
        equalize(im, img.width, img.height)
        im = yiq.yiq_to_rgb(im, img.width, img.height)
        im = Image.fromarray(im)
        im.show()
        
    else:
        print("\nFlw")
    
    img.close()
    im.close()
    
if __name__ == "__main__":
    main()