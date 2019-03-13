import cv2
import numpy as np
import matplotlib.pyplot as plt
import sys
from math import cos, pi, sqrt
from PIL import Image
import time

def calculate_cos(n, factor):
    c = np.zeros((n,n))
    s = sqrt(2/n)
    for i in range(n):
        for j in range(n):
            c[i,j] = (cos((j + 0.5) * i * factor) * s)
            
    return c

def calculate_inv_cos(n, factor):
    c = np.zeros((n,n))
    s = sqrt(2/n)
    for i in range(n):
        for j in range(1, n):
            c[i,j] = (cos(factor * j * (i + 0.5)) * s)
            
    return c

def dct(row, c):
#def dct(row):
    N = len(row)
    result = []
    factor = pi / N
    s = sqrt(2/N)
    
    for i in range(N):
        sum = 0.0
        for j in range(N):
            sum += row[j] * c[j,i]
        result.append(sum * s)

    return result
    #return row.dot(c)

def dct2d(img):
    N = img.shape
    c = calculate_cos(N[1], pi/N[1])
    rows = np.zeros_like(img).astype('float32')
    columns = np.zeros_like(img).astype('float32')

    for i in range(N[0]):
        rows[i,:] = dct(img[i,:],c)
    #rows = np.apply_along_axis(dct, 1, img, c)
    rows[0,:] /= sqrt(2)

    c = calculate_cos(N[0], pi/N[0])
    for j in range(N[1]):
        columns[:,j] = dct(rows[:,j],c)
    #columns = np.apply_along_axis(dct, 0, rows, c)

    return columns

def inverse_dct(row, c):
#def inverse_dct(row):
    N = len(row)
    result = []
    factor = pi / N

    for i in range(N):
        sum = row[0] / 2

        for j in range(1, N):
            sum += row[j] * cos(factor * j * (i + 0.5))
            
        result.append(sum * sqrt(2/N))

    return result
#    return row.dot(c)

def inverse_dct2d(cosines):
    N = cosines.shape
    rows = np.zeros_like(cosines).astype('float32')
    columns = np.zeros_like(cosines).astype('float32')

    c = calculate_inv_cos(N[0], pi/N[0])
    for i in range(N[1]):
        rows[:,i] = inverse_dct(cosines[:,i],c)
    
    #rows = np.apply_along_axis(inverse_dct, 1, cosines, c)
    #rows = np.clip(rows, 0, 255)
    c = calculate_inv_cos(N[1], pi/N[1])
    for j in range(N[0]):
        columns[j,:] = inverse_dct(rows[j,:],c)
    #columns = np.apply_along_axis(inverse_dct, 0, rows, c)
    columns = np.clip(columns, 0, 255)

    return columns

def dct_graph(cosines):
    N = cosines.shape[1]
    result = []

    for i in range(N):
        x = np.sum(cosines[:,i])
        result.append(x)

    return np.array(result)

def get_n_cosines(y, n):
    d = y.copy()
    aux = np.zeros_like(d)
    d = sorted(d.ravel(), key=abs)
    d = d[::-1]
    for i in range(n):
        x = np.where(d[i] == y)
        aux[x[0][0], x[1][0]] = d[i]
            
    return aux

def plot(d):
    x = dct_graph(d)
    plt.plot(np.linspace(0,256,x.shape[0]),x)
    plt.show()
    
if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("USAGE: python dct.py filename N")
        sys.exit(1)

    filename = sys.argv[1]
    img = cv2.imread(filename)
    n = int(sys.argv[2])
    b,g,r = cv2.split(img)
    start = time.time()
    b = dct2d(b)
    g = dct2d(g)
    r = dct2d(r)
    print("dct conversion done")
    

    b = get_n_cosines(b, n)
    g = get_n_cosines(g, n)
    r = get_n_cosines(r, n)
    print("cosines selection done")
    b = inverse_dct2d(b)
    g = inverse_dct2d(g)
    r = inverse_dct2d(r)
    print("inverse dct conversion done")
    end = time.time()
    print("time = " + str(end - start))
    x = cv2.merge((b,g,r))
    
    x = np.array(x).astype('uint8')
    x = x[:,:,::-1]
    Image.fromarray(x).show()
    
