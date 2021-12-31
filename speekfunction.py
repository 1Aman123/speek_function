import pyttsx3
import datetime

import speech as speech
from pyttsx3.drivers import sapi5

pyttsx3 - python text to speech extended version 3


pyttsx3.speak("My name is Aman Kumar Choudhary")
x = datetime.datetime.now().hour
print(f"Time is {x}")
if 0 <= x <= 12:
    print("Good Morning ")
    pyttsx3.speak("Good Morning ")
elif 12 < x <= 16:
    print("Good Afternoon ")
    pyttsx3.speak("Good Afternoon ")
elif 16 < x <= 20:
    print("Good Evening ")
    pyttsx3.speak("Good Evening ")
else:
    print("Good Night ")
    pyttsx3.speak("Good Night ")

Ram = pyttsx3.init('sapi5')
sapi5 - speech application program interface version 5
voices = Ram.getProperty('voices')
Ram.setProperty('voice', voices[1].id)
def speak(audio):
    Ram.say(audio)
    Ram.runAndWait()
speak("HELLO Aman")
