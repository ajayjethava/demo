import pyttsx3
import datetime
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour< 12:
        speak("Good Morning sir")
    elif hour >= 12 and hour< 18:
        speak("Good Afternoon sir")
    else :
        speak("Good Evening sir")
    speak("i am jarvis sir, how i can help you")


# def takeCommand():
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("listening....")
#         r.pause_threshold = 1
#         audio = r.listen(source)
#     try:
#         print("Recognizing...")
#         query = r.recognize_amazon(audio, language='en-in')
#         print(f"user said: {query}\n")

if __name__ == "__main__":
    #speak("hello sir i am your personal assistant created by Divyesh sir")
    wishMe()
    # takeCommand()