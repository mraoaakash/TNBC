from datetime import datetime
import time
import imagecodecs
import shutil
import tifffile as tiff
import os
import fnmatch
import numpy as np

def create_dataset(path):
	imlist=[]
	labels=[]
	for file in os.listdir(path):
		if fnmatch.fnmatch(file, '*.tif'):
			linker = str(os.path.join(path, file))
			img = tiff.imread(linker)
			imlist.append(list(np.array(img).reshape(-1)))
			labels.append(str(linker))
	imlist = np.array(imlist)
	np.savetxt("/home/aakash.rao_ug23/TNBC/gitrepo/tnbc/Segment_clustering/images_625.csv",imlist, delimiter=',')
	with open('/home/aakash.rao_ug23/TNBC/gitrepo/tnbc/Segment_clustering/labels_625.txt', 'w+') as f:
		for line in labels:
			f.write(line)
			f.write('\n')

create_dataset("/storage/tnbc/segments/224:224/Send")
