from threading import Thread

import pyttsx3
import speech_recognition as sr
import cv2

import photo_utils

engine = pyttsx3.init('sapi5')
engine.setProperty('voices', 'voices[0].id')


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def take_command():
    r = sr.Recognizer()

    with sr.Microphone(device_index=1) as source:

        r.pause_threshold = 0.7
        audio = r.listen(source)

        try:

            # Listening voice commands in indian english
            Query = r.recognize_google(audio, language='en-in')

        except Exception as e:
            return "NONE"

    return Query


def begin_gui():
    # Create a VideoCapture object to access the webcam
    cap = cv2.VideoCapture(0)

    def get_image():
        retval, im = cap.read()
        return im

    print("Hello")
    thread = Thread(target=start)

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

        if cv2.waitKey(33) == 27:
            print("Heard1")
            break
        elif cv2.waitKey(33) == 32 and not thread.is_alive():
            print("Heard2")
            thread.start()

    # Release the VideoCapture object
    cap.release()

    # Close all windows
    cv2.destroyAllWindows()


def start():
    command = ''
    speak("Do you want to be positioned in the top left, top right, bottom left, or bottom right?")

    while not (
            command == 'top left' or command == 'top right' or command == 'bottom left' or command == 'bottom right'
            or 'top left' in command or 'top right' in command
            or 'bottom left' in command or 'bottom right' in command):

        command = take_command()

        if not (command == 'top left' or command == 'top right' or command == 'bottom left' or command == 'bottom right'
                or 'top left' in command or 'top right' in command
                or 'bottom left' in command or 'bottom right' in command):
            speak("Issue understanding command. Please try again.")

    speak("Heard " + command)
    print("Heard " + command)
    photo_utils.get_formatted_photo(command)
