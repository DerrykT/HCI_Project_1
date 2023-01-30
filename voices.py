import pyttsx3
import speech_recognition as sr

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


def start():
    command = ''
    speak("Do you want to be positioned in the top left, top right, bottom left, or bottom right?")

    while not (
            command == 'top left' or command == 'top right' or command == 'bottom left' or command == 'bottom right'):

        command = take_command()

        if not (
                command == 'top left' or command == 'top right' or command == 'bottom left' or command == 'bottom right'):
            speak("Issue understanding command. Please try again.")

    speak("Heard " + command)
    # get_formatted_photo(command)


# start()
