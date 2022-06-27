#! /bin/bash
#PBS -N TNBC_Segment_clustering
#PBS -o out.log
#PBS -e err.log
#PBS -l ncpus=10
#PBS -q gpu

module load compiler/anaconda3
source /home/aakash.rao_ug23/TNBC/gitrepo/tnbc/Image_Processing/imgsplit/env/bin/activate
python3 /home/aakash.rao_ug23/TNBC/gitrepo/tnbc/Segment_clustering/code.py

