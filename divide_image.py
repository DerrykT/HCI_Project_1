import cv2
img = cv2.imread('savedImage.jpg')
#start vertical divide
height = img.shape[0]
width = img.shape[1]
# Cut  image in half
width_cutoff = width // 2
left1 = img[:, :width_cutoff]
right1 = img[:, width_cutoff:]

#Dividing left image horizontally
#Rotate image 90 CLOCKWISE
img = cv2.rotate(left1, cv2.ROTATE_90_CLOCKWISE)
# start vertical division
height = img.shape[0]
width = img.shape[1]

width_cutoff = width // 2
l1 = img[:, :width_cutoff]
l2 = img[:, width_cutoff:]

#Rotate image 90 COUNTERCLOCKWISE
l1 = cv2.rotate(l1, cv2.ROTATE_90_COUNTERCLOCKWISE)
#save image 
cv2.imwrite("one_horisont_1.jpg", l1)
#rotate image to 90 COUNTERCLOCKWISE
l2 = cv2.rotate(l2, cv2.ROTATE_90_COUNTERCLOCKWISE)
#save image 
cv2.imwrite("one_horisont_2.jpg", l2)

#Dividing right image horizontally
#rotate image 90 CLOCKWISE
img = cv2.rotate(right1, cv2.ROTATE_90_CLOCKWISE)
# Start vertical division
height = img.shape[0]
width = img.shape[1]

width_cutoff = width // 2
r1 = img[:, :width_cutoff]
r2 = img[:, width_cutoff:]
#Rotate image 90 COUNTERCLOCKWISE
r1 = cv2.rotate(r1, cv2.ROTATE_90_COUNTERCLOCKWISE)
#save image
cv2.imwrite("second_vhorisont_1.jpg", r1)
#rotate image 90 COUNTERCLOCKWISE
r2 = cv2.rotate(r2, cv2.ROTATE_90_COUNTERCLOCKWISE)
#save image
cv2.imwrite("second_horisont_2.jpg", r2)