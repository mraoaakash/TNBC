import imagecodecs
import tifffile as tiff
import cv2
import random
import re
import os
from random import randint
import fnmatch
import numpy as np


def create_dataset(path):
	imlist=np.array([])
	labels=[17000]
	i=0
	for subdir, dirs, files in os.walk(path):
		for file in files:
			linker = str(os.path.join(subdir, file))
			img = np.array(tiff.imread(linker)).reshape(-1)
			imlist = np.append(imlist,img, axis=0)
			labels[i]=str(file)
			i+=1
	print(imlist)
	print(labels)

create_dataset("/storage/tnbc/segments/625:625/Raw/")
