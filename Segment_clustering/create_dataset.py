from venv import create
from PIL import Image
import os
import fnmatch
import numpy as np

def create_dataset(path):
	imlist=[]
	labels=[]
	for file in os.listdir(path):
		if fnmatch.fnmatch(file, '*.tif'):
			linker = str(os.path.join(path, file))
			img = Image.open(linker).convert('L')
			imlist.append(list(np.array(img).reshape(-1)))
			labels.append(str(linker))
			print("-", end= " ")
	imlist = np.array(imlist)
	np.savetxt("/storage/tnbc/segments/625:625/images_grayscale_625.csv",imlist, delimiter=',')
	with open('/storage/tnbc/segments/625:625/labels_625.txt', 'w+') as f:
		for line in labels:
			f.write(line)
			f.write('\n')
	#np.savetxt("/Users/mraoaakash/Desktop/tnbc-1/Segment_clustering/images_625.csv",imlist, delimiter=',')
	#with open('/Users/mraoaakash/Desktop/tnbc-1/Segment_clustering/labels_625.txt', 'w+') as f:
	#for line in labels:
			#f.write(line)
			#f.write('\n')

	return (imlist,labels)

create_dataset("/storage/tnbc/segments/625:625/Send")
