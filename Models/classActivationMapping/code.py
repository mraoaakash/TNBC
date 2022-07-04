from keras.applications.resnet import ResNet50
from keras.preprocessing import image 
from keras.applications.resnet import preprocess_input, decode_predictions
import numpy as np

model = ResNet50(weights='imagenet')

img_path = '/Users/mraoaakash/Desktop/TNBC/images/editedimages/625:625/Send/20190610_2_518-16_G-18-285_Biopsy_ER_HnE_40X_cropped_9199_18398_22'


print("Loading ResNet50 model...")