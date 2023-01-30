# cv2 library is used for computer vision work

import cv2
import pyttsx3

from voice_util import speak

fullImagePath = "testImage.jpg"
topLeftPath = "top_left.jpg"
topRightPath = "top_right.jpg"
bottomLeftPath = "bottom_left.jpg"
bottomRightPath = "bottom_right.jpg"


imagePath = "testImage.jpg"
cascPath = "cascades/haarcascade_fontalface_default.xml"

# Create the haar cascade
faceCascade = cv2.CascadeClassifier(cascPath)

def divide_photo():
    img = cv2.imread('testImage.jpg')

    # start vertical divide
    height = img.shape[0]
    width = img.shape[1]
    # Cut  image in half
    width_cutoff = width // 2
    left1 = img[:, :width_cutoff]
    right1 = img[:, width_cutoff:]

    # Dividing left image horizontally
    # Rotate image 90 CLOCKWISE
    img = cv2.rotate(left1, cv2.ROTATE_90_CLOCKWISE)
    # start vertical division
    height = img.shape[0]
    width = img.shape[1]

    width_cutoff = width // 2
    l1 = img[:, :width_cutoff]
    l2 = img[:, width_cutoff:]

    # Rotate image 90 COUNTERCLOCKWISE
    l1 = cv2.rotate(l1, cv2.ROTATE_90_COUNTERCLOCKWISE)
    # save image
    cv2.imwrite("bottom_left.jpg", l1)
    # rotate image to 90 COUNTERCLOCKWISE
    l2 = cv2.rotate(l2, cv2.ROTATE_90_COUNTERCLOCKWISE)
    # save image
    cv2.imwrite("top_left.jpg", l2)

    # Dividing right image horizontally
    # rotate image 90 CLOCKWISE
    img = cv2.rotate(right1, cv2.ROTATE_90_CLOCKWISE)
    # Start vertical division
    height = img.shape[0]
    width = img.shape[1]

    width_cutoff = width // 2
    r1 = img[:, :width_cutoff]
    r2 = img[:, width_cutoff:]

    # Rotate image 90 COUNTERCLOCKWISE
    r1 = cv2.rotate(r1, cv2.ROTATE_90_COUNTERCLOCKWISE)

    # save image
    cv2.imwrite("bottom_right.jpg", r1)

    # rotate image 90 COUNTERCLOCKWISE
    r2 = cv2.rotate(r2, cv2.ROTATE_90_COUNTERCLOCKWISE)

    # save image
    cv2.imwrite("top_right.jpg", r2)


def take_photo():
    # This program takes and saves a selfie from your webcam
    # int the current directory.
    camera_port = 0
    ramp_frames = 30
    camera = cv2.VideoCapture(camera_port)

    def get_image():
        retval, im = camera.read()
        return im

    for i in range(ramp_frames):
        temp = camera.read()

    camera_capture = get_image()
    filename = "testImage.jpg"
    cv2.imwrite(filename, camera_capture)
    del (camera)


def detect_face():
    # Read the image
    image = cv2.imread(imagePath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    return len(faces) > 0

def count_down():
    speak("3")
    speak("2")
    speak("1")

def get_formatted_photo(command):
    count_down()
    take_photo()
    divide_photo()

    in_full_photo = detect_face(fullImagePath)
    if not in_full_photo:
        speak("You are not in frame. Try moving around to get in frame.")
        return get_formatted_photo(command)

    # in_top_left = detect_face()



