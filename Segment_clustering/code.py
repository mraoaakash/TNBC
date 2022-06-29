import imagecodecs
import shutil
import tifffile as tiff
import os
import numpy as np

def create_dataset(path):
	imlist=[]
	labels=[]
	n=200000
	for file in os.listdir(path)[:n]:
		linker = str(os.path.join(path, file))
		img = tiff.imread(linker)
		imlist.append(list(np.array(img).reshape(-1)))
		labels.append(str(linker))
	imlist = np.array(imlist)
	print(imlist)
	print(labels)
	np.savetxt("/home/aakash.rao_ug23/TNBC/gitrepo/tnbc/Segment_clustering/images.csv",imlist, delimiter=',')
	with open('/home/aakash.rao_ug23/TNBC/gitrepo/tnbc/Segment_clustering/labels.txt', 'w+') as f:
		for line in labels:
			f.write(line)
			f.write('\n')


create_dataset("/storage/tnbc/segments/224:224/Raw")
