import imagecodecs
import tifffile as tiff
import numpy as np
import random 
from scipy import fft as fft
import os
from sklearn.cluster import AffinityPropagation

from Segment_clustering.create_dataset import create_dataset

def aff_prop():
    dir = "/Users/mraoaakash/Desktop/TNBC/images/editedimages/625:625/Send"
    X = create_dataset()[0]
    y_original = create_dataset()[1]
    clustering = AffinityPropagation(random_state=5).fit(X)
    y_pred = clustering.predict(X)
    print("The predicted labels:\n", y_pred)
    return

aff_prop()