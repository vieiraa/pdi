import matplotlib.pyplot as pp
import collections

def make_histogram(img, width, height):
    hist = {}
    
    for j in range(height):
        for i in range(width):
            pixel = int(img[j, i, 0])
            
            if pixel not in hist:
                hist[pixel] = 0
            
            hist[pixel] += 1
                        
    return collections.OrderedDict(sorted(hist.items()))

def plot_histogram(hist):
    keys = hist.keys()
    values = hist.values()
    
    pp.bar(keys, values, linewidth=0.1)
    pp.show()
