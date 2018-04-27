import numpy as np
from PIL import Image
import yiq
import sys

def threshold_user(image, thresh):
    thresh /= 255
    
    img = np.zeros((image.height, image.width, 3), 'float32') 
    im = yiq.rgb2yiq(image)
    
    for j in range(image.height):
        for i in range(image.width):
            #img[j, i, 0] = im[j, i, 0]
            
            if im[j, i, 0] <= thresh:
                img[j, i, 0] = 0
            else:
                img[j, i, 0] = 1
                
    return img
    
def threshold_mean(image):
    img = np.zeros((image.height, image.width, 3), 'float32') 
    im = yiq.rgb2yiq(image)

    thresh = 0
    for j in range(image.height):
        for i in range(image.width):
            img[j, i, 0] = im[j, i, 0]
            thresh += img[j, i, 0]
            
    thresh /= (image.width * image.height)
    
    for j in range(image.height):
        for i in range(image.width):
            if img[j, i, 0] <= thresh:
                img[j, i, 0] = 0
            else:
                img[j, i, 0] = 1
                
    return img

def main():
    if len(sys.argv) < 2:
        print("Usage: python " + sys.argv[0] + " image_name")
        sys.exit(1)
        
    img = Image.open(sys.argv[1])
    
    print("1 - Limiar definido pelo usuário")
    print("2 - Limiar por média de valores em Y")
    print("0 - Sair")
    
    option = int(input("Selecione uma opção: "))
    
    if option == 1:
        thresh = int(input("Digite o limiar: "))
        im = threshold_user(img, thresh)
        im = yiq.yiq2rgb(im, img.width, img.height)
        im = Image.fromarray(im)
        im.show()
        
    if option == 2:
        im = threshold_mean(img)
        im = yiq.yiq2rgb(im, img.width, img.height)
        im = Image.fromarray(im)
        im.show()
        
    else:
        sys.exit(0)
        
if __name__ == "__main__":
    main()
