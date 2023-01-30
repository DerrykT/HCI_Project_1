# import speech_recognition as sr
import pyttsx3
import cv2

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', 'voices[0].id')

engine.say("Hello World")



# Get user supplied values
imagePath = "C:/Users/Derry/PycharmProjects/HCI_Project_1.2/testImage.jpg"
cascPath = "cascades/haarcascade_fontalface_default.xml"

# Create the haar cascade
faceCascade = cv2.CascadeClassifier(cascPath)

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

for x, y, width, height in faces:
    print("Working")
    print(x)
    print(y)
    print(width)
    print(height)
    cv2.rectangle(image, (x, y), (x + width, y + height), color=(255, 0, 0), thickness=2)

cv2.imwrite("test2.jpg", image)