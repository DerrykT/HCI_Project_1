# cv2 library is used for computer vision work

import cv2
import pyttsx3
from tkinter import Tk, Label
from PIL import Image, ImageTk

engine = pyttsx3.init('sapi5')
engine.setProperty('voices', 'voices[0].id')

outOfFrameCommands = ["Move to the right.", "Move to original spot.", "Move to the left.", "Move to original spot."]


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


fullImagePath = "full_image.jpg"
topLeftPath = "segmented/top_left.jpg"
topRightPath = "segmented/top_right.jpg"
bottomLeftPath = "segmented/bottom_left.jpg"
bottomRightPath = "segmented/bottom_right.jpg"

imagePath = "testImage.jpg"
cascPath = "cascades/haarcascade_fontalface_default.xml"

# Create the haar cascade
faceCascade = cv2.CascadeClassifier(cascPath)


def show_image():
    root = Tk()
    root.title("Current Image")

    image = Image.open(fullImagePath)
    photo = ImageTk.PhotoImage(image)

    label = Label(root, image=photo)
    label.pack()

    root.mainloop()


def divide_photo():
    img = cv2.imread(fullImagePath)

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
    cv2.imwrite(bottomRightPath, l1)
    # rotate image to 90 COUNTERCLOCKWISE
    l2 = cv2.rotate(l2, cv2.ROTATE_90_COUNTERCLOCKWISE)
    # save image
    cv2.imwrite(topRightPath, l2)

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
    cv2.imwrite(bottomLeftPath, r1)

    # rotate image 90 COUNTERCLOCKWISE
    r2 = cv2.rotate(r2, cv2.ROTATE_90_COUNTERCLOCKWISE)

    # save image
    cv2.imwrite(topLeftPath, r2)


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
    filename = fullImagePath
    cv2.imwrite(filename, camera_capture)
    del (camera)


def detect_face(filePath):
    # Read the image
    image = cv2.imread(filePath)
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


def get_formatted_photo(command, index):
    count_down()
    take_photo()
    divide_photo()

    inFullPhoto = detect_face(fullImagePath)
    if not inFullPhoto:
        speak("You are not in frame. " + outOfFrameCommands[index])
        return get_formatted_photo(command, (index + 1) % len(outOfFrameCommands))

    inTopLeft = detect_face(topLeftPath)

    if inTopLeft:
        print("Top Left")
        if command == "top left":
            speak("Found In Frame")
            return
        elif command == "top right":
            speak("Found in top left. Move to the right to be in frame.")
            return get_formatted_photo(command, index)
        elif command == "bottom left":
            speak("Found in top left. Move down to be in frame.")
            return get_formatted_photo(command, index)
        else:
            speak("Found in top left. Move down and to the right to be in frame.")
            return get_formatted_photo(command, index)

    inTopRight = detect_face(topRightPath)

    if inTopRight:
        print("Top Right")
        if command == "top left":
            speak("Found in top right. Move to the left to be in frame.")
            return get_formatted_photo(command, index)
        elif command == "top right":
            speak("Found In Frame")
            return
        elif command == "bottom left":
            speak("Found in top right. Move down and to the left to be in frame.")
            return get_formatted_photo(command, index)
        else:
            speak("Found in top right. Move down to be in frame.")
            return get_formatted_photo(command, index)

    inBottomLeft = detect_face(bottomLeftPath)

    if inBottomLeft:
        print("Bottom Left")
        if command == "top left":
            speak("Found in bottom left. Move up to be in frame.")
            return get_formatted_photo(command, index)
        elif command == "top right":
            speak("Found in bottom left. Move up and to the right to be in frame.")
            return get_formatted_photo(command, index)
        elif command == "bottom left":
            speak("Found In Frame")
            return
        else:
            speak("Found in bottom left. Move to the right to be in frame.")
            return get_formatted_photo(command, index)

    inBottomRight = detect_face(bottomRightPath)

    if inBottomRight:
        print("Bottom Right")
        if command == "top left":
            speak("Found in bottom right. Move up and to the left to be in frame.")
            return get_formatted_photo(command, index)
        elif command == "top right":
            speak("Found in bottom right. Move up to be in frame.")
            return get_formatted_photo(command, index)
        elif command == "bottom left":
            speak("Found in bottom right. Move left to be in frame.")
            return get_formatted_photo(command, index)
        else:
            speak("Found In Frame")
            return

    show_image()
