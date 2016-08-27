from pylab import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
from scipy.misc import imread
from scipy.misc import imresize
import scipy as sp
import matplotlib.image as mpimg
import os
from scipy.ndimage import filters
from PIL import Image

def count_diffs (og, new):
    # returns False, true
    unique, counts = np.unique((og==new), return_counts=True)
    d = dict(zip(unique, counts))
    for u in d:
        if u:
            print ("there are " + str(d[u]) + " similarities")
        else:
            print ("there are " + str(d[u]) + " differences")


if __name__ == "__main__":
    
    og = imread("reaper_og.jpg")
    tosombra = imread("muselk_og.jpg")
    response = imread("reaper_datamoshed.jpg")
    
    # count differences for stats purposes
    count_diffs(og, tosombra)
    
    differences = tosombra == og
    
    datamosh = tosombra - og
    
    '''
    for i,j,k in itertools.product(range(og.shape[0]), range(og.shape[1]), range(og.shape[2])):
        if tosombra[i,j,k] - og[i,j,k] > 0:
            print ("NEGAtIVE")
    '''
    
    imsave("muselks_datamosh.jpg", datamosh)
    imsave("differences.jpg", differences)
    
    #recreate the datamosh
    
    data = np.copy(og)
    
    data = data + datamosh
    
    imsave("recreated_datamosh.jpg", data)
    
    # remove datamosh from response to see differences
    
    new_response = response - datamosh
    
    imsave("recreated_undatamoshed_response_2.jpg", new_response)
    
    '''
    diffs = og == tosombra
    str_diffs = ""
    
    for i,j,k in itertools.product(range(og.shape[0]), range(og.shape[1]), range(og.shape[2])):
        if not diffs[i,j,k]:
            str_diffs += str(tosombra[i,j,k])
            
    print (str_diffs)
    '''