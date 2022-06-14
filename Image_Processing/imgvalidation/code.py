import imagecodecs
import tifffile as tiff
import random
import re
import os
from random import randint
import fnmatch
import hashlib
import json
os.environ["OPENCV_IO_MAX_IMAGE_PIXELS"] = pow(2,50).__str__()
import cv2



#returns all .tif files from the entire storage by mapping 
#from the root inside all subdirectories. This returns a path
#to every single .tif file in the entire directory defined
#by the user
def genmd5():
	dict = {}
	# PLEASE CHANGE THIS FILE PATH TO YOUR LOCAL FILE PATH IF RUN LOCALLY
	dir = "/storage/tnbc"
	jsonFile = open("/home/aakash.rao_ug23/TNBC/gitrepo/tnbc/Image_Processing/imgvalidation/data.json", "w+")
	for subdir, dirs, files in os.walk(dir):
		for file in files:
			path = os.path.join(subdir, file)
			command = "md5sum " +  path
			sum = os.popen(command).read()
			if len(sum)>0: sum=sum.split()[0]
			print(sum)
			dict[str(file)] = {'path':path, 'md5':sum} 
	print(dict)
	jsonString = json.dumps(dict)
	jsonFile.write(jsonString)


genmd5()
