# Imgsplit
### Introduction
This piece of code serves as a part of the image pipleine used to prepare images for machine learning. The different functions of this script carry out varying image manipulation tasks in order to generate images with sufficient granularity. The use case of this code is specifically catering to the image processing of cancer biopsy images. 

The problem at hand for us was to build a pipeline that randomly selects an image from a repository and randomly samples a defined number of sub-images from it. Here, we have defined our level of granularity at 580\*580px in order to retain sufficient detail in the images. This value will wary depending on the stage of the study at which we are at as well as the type of image being used.

### Functions
#### imcrop(path,size)
This function takes a path and a size. Upon opening the image at the defined path, it splits the entire image length and breath wise into successive components. The image below illustrates the number of splits:


<img src="./images/imgrop-01.png?raw=true" width="1000"/>



#### Function_2()
Info

#### Function_3()
Info
