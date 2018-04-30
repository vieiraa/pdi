import numpy as np
from PIL import Image

def conv_pixel(image, x, y, matrix, out, flag_y, offset):
    xc = int(len(matrix[0]) / 2)
    yc = int(len(matrix) / 2)
    
    rt = 0.0
    gt = 0.0
    bt = 0.0
    yt = 0.0
    
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            off_x = x + j - xc
            off_y = y + i - yc
            
            if not flag_y:
                rt += matrix[i, j]*image.getpixel((off_x, off_y))[0]
                gt += matrix[i, j]*image.getpixel((off_x, off_y))[1]
                bt += matrix[i, j]*image.getpixel((off_x, off_y))[2]
            else:
                yt += matrix[i,j]*image[j,i,0]
    
    if not flag_y:
        rt = min(rt, 255)
        gt = min(gt, 255)
        bt = min(bt, 255)
    
        rt = max(rt, 0)
        gt = max(gt, 0)
        bt = max(bt, 0)
    
        out[y, x, 0] = rt + offset
        out[y, x, 1] = gt + offset
        out[y, x, 2] = bt + offset
    
    else:
        yt = min(yt, 255)
        yt = max(yt, 0)
        out = [y, x, 0] = yt + offset
    
def conv_image(image, matrix, flag_y, offset):
    out = ""
    
    if not flag_y:
        out = np.zeros((image.height, image.width, 3), 'uint8')
    else:
        out = np.zeros((image.height, image.width, 3), 'float32')
    
    for y in range(1, image.height-1):
        for x in range(1, image.width-1):
            conv_pixel(image, x, y, matrix, out, flag_y, offset)
    
    return out
