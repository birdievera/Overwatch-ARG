from pylab import *
import numpy as np
import itertools

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
    
    # twitter img
    
    '''
    og = imread("reaper_og.jpg")
    tosombra = imread("message_to_sombra_twitter.jpg")
    response = imread("reaper_datamoshed.jpg")
    
    different = tosombra-og
    
    imsave("differences_imgur.jpg", different)

    data = np.copy(og)
    
    data = data + different

    imsave("to_sombra_recreated.jpg", data)
    imsave("to_sombra_twitter.jpg", tosombra)
    imsave("to_from_sombra_datamoshed.jpg", response)
    
    print (all(data == tosombra))
    
    
    data2 = np.copy(response)
    
    data2 = data2 + different
    
    imsave("to_from_sombra_plus_compression.jpg", data2)
    '''

    og = np.load("reaper_og.jpg")
    tosombra_og = np.load("muselk_og.jpg")
    tosombra_imgur = np.load("message_to_sombra.jpg")
    response = np.load("reaper_datamoshed.jpg")
    
    print (og['header'])
    print (tosombra_og['header'])
    print (tosombra_imgur['header'])
    print (response['header'])
    
    og = imread("reaper_og.jpg")
    tosombra = imread("message_to_sombra.jpg")
    response = imread("reaper_datamoshed.jpg")
    imgurtosombra = imread("muselk_og.jpg")
    
    print ((tosombra == imgurtosombra))
    
    count_diffs(tosombra, imgurtosombra)
    
    #goal: find the original datamosh by muselk
    
    # count differences for stats purposes
    count_diffs(og, tosombra)
    
    datamosh = tosombra - og
    
    '''
    for i,j,k in itertools.product(range(og.shape[0]), range(og.shape[1]), range(og.shape[2])):
        if tosombra[i,j,k] - og[i,j,k] > 0:
            print ("NEGAtIVE")
    '''
    
    imsave("muselks_datamosh.jpg", datamosh)
    
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