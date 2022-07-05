from venv import create
import imagecodecs
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
			print("-", end= " ")
	imlist = np.array(imlist)
	np.savetxt("/home/storage/tnbc/segments/625:625/images_625.csv",imlist, delimiter=',')
	with open('/home/storage/tnbc/segments/625:625/labels_625.txt', 'w+') as f:
		for line in labels:
			f.write(line)
			f.write('\n')
	#np.savetxt("/Users/mraoaakash/Desktop/tnbc-1/Segment_clustering/images_625.csv",imlist, delimiter=',')
        #with open('/Users/mraoaakash/Desktop/tnbc-1/Segment_clustering/labels_625.txt', 'w+') as f:
                #for line in labels:
                        #f.write(line)
                        #f.write('\n')

	return (imlist,labels)

create_dataset("/home/storage/tnbc/segments/625:625/Send")
