
#--------------->    First step:
# -->import all the required packages
#--> If you have not installed yet write and then import
#--> pip install opencv-python
#-->pip  install numpy

import cv2
import numpy as np

#------------------>    second_step:
# --> read the image and resize it if you want.! and
#---> convert the resized image to Gray scale using opencv function
img=cv2.imread('IMG_4698 6X LF+DF.JPEG')
print(img.shape)

image=cv2.resize(img,(512,512))
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
# ------------->  Third step:'
#--> apply the  morphological opening opertation to the image... and show resukt into the window...
opening=cv2.morphologyEx(gray,cv2.MORPH_OPEN,np.ones((1,1)))


cv2.imshow("opening",opening)
cv2.waitKey(0)
