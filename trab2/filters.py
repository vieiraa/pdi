import convolution as conv
from PIL import Image
import numpy as np
import sys

def apply_filter(image, kernel):
    return conv.conv_image(image, kernel)

def main():
    if len(sys.argv) < 2:
        print("Usage: python " + sys.argv[0] + " image_name")
        sys.exit(1)
        
    img = Image.open(sys.argv[1])
    
    kernel2 = np.array([[-1/8,-1/8,-1/8],
                        [-1/8,   1,-1/8],
                        [-1/8,-1/8,-1/8]])

    kernel3 = np.array([[-1,0,1],
                        [-1,0,1],
                        [-1,0,1]])

    kernel4 = np.array([[-1,-1,-1],
                        [ 0, 0, 0],
                        [ 1, 1, 1]])

    kernel5 = np.array([[-1,-1,0],
                        [-1, 0,1],
                        [ 0, 1,1]])
    
    kernel6 = np.array([[0,0, 0],
                        [0,1, 0],
                        [0,0,-1]])  
    
    kernel7 = np.array([[0,0,-1],
                        [0,1, 0],
                        [0,0, 0]])
    
    kernel8 = np.array([[ 0, 0,2],
                        [ 0,-1,0],
                        [-1, 0,0]])

    print("1 - Aplicar filtro de aguçamento")
    print("\n2 - Aplicar filtro de detecção de bordas:\n\t\t", kernel2[0], "\n\t\t", kernel2[1], "\n\t\t", kernel2[2])
    print("\n3 - Aplicar filtro de detecção de bordas:\n\t\t", kernel3[0], "\n\t\t", kernel3[1], "\n\t\t", kernel3[2])
    print("\n4 - Aplicar filtro de detecção de bordas:\n\t\t", kernel4[0], "\n\t\t", kernel4[1], "\n\t\t", kernel4[2])
    print("\n5 - Aplicar filtro de detecção de bordas:\n\t\t", kernel5[0], "\n\t\t", kernel5[1], "\n\t\t", kernel5[2])
    print("\n6 - Aplicar filtro de relevo:\n\t\t", kernel6[0], "\n\t\t", kernel6[1], "\n\t\t", kernel6[2])
    print("\n7 - Aplicar filtro de relevo:\n\t\t", kernel7[0], "\n\t\t", kernel7[1], "\n\t\t", kernel7[2])
    print("\n8 - Aplicar filtro de relevo:\n\t\t", kernel8[0], "\n\t\t", kernel8[1], "\n\t\t", kernel8[2])
    print("0 - Sair") 

    option = int(input("\nSelecione uma opção: "))
    
    if option == 1:
        
        c = int(input("\nSelecione o valor de c: "))
        d = int(input("\nSelecione o valor de d: "))

        kernel1 = np.array([[0,-c,0],
                            [-c,4*c+d,-c],
                            [0,-c,0]])

        im = apply_filter(img, kernel1)
        im = Image.fromarray(im)
        im.show("Kernel1 a1")

        kernel1 = np.array([[-c,   -c,-c],
                            [-c,8*c+d,-c],
                            [-c,   -c,-c]])

        im = apply_filter(img, kernel1)
        im = Image.fromarray(im)
        im.show("Kernel1 a2")

    elif option == 2:
        im = apply_filter(img, kernel2)
        im = Image.fromarray(im)
        im.show("Kernel2")
        
    elif option == 3:
        im = apply_filter(img, kernel3)
        im = Image.fromarray(im)
        im.show("Kernel3")

    elif option == 4:
        im = apply_filter(img, kernel4)
        im = Image.fromarray(im)
        im.show("Kernel4")
    
    elif option == 5:
        im = apply_filter(img, kernel5)
        im = Image.fromarray(im)
        im.show("Kernel5")

    elif option == 6:
        im = apply_filter(img, kernel6)
        im = Image.fromarray(im)
        im.show("Kernel6")

    elif option == 7:
        im = apply_filter(img, kernel7)
        im = Image.fromarray(im)
        im.show("Kernel7")

    elif option == 8:
        im = apply_filter(img, kernel8)
        im = Image.fromarray(im)
        im.show("Kernel8")

    else:
        sys.exit()
    
if __name__ == "__main__":
    main()
    
