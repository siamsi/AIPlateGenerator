import cv2 as cv
from PIL import ImageFont, ImageDraw, Image
import numpy as np
import os

back= cv.imread('Back.jpg')
large2 = cv.imread('2.png')
large8 = cv.imread('t2.png')
back= cv.imread('Back.jpg')
back= cv.resize(back, (int(back.shape[1]*1.2), int(back.shape[0]*1.2)))
back[15:15+large2.shape[0],55:55+large2.shape[1], :] =large2
back[15:15+large8.shape[0],110:110+large8.shape[1], :] =large8
cv.imshow('img', back)
cv.waitKey()
