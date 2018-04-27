import numpy as np
import yiq
from PIL import Image
import sys

def aditive_brightness(image, plus):
    img = np.zeros((image.height, image.width, 3), 'uint8')

    for i in range(image.width):
        for j in range(image.height):
            r, g, b = image.getpixel((i, j))

            img[j, i, 0] = min(255, r + plus)
            img[j, i, 1] = min(255, g + plus)
            img[j, i, 2] = min(255, b + plus)
            
    print("Done")

    return img

def multiplicative_brightness(image, mult):
    img = np.zeros((image.height, image.width, 3), 'uint8')

    for i in range(image.width):
        for j in range(image.height):
            r, g, b = image.getpixel((i, j))

            img[j, i, 0] = min(255, r * mult)
            img[j, i, 1] = min(255, g * mult)
            img[j, i, 2] = min(255, b * mult)
            
    print("Done")

    return img

def aditive_brightness_y(image, width, height, plus):
    img = np.zeros((height, width, 3), 'float32')

    for i in range(width):
        for j in range(height):
            y = image[j, i, 0]
            ii = image[j, i, 1]
            q = image[j, i, 2]

            img[j, i, 0] = min(1.0, y + plus)
            img[j, i, 1] = ii
            img[j, i, 2] = q
            
    print("Done")

    return img

def multiplicative_brightness_y(image, width, height, mult):
    img = np.zeros((height, width, 3), 'float32')

    for i in range(width):
        for j in range(height):
            y = image[j, i, 0]
            ii = image[j, i, 1]
            q = image[j, i, 2]

            img[j, i, 0] = min(1.0, y * mult)
            img[j, i, 1] = ii
            img[j, i, 2] = q
            
    print("Done")

    return img

def main():
    if len(sys.argv) < 2:
        print("Usage: python " + sys.argv[0] + " image_name")
        sys.exit(1)
        
    img = Image.open(sys.argv[1])
        
    print("1 - Brilho aditivo em RGB")
    print("2 - Brilho multiplicativo em RGB")
    print("3 - Brilho aditivo em Y")
    print("4 - Brilho multiplicativo em Y")
    print("0 - Sair")
    
    option = int(input("Escolha um opção: "))
    
    if option == 1:
        plus = float(input("Digite o valor a ser adicionado: "))
        im = aditive_brightness(img, plus)
        im = Image.fromarray(im)
        img.show()
        im.show()
        
    elif option == 2:
        mult = float(input("Digite o valor a ser multiplicado: "))
        im = multiplicative_brightness(img, mult)
        im = Image.fromarray(im)
        img.show()
        im.show()
        
    elif option == 3:
        plus = float(input("Digite o valor a ser adicionado: "))
        im = yiq.rgb2yiq(img)
        im = aditive_brightness_y(im, img.width, img.height, plus)
        im = yiq.yiq2rgb(im, img.width, img.height)
        im = Image.fromarray(im)
        img.show()
        im.show()
        
    elif option == 4:
        mult = float(input("Digite o valor a ser multiplicado: "))
        im = yiq.rgb2yiq(img)
        im = multiplicative_brightness_y(im, img.width, img.height, mult)
        im = yiq.yiq2rgb(im, img.width, img.height)
        im = Image.fromarray(im)
        img.show()
        im.show()
        
    else:
        print("Bye")
        sys.exit(0)
        
if __name__ == "__main__":
    main()
