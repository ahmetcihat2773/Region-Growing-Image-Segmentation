import numpy as np
import cv2
from Algorithms import Algorithms 
from skimage.measure import label
from matplotlib import pyplot as plt 

img = cv2.imread('./UTFVP/0007_6_3_120523-110018.png',cv2.CV_8U)
print(img.shape)
algorithms = Algorithms()
#algorithms.showImage(img,"Original Image")

otsu_img = algorithms.apply_otsu(img)
#algorithms.showImage(otsu_img,"After OTSU Thresholding")
algorithms.region_growing(otsu_img)
#dila_img = algorithms.apply_dilation(otsu_img,10)
#algorithms.showImage(dila_img,"After Dilation")

 