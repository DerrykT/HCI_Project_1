#cv2 library is used for computer vision work

import cv2

# This program takes and saves a selfie from your webcam
# int the current directory.

vid = cv2.VideoCapture(0)

ret, frame = vid.read()

filename = 'savedImage.jpg'
cv2.imwrite(filename, frame)