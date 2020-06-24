# JUNO PJ27 SOUTHERN CIRCUMPOLAR CYCLONES IMAGE SET PROCESSING OPENCV

import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
imgL = cv.imread('ImageSet/JNCE_2020154_27C00059_V01-mapprojected.png',0)
imgR = cv.imread('ImageSet/JNCE_2020154_27C00059_V01-red.png',0)
stereo = cv.StereoBM_create(numDisparities=16, blockSize=15)
disparity = stereo.compute(imgL,imgR)
plt.imshow(disparity,'gray')
plt.show()