import pyttsx3
import speech_recognition as sr
import cv2

import divide_image

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

            # Displaying exception
            print(e)
            print("Say that again sir")
            return "NONE"

    return Query


def start():
    command = take_command()

    if command == 'top left' or command == 'top right' or command == 'bottom left' or command == 'bottom right':
        speak("You said" + command)
    else:
        speak("Issue understanding command. Please try again.")
        start()

    get_formatted_photo()


speak("Do you want to be positioned in the top left, top right, bottom left, or bottom right?")
start()
