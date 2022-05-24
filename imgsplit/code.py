import imagecodecs
import tifffile as tiff
import cv2
import random
import re
import os
from random import randint

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
			filename = "/home/aakash.rao_ug23/TNBC/imgsplit/editedimages/file_%d.jpg"%d
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
		filepath = "/home/aakash.rao_ug23/TNBC/imgsplit/editedimages/"+filename[0:len(filename)-4]+"_v_"+str(i)+".tif" 
		cv2.imwrite(filepath, crop) #saves the image with the filepath mentioned above





#defines a random image by path
def randpath():

	# PLEASE CHANGE	THIS FILE PATH TO YOUR LOCAL FILE PATH IF RUN LOCALLY
	dir = "/storage/tnbc/OPTRASCAN_IISER_Round_1/IISER_Box_"+str(randint(1,7)) +"/TIFF"
	filename = random.choice(os.listdir(dir))
	path = os.path.join(dir, filename)
	return (path,filename)



#Calls the crop function 
def visit(n):
	for i in range(n):
		tpath = randpath() #generates a random path
		randcrop(tpath[0], tpath[1], 580,500) #Calls the function randcrop

visit(30)

