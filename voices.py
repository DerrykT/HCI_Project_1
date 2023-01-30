import pyttsx3
import speech_recognition as sr

def speak(audio):
    r = sr.Recognizer()

    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voices', 'voices[0].id')

    engine.say(audio)
    engine.runAndWait()


def take_command():
    r = sr.Recognizer()

# Device index 1 is the second microphone on the local machines list of available mic's

# sr.Microphone.list_microphone_names()    <-- this command lists available mics on local machine

# ['Microsoft Sound Mapper - Input', 
# 'Microphone (Realtek(R) Audio)', 
# 'Microsoft Sound Mapper - Output', 
# 'Speakers (Realtek(R) Audio)', 
# 'Primary Sound Capture Driver', 
# 'Microphone (Realtek(R) Audio)',
# 'Primary Sound Driver', ...] 


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

