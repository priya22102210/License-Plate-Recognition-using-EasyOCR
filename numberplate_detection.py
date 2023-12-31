# -*- coding: utf-8 -*-
"""NUMBERPLATE_RECOGNIITON.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16a5ptwiP5n4CRago68sEWXuFoNprcrRc

CHECKING VERSION OF CUDA PRESENT IN OUR SYSTEM:
this version will help us download the right pytorch version in our system
"""

#!nvcc --version

"""INSTALLING AND IMPORTING ALL THE REQUIRED PACKAGES

EASYOCR: is a Python package that allows computer vision developers to effortlessly perform Optical Character Recognition text detection with Python.
The EasyOCR package is created and maintained by Jaided AI, a company that specializes in Optical Character Recognition services.
EasyOCR is implemented using Python and the PyTorch library. If you have a CUDA-capable GPU, the underlying PyTorch deep learning library can speed up your text detection and OCR speed tremendously.
can OCR text in 58 languages

IMUTILS:A series of convenience functions to make basic image processing functions such as translation, rotation, resizing, skeletonization, and displaying Matplotlib images easier with OpenCV and both Python 2.7 and Python3

OPENCV:is an open source computer vision and machine learning software library. OpenCV was built to provide a common infrastructure for computer vision applications and to accelerate the use of machine perception in the commercial products. Being an Apache 2 licensed product, OpenCV makes it easy for businesses to utilize and modify the code

PYTORCH:PyTorch is a machine learning framework based on the Torch library, used for applications such as computer vision and natural language processing, originally developed by Meta AI and now part of the Linux Foundation umbrella.

CUDA:CUDA (or Compute Unified Device Architecture) is a parallel computing platform and application programming interface (API) that allows software to use certain types of graphics processing units (GPUs) for general purpose processing, an approach called general-purpose computing on GPUs (GPGPU)
"""

#!pip install easyocr
#!pip install imutils
#!pip install opencv-python-headless==4.1.2.30
#!pip3 install torch torchvision torchaudio

import cv2
from matplotlib import pyplot as plt
import numpy as np
import easyocr
import imutils

"""CONVERT COLORED IMAGE (RGB FORMAT) INTO GRAYSCALE FORMAT:
because image processing in rbg image is a bit complex as comparative to grayscale as rgb has 3 layers,pixel count is high.
"""

#img=cv2.imread("/content/car4.jpg")
#img=cv2.imread("/content/car number.jpg")
img=cv2.imread("/content/car5.jpg")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
plt.imshow(cv2.cvtColor(gray,cv2.COLOR_BGR2RGB))#since matplot lib takes input in colored format only thats why we need to conver it again
img.shape

"""APPLY FILTER AND EDGE DETECTION:
to remove extra data present in the image
BILATERAL FILTER:A bilateral filter is used for smoothening images and reducing noise, while preserving edges.
Canny filter:we use the canny edge detection for many popular tasks in edge detection such as lane detection, sketching, border removal
Theoretical Understanding
The basic steps involved in this algorithm are:


Noise reduction using Gaussian filter

Gradient calculation along the horizontal and vertical axis

Non-Maximum suppression of false edges

Double thresholding for segregating strong and weak edges

Edge tracking by hysteresis

"""

bfilter=cv2.bilateralFilter(gray,11,17,17)#noise reduction #11=bi_ksize ,17=sigma
edged=cv2.Canny(bfilter,30,200)#edge detection #30 and 200 are threshold values
plt.imshow(cv2.cvtColor(edged,cv2.COLOR_BGR2RGB))

!pip install imutils

"""FIND  CONTOURS AND APPLY MASK:
CV2.findcontours:
 src: Input Image of n – dimensional array(n = 2,3) but preferred 2-dim binary images for better result.
contour_retrieval: This is contour retrieval mode. Possible values are :
a) cv2.RETR_TREE
b) cv2.RETR_EXTERNAL
c) cv2.RETR_LIST
d) cv2.RETR_CCOMP etc.
contours_approximation: This is Contour approximation method. Possible values are :
a) cv2.CHAIN_APPROX_NONE
b) cv2.CHAIN_APPROX_SIMPLE

# New Section
"""

keypoints=cv2.findContours(edged.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
#return predefined levels
 #chain_aprx_simple: It excludes all excessive points and compresses the contour, thereby saving memory.to get aprx shape of the contour instead of its pixels
contours=imutils.grab_contours(keypoints)#to store the contours in simpler form
contours=sorted(contours,key=cv2.contourArea,reverse=True)[:10]#sort in descending order of shape area and top 10 shapes

"""# New Section"""

location=None
for contour in contours:
  approx=cv2.approxPolyDP(contour,10,True)# function with a precision factor for approximating a shape
  #we take a curve and reduce its number of vertices while retaining the bulk of its shape
  #here 10 =The eps × peri value acts as the approximation accuracy and will change with each epoch due to eps’s incremental nature.
  if len(approx)==4:
    location=approx
    break

location#will use these 4 keypoints for masking
#A mask is a filter. Concept of masking is also known as spatial filtering.

mask=np.zeros(gray.shape,np.uint8)#will create a black background
new_image=cv2.drawContours(mask,[location],0,255,-1)# used to draw any shape provided you have its boundary points
new_image=cv2.bitwise_and(img,img,mask=mask)#converts img to bitwise
#hence all the pixcels are

plt.imshow(cv2.cvtColor(new_image,cv2.COLOR_BGR2RGB))

(x,y)=np.where(mask==255)
(x1,y1)=(np.min(x),np.min(y))
(x2,y2)=(np.max(x),np.max(y))
cropped_image=gray[x1:x2+1,y1:y2+1]

plt.imshow(cv2.cvtColor(cropped_image,cv2.COLOR_BGR2RGB))

reader=easyocr.Reader(['en'])
result=reader.readtext(cropped_image)
result

text=result[0][-2]
font=cv2.FONT_HERSHEY_SIMPLEX
res=cv2.putText(img,text=text,org=(approx[0][0][0],approx[1][0][1]+60),fontFace=font,fontScale=1,color=(0,255,0),thickness=2)
res=cv2.rectangle(img,tuple(approx[0][0]),tuple(approx[2][0]),(0,255,0),3)
plt.imshow(cv2.cvtColor(res,cv2.COLOR_BGR2RGB))



