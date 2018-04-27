import numpy as np
import yiq
from PIL import Image
from math import ceil,sqrt
import convolution as conv
import sys

def laplacian_filter(image):
    kernel = np.array([[0,1,0],
                       [1,-4,1],
                       [0,1,0]])
    
    return conv.conv_image(image, kernel)

def sobel_filter(image):    
    out = np.zeros((image.height, image.width, 3), 'uint8')
    
    kernel_x = np.array([[1,0,-1],
                         [2,0,-2],
                         [1,0,-1]])
    kernel_y = np.array([[1,2,1],
                         [0,0,0],
                         [-1,-2,-1]])
    
    out_x = conv.conv_image(image, kernel_x)
    out_y = conv.conv_image(image, kernel_y)
    
    for y in range(image.height):
        for x in range(image.width):
            out[y,x,0] = ceil(sqrt(out_x[y,x,0]**2 + out_y[y,x,0]**2))
            out[y,x,1] = ceil(sqrt(out_x[y,x,1]**2 + out_y[y,x,1]**2))
            out[y,x,2] = ceil(sqrt(out_x[y,x,2]**2 + out_y[y,x,2]**2))
            
    return out

def main():
    if len(sys.argv) < 2:
        print("Usage: python " + sys.argv[0] + " image_name")
        sys.exit(1)
        
    img = Image.open(sys.argv[1])
    
    print("1 - Aplicar filtro laplaciano")
    print("2 - Aplicar filtro de Sobel")
    print("0 - Sair")
    
    option = int(input("Selecione uma opção: "))
    
    if option == 1:
        im = laplacian_filter(img)
        im = Image.fromarray(im)
        im.show()
        
    elif option == 2:
        im = sobel_filter(img)
        im = Image.fromarray(im)
        im.show()
        
    else:
        sys.exit(0)
        
if __name__ == "__main__":
    main()
