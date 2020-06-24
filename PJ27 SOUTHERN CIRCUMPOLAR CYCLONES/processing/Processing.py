# JUNO PJ27 SOUTHERN CIRCUMPOLAR CYCLONES IMAGE SET PROCESSING OPENCV

import numpy as np
import cv2 as cv

img = cv.imread('ImageSet/JNCE_2020154_27C00059_V01-mapprojected.png')
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
img2 = cv.cvtColor(img, cv.COLOR_BGR2HLS_FULL)
cv.imshow('BGR2RGB', img)
cv.imshow('BGR2HLS_FULL', img2)
cv.waitKey(0)
cv.destroyAllWindows() 