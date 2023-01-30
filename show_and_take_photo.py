import cv2
from tkinter import Tk, Label
from PIL import Image, ImageTk

# This program will access the users webcam, display the current picture in real time, 
# and then the user has two options: 'q' to quit & 't' to save photo to current directory. 

def show_image():
    root = Tk()
    root.title("Current Image")

    image = Image.open("testImage.jpg")
    photo = ImageTk.PhotoImage(image)

    label = Label(root, image=photo)
    label.pack()

    root.mainloop()


# Create a VideoCapture object to access the webcam
cap = cv2.VideoCapture(0)
def get_image():
    retval, im = cap.read()
    return im

# Check if the webcam is opened correctly
if not cap.isOpened():
    raise Exception("Could not open video device")

while True:
    # Capture a single frame from the webcam
    ret, frame = cap.read()

    # Check if the frame was captured correctly
    if not ret:
        raise Exception("Could not capture frame")

    # Display the captured frame
    cv2.imshow("Webcam", frame)

    # Break the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    elif cv2.waitKey(1) & 0xFF == ord("t"):
        camera_capture = get_image()
        filename = "testImage.jpg"
        cv2.imwrite(filename,camera_capture)
show_image()

# Release the VideoCapture object
cap.release()

# Close all windows
cv2.destroyAllWindows()



