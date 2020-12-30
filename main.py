import numpy as np
import cv2
from Algorithms import Algorithms 
from skimage.measure import label
from matplotlib import pyplot as plt 

img = cv2.imread('./UTFVP/0053_1_1_120511-103029.png',cv2.CV_8U)
print(img.shape)
algorithms = Algorithms()
#algorithms.showImage(img,"Original Image")

otsu_img = algorithms.apply_otsu(img)
algorithms.showImage(otsu_img,"After OTSU Thresholding")
#dila_img = algorithms.apply_dilation(otsu_img,40)
#algorithms.showImage(dila_img,"After Dilation")
region_growing = algorithms.region_growing(otsu_img)
algorithms.showImage(region_growing,"After Region Growing")



 