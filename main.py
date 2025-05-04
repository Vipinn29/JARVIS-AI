import speech_recognition as sr
from openai import OpenAI
import win32com.client as win
import webbrowser
import datetime
import os

speaker = win.Dispatch("SAPI.spVoice")

chatStr = ""

def chat(prompt):
    global chatStr

    client = OpenAI(
        api_key="sk-vAn5ZActfdOlo3FREgPOThVc7UiedU6GmuACKjpyjAr7YmQK",
        base_url="https://api.chatanywhere.tech/v1"
    )

    chatStr += f" User: {prompt}\n Jarvis: "
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f" User: {prompt}\n Jarvis: "}
        ],
        logprobs=True,
    )
    
    chatStr += f"{completion.choices[0].message.content}\n"
    print(chatStr)
    speaker.Speak(completion.choices[0].message.content)
    return completion.choices[0].message.content


def AI(prompt):
    client = OpenAI(
        api_key="sk-vAn5ZActfdOlo3FREgPOThVc7UiedU6GmuACKjpyjAr7YmQK",
        base_url="https://api.chatanywhere.tech/v1"
    )

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"{prompt}"}
        ],
        logprobs=True,
    )

    if not os.path.exists("OpenAI"):
        os.mkdir("OpenAI")

    with open(f"OpenAI/{''.join(prompt.split('AI')[1:]).strip()}.txt", "w") as f:  
        f.write(f"OpenAI Response for Query: {prompt} \n-------------------------\n\n")
        f.write(completion.choices[0].message.content)


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
        except Exception as e:
            print(f"Some error occourd, Sorry From Jarvis")
            return "None"

# Main Function
if __name__ == '__main__':
    print("Welcome to Jarvis AI")
    speaker.Speak("Welcome to Jarvis AI")

    while True:
        query = TakeCommand()

        # Add more Sites as well
        sites = [["Youtube", "https://www.youtube.com/"],["google", "https://www.google.com/"],["wikipedia", "https://  www.wikipedia.com/"],["instagram", "https://www.instagram.com/"]]

        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                speaker.Speak(f"Opening {site[0]}")
                webbrowser.open(site[1])


        Dt = datetime.datetime.now()
        if "Time".lower() in query.lower():
            speaker.Speak(f"The time is: {Dt.strftime('%X')}")


        if "Date".lower() in query.lower():
            speaker.Speak(f"The Date is: {Dt.strftime('%x')}")


        if "Day".lower() in query.lower():
            speaker.Speak(f"Today is: {Dt.strftime('%A')}")


        elif "Using AI".lower() in query.lower():
            AI(prompt=query)
    

        elif  "Jarvis quit".lower() in query.lower():
            exit()


        elif "reset chat".lower() in query.lower():
            chatStr = ""


        else:
            print("Chatting...")
            chat(query)

