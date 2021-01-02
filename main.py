import numpy as np
import cv2
from Algorithms import Algorithms 
from skimage.measure import label
from matplotlib import pyplot as plt 
img = cv2.imread('./UTFVP/0053_3_1_120511-103050.png',cv2.CV_8U)
print(img.shape)
algorithms = Algorithms()
# BINARY REGION GROWING
#algorithms.showImage(img,"Original Image")
#otsu_img = algorithms.apply_otsu(img)
#algorithms.showImage(otsu_img,"After OTSU Thresholding")
#dila_img = algorithms.apply_dilation(otsu_img,3,10)
#dila_img_1 = algorithms.apply_dilation(dila_img,3,10)
#algorithms.showImage(dila_img,"After Dilation")
#region_growing = algorithms.region_growing_binary(dila_img)
#algorithms.showImage(region_growing,"After Region Growing")
#imC = cv2.applyColorMap(region_growing, cv2.COLORMAP_JET)
#algorithms.showImage(imC,"Color Map")

# GRAY LEVEL REGION GROWING
# Resimler arası kopmaları engellemek için ilk önce dilation uygulayacağım.
#img = algorithms.apply_dilation(img,7,2)
labeled = algorithms.region_growing_gray(img)
u8 = labeled.astype(np.uint8)
algorithms.showImage(u8,"asd")
imC = cv2.applyColorMap(u8, cv2.COLORMAP_JET)
algorithms.showImage(imC,"Color Map")