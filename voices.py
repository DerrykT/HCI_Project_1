import pyttsx3
import speech_recognition as sr


# r = sr.Recognizer()
#
# with sr.Microphone() as source:
#     engine = pyttsx3.init('sapi5')
#     voices = engine.getProperty('voices')
#     engine.setProperty('voices', 'voices[0].id')
#
#     engine.say("Do you want your face in the top right, top left, bottom right, or bottom left?")
#     engine.runAndWait()
#
#     r.pause_threshold = 0.7
#     audio = r.listen(source)
#     Query = r.recognize_google(audio, language='en-in')
#
#     print("the query is printed='", Query, "'")

def speak(audio):
    r = sr.Recognizer()

    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voices', 'voices[0].id')

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


speak("Speak")
command = take_command()
speak(command)

