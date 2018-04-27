import numpy as np
import yiq
from PIL import Image
from math import ceil
import sys

def mean(arr):
    m = 0
    for k in arr:
        m += k
        
    return int(m/len(arr))

def median(arr):
    size = len(arr)
    arr = list(np.sort(arr))
    
    if size % 2 == 0:
        return int((arr[int(size/2)] + arr[int(size/2+1)])/2)
    else:
        return arr[int(size/2) + 1]
    
def get_pixels(img, x, y, size):
    #im = np.zeros((img.height, img.width, 3), 'uint8')
    r = []
    g = []
    b = []
    limit = range(-size + ceil(size/2), size - int(size/2)+1)
    L = abs(min(limit))
    U = max(limit)
    
    for j in range(y-L, y+U):
        for i in range(x-L, x+U):
            for band in range(3):
                if band == 0:
                    try:
                        r.append(img.getpixel((i, j))[0])
                    except:
                        r.append(0)
                elif band == 1:
                    try:
                        g.append(img.getpixel((i, j))[1])
                    except:
                        g.append(0)
                else:
                    try:
                        b.append(img.getpixel((i, j))[2])
                    except:
                        b.append(0)
    
    return (r, g, b)
    
def mean_filter(img, size):
    copy = img.copy()
    
    for j in range(img.height):
        for i in range(img.width):
            r, g, b = get_pixels(img, i, j, size)
            r = mean(r)
            g = mean(g)
            b = mean(b)
            
            copy.putpixel((i, j), (r, g, b))
            
    return copy
            
def median_filter(img, size):
    copy = img.copy()
    
    for j in range(img.height):
        for i in range(img.width):
            r, g, b = get_pixels(img, i, j, size)
            r = median(r)
            g = median(g)
            b = median(b)
            
            copy.putpixel((i, j), (r, g, b))
            
    return copy

def main():
    if len(sys.argv) < 2:
        print("Usage: python " + sys.argv[0] + " image_name")
        sys.exit(1)
        
    img = Image.open(sys.argv[1])
    
    print("1 - Aplicar filtro de média")
    print("2 - Aplicar filtro de mediana")
    print("0 - Sair")
    
    option = int(input("Selecione uma opção: "))
    
    if option == 1:
        size = int(input("\nDigite o tamanho do kernel: "))
        im = mean_filter(img, size)
        im.show()
    
    elif option == 2:
        size = int(input("\nDigite o tamanho do kernel: "))
        im = median_filter(img, size)
        im.show()
    
    else:
        sys.exit(0)
        
if __name__ == "__main__":
    main()
