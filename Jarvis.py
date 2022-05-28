# Importing essential modules:

import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import pyjokes
import datetime
from pywikihow import search_wikihow
import winsound


# Setting voice setting:

engine = pyttsx3.init('sapi5')                                                              # api is Microsoft's audio intake function.
voices = engine.getProperty('voices')                                                       # to check all available voices in your computer
engine.setProperty('voice', voices[0].id)                                                   # to set voices for your program


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# For welcome and greet:

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    
speak("Hello ISHANI, How may I assist you?")


# Setting microphone settings:
 
def takeCommand():                                                                  # it takes microphone input from users and returns string command
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        
    except Exception as e:
        print("I'm Sorry. What was that again?")
        return "None"
    return query


# For sending E-mails:

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login("youremail@gmail.com","your-password")
    server.sendmail("youremail@gmail.com",to,content)
    server.close()
    

# For Wikipedia search:

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()                                                      # logic for executing tasks based on query
        
        if 'wikipedia' in query:
            speak ('Searching Wikipedia...')
            query = query.replace("Wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        

# For opening different websites:
       
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'open facebook' in query:
            webbrowser.open("facebook.com")
        elif 'news' in query:
            webbrowser.open("news.google.co.in")


# For telling current time:
        
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")


# For opening & closing different applications:
        
        elif 'open code' in query:
            speak("Okay, starting VS Code")
            codePath1 = "C:\\Users\\RISHVEY\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath1)
        
        elif 'open browser' in query:
            speak("Okay, starting Browser")
            codePath2 = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(codePath2)
        
        elif 'open music' in query:
            speak("Okay, starting Spotify")
            codePath3 = "C:\\Users\\RISHVEY\\AppData\\Roaming\\Spotify\\Spotify.exe"
            os.startfile(codePath3)
        
        
        elif 'email to' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "yourEmail@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend, I am not able to send this email")


# For random jokes:
        
        elif 'joke' in query:
            jokes = pyjokes.get_joke(language = "en", category = "all")
            print(jokes)
            speak(jokes)


# For alarm:

        elif 'alarm' in query:
            speak("Enter The Time!")
            time = input("Please Enter The Time: ")
            while True:
                Time_Ac = datetime.datetime.now()
                now = Time_Ac.strftime("%H:%M:%S")
                if now == time:
                    speak("Time to wake up, RishVey")
                    winsound.PlaySound('Star Wars.wav',winsound.SND_FILENAME)
                    speak("Alarm Closed!")
                elif now>time:
                    break


# For Scrap Searching

        elif 'how to' in query:
            speak("Let Me Get Data From The Internet!")
            print("Let Me Get Data From The Internet!")
            op = query.replace("jarvis"," ")
            max_result = 1
            how_to_func = search_wikihow(op, max_result)
            assert len(how_to_func) == 1
            how_to_func[0].print()
            speak(how_to_func[0].summary)
        

# To exit the program:
        
        elif 'exit' in query or 'stop' in query or 'thank you' in query:
            hour = int(datetime.datetime.now().hour)
            if hour >= 21 and hour < 6:
                speak("Good night RishVey, Take Care!")
            else:
                speak("Have a good day RishVey!")
            exit() 