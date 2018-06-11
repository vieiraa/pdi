import cv2
import numpy as np
import matplotlib.pyplot as plt
import sys
from math import cos, pi, sqrt
from PIL import Image

def dct(row):
    N = len(row)
    result = []
    factor = pi / N
    
    for i in range(N):
        sum = 0.0
        for j in range(N):
            sum += row[j] * cos((j + 0.5) * i * factor)
        result.append(sum * sqrt(2 / N))

    return result

def dct2d(img):
    N = img.shape
    rows = np.zeros_like(img).astype('float32')
    columns = np.zeros_like(img).astype('float32')

    for i in range(N[0]):
        rows[i,:] = dct(img[i,:])
    rows[0,:] /= sqrt(2)

    for j in range(N[1]):
        columns[:,j] = dct(rows[:,j])

    return columns

def inverse_dct(row):
    N = len(row)
    result = []
    factor = pi / N

    for i in range(N):
        sum = row[0] / 2

        for j in range(1, N):
            sum += row[j] * cos(factor * j * (i + 0.5))
            
        result.append(sum * sqrt(2/N))

    return result

def inverse_dct2d(cosines):
    N = cosines.shape
    rows = np.zeros_like(cosines).astype('float32')
    columns = np.zeros_like(cosines).astype('float32')

    for i in range(N[1]):
        rows[:,i] = inverse_dct(cosines[:,i])

    for j in range(N[0]):
        columns[j,:] = inverse_dct(rows[j,:])

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
    b = dct2d(b)
    g = dct2d(g)
    r = dct2d(r)

    b = get_n_cosines(b, n)
    g = get_n_cosines(g, n)
    r = get_n_cosines(r, n)
    b = inverse_dct2d(b)
    g = inverse_dct2d(g)
    r = inverse_dct2d(r)
    x = cv2.merge((b,g,r))
    
    x = np.array(x).astype('uint8')
    x = x[:,:,::-1]
    Image.fromarray(x).show()
    
