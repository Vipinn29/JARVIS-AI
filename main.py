import speech_recognition as sr
import openai
import wikipedia as wk
import win32com.client as win
import webbrowser
import time

speaker = win.Dispatch("SAPI.spVoice")

print("Jarvis AI")
speaker.Speak("Jarvis AI")

def TakeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        # r.pause_threshold =  1
        try:
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
            return query
        except:
            print("Some error occourd, Sorry From Jarvis")
            return "None"

while True:
    query = TakeCommand()

    sites = [["Youtube", "https://www.youtube.com/"],["google", "https://www.google.com/"],["wikipedia", "https://www.wikipedia.com/"],["instagram", "https://www.instagram.com/"]]

    for site in sites:
        if f"Open {site[0]}".lower() in query.lower():
            speaker.Speak(f"Opening {site[0]}")
            webbrowser.open(site[1])

    Time = time.strftime("%H:%M:%S")
    if "time" in query:
        speaker.Speak(f"The time is: {Time}")

    elif query == "quit":
        break

