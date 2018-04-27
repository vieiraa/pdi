import numpy as np
import yiq
from PIL import Image
import sys

def negative(image):
    neg = np.zeros((image.height, image.width, 3), 'uint8')

    for i in range(image.width):
        for j in range(image.height):
            r, g, b = image.getpixel((i, j))

            neg[j, i, 0] = 255 - r
            neg[j, i, 1] = 255 - g
            neg[j, i, 2] = 255 - b

    return neg

def negative_y(image, width, height):
    neg = np.zeros((height, width, 3), 'float32')

    for i in range(width):
        for j in range(height):
            y = image[j, i, 0]
            ii = image[j, i, 1]
            q = image[j, i, 2]

            neg[j, i, 0] = 1-y
            neg[j, i, 1] = ii
            neg[j, i, 2] = q

    return neg

def main():
    if len(sys.argv) < 2:
        print("Usage: python " + sys.argv[0] + " image_name")
        sys.exit(1)
        
    img = Image.open(sys.argv[1])
    
    print("1 - Aplicar negativo em RGB")
    print("2 - Aplicar negativo em Y")
    print("0 - Sair")
    
    option = int(input("Selecione uma opção: "))
    
    if option == 1:
        im = negative(img)
        im = Image.fromarray(im)
        im.show()
        
    elif option == 2:
        im = yiq.rgb2yiq(img)
        im = negative_y(im, img.width, img.height)
        im = yiq.yiq2rgb(im, img.width, img.height)
        im = Image.fromarray(im)
        im.show()
        
    else:
        sys.exit(0)
        
if __name__ == "__main__":
    main()
