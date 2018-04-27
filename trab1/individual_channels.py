import numpy as np
from PIL import Image
import sys

def image_split_monochromatic(image):
    r = np.zeros((image.height, image.width, 3), 'uint8')
    g = np.zeros((image.height, image.width, 3), 'uint8')
    b = np.zeros((image.height, image.width, 3), 'uint8')

    for i in range(image.width):
        for j in range(image.height):
            rc, gc, bc = image.getpixel((i, j))
            r[j, i, 0] = r[j, i, 1] = r[j, i, 2] = rc
            g[j, i, 0] = g[j, i, 1] = g[j, i, 2] = gc
            b[j, i, 0] = b[j, i, 1] = b[j, i, 2] = bc

    return r, g, b

def image_split_color(image):
    r = np.zeros((image.height, image.width, 3), 'uint8')
    g = np.zeros((image.height, image.width, 3), 'uint8')
    b = np.zeros((image.height, image.width, 3), 'uint8')

    for i in range(image.width):
        for j in range(image.height):
            rc, gc, bc = image.getpixel((i, j))
            r[j, i, 0] = rc
            g[j, i, 1] = gc
            b[j, i, 2] = bc

    return r, g, b

def main():
    if len(sys.argv) < 2:
        print("Usage: python " + sys.argv[0] + " image_name")
        sys.exit(1)
        
    img = Image.open(sys.argv[1])
    
    print("1 - Exibir bandas individuais como imagens monocromáticas")
    print("2 - Exibir bandas individuais como imagens coloridas")
    
    option = int(input("Selecione uma opção: "))
    
    if option == 1:
        r, g, b = image_split_monochromatic(img)
        
        while True:
            print("\n1 - Exibir banda R")
            print("2 - Exibir banda G")
            print("3 - Exibir banda B")
            print("0 - Sair")
            
            option = int(input("Selecione uma opção: "))
            
            if option == 0:
                break
            
            elif option == 1:
                im = Image.fromarray(r)
                im.show()
                
            elif option == 2:
                im = Image.fromarray(g)
                im.show()
                
            elif option == 3:
                im = Image.fromarray(b)
                im.show()
                
    else:
        r, g, b = image_split_color(img)
        
        while True:
            print("\n1 - Exibir banda R")
            print("2 - Exibir banda G")
            print("3 - Exibir banda B")
            print("0 - Sair")
            
            option = int(input("Selecione uma opção: "))
            
            if option == 0:
                break
            
            elif option == 1:
                im = Image.fromarray(r)
                im.show()
                
            elif option == 2:
                im = Image.fromarray(g)
                im.show()
                
            elif option == 3:
                im = Image.fromarray(b)
                im.show()
                
if __name__ == "__main__":
    main()
