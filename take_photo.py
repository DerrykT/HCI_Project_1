#cv2 library is used for computer vision work

import cv2

# This program takes and saves a selfie from your webcam
# int the current directory.

vid = cv2.VideoCapture(0)

ret, frame = vid.read()

filename = 'savedImage.jpg'
cv2.imwrite(filename, frame)


# camera_port = 0
# ramp_frames = 30
# camera = cv2.VideoCapture(camera_port)
# def get_image():
#  retval, im = camera.read()
#  return im
# for i in range(ramp_frames):
#  temp = camera.read()
#
# camera_capture = get_image()
# filename = "testImage.jpg"
# cv2.imwrite(filename,camera_capture)
# del(camera)