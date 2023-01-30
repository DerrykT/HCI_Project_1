import pyttsx3
import SpeechRecognition as sr


r = sr.Recognizer()

with sr.Microphone() as source:
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voices', 'voices[0].id')

    engine.say("Do you want your face in the top right, top left, bottom right, or bottom left?")

    r.pause_threshold = 0.7
    audio = r.listen(source)
    Query = r.recognize_google(audio, language='en-in')

    print("the query is printed='", Query, "'")




