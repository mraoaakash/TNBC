#import imagecodecs
# import tifffile as tiff
# import cv2
import random
import re
import shutil, os
from random import randint
import fnmatch

#crops a defined image
def imcrop(path,size):
	img = tiff.imread(path, 0)
	#helper and counter variables
	a=img.shape
	i=0
	d=0
	j=0

	#crops and exports chunks of the images
	while i <= a[0]-size-1:
		j=0
		while j <= a[1]-size-1:
			crop = img[j:(j+size), i:(i+size),:]
			filename = "./TNBC/gitrepo/tnbc/Image_Processing/imgsplit/editedimages/file_%d.jpg"%d
			crop = cv2.resize(crop,(224,224))
			cv2.imwrite(filename, crop)
			d=d+1
			j+=size
		i=i+size




#crops n random regions of the image 
def randcrop(path, filename, size, num):
	img = tiff.imread(path,0) #brings the image into memory
	for i in range(0,num):
		w = randint(0, img.shape[0]-size-1) 
		l = randint(0, img.shape[1]-size-1) #gets random (x,y) coordinates
		crop = img[w:(w+size) ,l:(l+size)] #crops size squared area around the defined random coordinate

		# PLEASE CHANGE THIS FILE PATH TO YOUR LOCAL FILE PATH IF RUN LOCALLY 
		filepath = "./TNBC/gitrepo/tnbc/Image_Processing/imgsplit/editedimages/"+filename[0:len(filename)-4]+"_cropped_"+str(w)+"_"+str(l)+".tif" 
		cv2.imwrite(filepath, crop) #saves the image with the filepath mentioned above





#defines a random image by path
def randpath():

	# PLEASE CHANGE	THIS FILE PATH TO YOUR LOCAL FILE PATH IF RUN LOCALLY
	dir = "/Users/mraoaakash/Desktop/TNBC/images/editedimages/224:224/Raw"
	filename = random.choice(os.listdir(dir))
	path = os.path.join(dir, filename)
	return (path,filename)



#Calls the crop function 
def visit(n):
	for i in range(n):
		tpath = randpath() #generates a random path
		shutil.copy(tpath[0], '/Users/mraoaakash/Desktop/TNBC/images/editedimages/224:224/Send')
		#randcrop(tpath[0], tpath[1], 580,10) #Calls the function randcrop
	print(array)


#returns all .tif files from the entire storage by mapping 
#from the root inside all subdirectories. This returns a path
#to every single .tif file in the entire directory defined
#by the user
def tiffimgs():
	# PLEASE CHANGE THIS FILE PATH TO YOUR LOCAL FILE PATH IF RUN LOCALLY
	dir = "/storage/tnbc"
	for subdir, dirs, files in os.walk(dir):
		for file in files:
			if fnmatch.fnmatch(file, '*.tif'):
				prpath=str(os.path.join(subdir, file))
				#call your preferred function here
				#can be randcrop or imgcrop or any
				#custom function


#does the same function as tiffimgs() while ensuring that
#the paths accepted are only thos of images with 'key' in
#their name. This can be used to run certian functions on
#specifically HnE/Vimentin/CD31 files.
def keyimgs(key):
	# PLEASE CHANGE THIS FILE PATH TO YOUR LOCAL FILE PATH IF RUN LOCALLY
	dir = "/storage/tnbc"
	for subdir, dirs, files in os.walk(dir):
		for file in files:
			if fnmatch.fnmatch(file, '*.tif'):
				if key in file.lower():
					prpath=str(file+"\n")
					#call yout preferred function here
					#can be	randcrop or imgcrop or any
					#custom function


visit(5000)