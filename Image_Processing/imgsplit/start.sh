#! /bin/bash
#PBS -N TNB_IMG_split
#PBS -o out.log
#PBS -e err.log
#PBS -l ncpus=50
#PBS -q gpu

module load compiler/anaconda3
source /home/aakash.rao_ug23/TNBC/gitrepo/tnbc/Image_Processing/imgsplit/env/bin/activate
python3 /home/aakash.rao_ug23/TNBC/gitrepo/tnbc/Image_Processing/imgsplit/grid_im_split.py