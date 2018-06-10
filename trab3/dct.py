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
    d[n:] = 0
    d[:,n:] = 0

    return d

def plot(d):
    plt.plot(np.linspace(0,256,d.shape[0]),d)
    plt.show()
    
if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("USAGE: python dct.py filename N")
        sys.exit(1)

    filename = sys.argv[1]
    img = cv2.imread(filename)
    d = dct2d(img)
    
    n = int(sys.argv[2])
    x = get_n_cosines(d, n)
    x = inverse_dct2d(x)
    x = np.array(x).astype('uint8')
    x = x[:,:,::-1]
    Image.fromarray(x).show()
    
