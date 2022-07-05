import imagecodecs
import tifffile as tiff
import numpy as np
import random 
from scipy import fft as fft
import os
from sklearn.cluster import AffinityPropagation



def aff_prop():
    dir = "/home/storage/tnbc/segments/224:224/Send"
    X = np.loadtxt("/storage/tnbc/segments/224:224/images_grayscale_224.csv", delimiter=',')
    clustering = AffinityPropagation(random_state=5).fit(X)
    y_pred = clustering.predict(X)
    print("The predicted labels:\n", y_pred)
    return

aff_prop()
