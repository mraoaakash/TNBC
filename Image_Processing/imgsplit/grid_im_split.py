import imagecodecs
import tifffile as tiff
import cv2
import random
import json
import shutil, os
from random import randint
import fnmatch
import hashlib
from PIL import Image
import numpy as np


exclude = ['benchmark','segments']
exclude_im=["20200220-515-191_17-1049_17A-HER2-Biopsy-HnE-40X.tif","20200220-161-112_15-619_15_A-HER2-Biopsy-HnE-40X.tif", "20200220-142-246_15-3385_15_A-HER2-Biopsy-HnE-40X.tif", "20210821_752_307_19_W3_19_H7_ER_Surgery_HnE_40X.tif", "20210821_897_497_19_1816_19_A_ER_biopsy_HnE_40X.tif"]

def new_randcrop(files):
    size=224
    filekey = dict()
    x=0
    dir = "/storage/tnbc"
    key="hne"
    for file in files:
        path=file[0]
        img = tiff.imread(path,0) #brings the image into memory
        print(str(file[1]))
    #     for i in range(0,img.shape[0]-size,+img.shape[0]//10):
    #         for j in range(0, img.shape[1]-size, +img.shape[1]//10):
    #             random.seed(x)
    #             w = i+ randint(0,img.shape[0]//10-size)
    #             random.seed(x)
    #             l = j+ randint(0,img.shape[1]//10-size)
    #             crop = img[w:(w+size) ,l:(l+size)] #crops size squared area around the defined random coordinate
    #             newfilename = "patch_"+str(x)+".tif"
    #             filepath = "/storage/tnbc/segments/newseg/224/"+newfilename
    #             cv2.imwrite(filepath, crop) #saves the image with the filepath mentioned above
    #             filekey[newfilename] = {"name":file[1], "oldpath": path, "newpath":filepath, "x":w, "y":l, "seed":x, "size":size, "im_shape":img.shape, "md5sum":hashlib.md5(filepath).hexdigest()}
    #             x+=1
    # with open("/storage/tnbc/segments/newseg/224/metadata_224.json", "w+") as outfile:
    #     json.dump(filekey, outfile)

def keyimgs(key="hne"):
	# PLEASE CHANGE THIS FILE PATH TO YOUR LOCAL FILE PATH IF RUN LOCALLY
    array = []
    dir = "/storage/tnbc"
    for subdir, dirs, files in os.walk(dir):
        dirs[:] = [d for d in dirs if d not in exclude]
        files[:] = [f for f in files if f not in exclude_im]
        for file in files:
            if fnmatch.fnmatch(file, '*.tif'):
                if key in file.lower():
                    prpath=str(os.path.join(subdir, file))
                    array.append((prpath, file))
    new_randcrop(array)

keyimgs()