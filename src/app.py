import cv2
import glob
import os

inputFolder= 'iexec_in'
#outputFolder= 'iexec_out'

i = 0
for img in glob.glob(inputFolder + "/*.jpg"):
    image =cv2.imread(img)
    imgResized =cv2.resize(image, (150,150))
    cv2.imwrite("/iexec_out/image_150.jpg",imgResized)
    imgResized =cv2.resize(image, (300,300))
    cv2.imwrite("/iexec_out/image_300.jpg",imgResized)
    imgResized =cv2.resize(image, (600,600))
    cv2.imwrite("/iexec_out/image_600.jpg",imgResized)
    imgResized =cv2.resize(image, (1200,1200))
    cv2.imwrite("/iexec_out/image_1200.jpg",imgResized)
    i += 1
