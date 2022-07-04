import imagecodecs
import tifffile as tiff
import numpy as np
import random 
from scipy import fft as fft
import os

from Segment_clustering.create_dataset import create_dataset

def d_cos_t():
    dir = "/Users/mraoaakash/Desktop/TNBC/images/editedimages/625:625/Send"
    filename = random.choice(os.listdir(dir))
    path = os.path.join(dir, filename)
    img = np.array(tiff.imread(path)).reshape(-1)
    img_cos = fft.dct(img)
    print("The transform:\n", img_cos)
    print("The shape of the transform:\n", img_cos.shape)
    print("The shape of the imager:\n", img.shape)
    return 

