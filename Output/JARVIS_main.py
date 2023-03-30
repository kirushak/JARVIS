import subprocess
import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os
import smtplib
import time 
import ctypes
import winshell
import pywhatkit

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Jarvis Sir. Please tell me how may I help you")       

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
            
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('kirushakkarasu2004@gmail.com', 'apex_2026')
    server.sendmail('kirushakkarasu2004@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:

        query = takeCommand().lower()

        # Logic for executing tasks 
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("www.youtube.com")
            speak("opening youtube.....")
            time.sleep(10)

        elif 'open google' in query:
            webbrowser.open("www.google.com")
            speak("opening google....")
            time.sleep(10)

        elif 'news' in query:
            webbrowser.open("www.ndtv.com")
            speak('Here are some latest headlines')
            time.sleep(10)

        elif 'search'  in query:
            query = query.replace("search", "")
            webbrowser.open_new_tab(query)
            time.sleep(10)

        elif "open hub" in query:
            webbrowser.open("www.github.com")
            speak("Opening Github....")
            time.sleep(10)

        elif "open whatsapp" in query:
            webbrowser.open("www.whatsapp.com")
            speak("Opening Whatsappp....")
            time.sleep(10)
            
        elif "open instagram" in query:
            webbrowser.open("www.instagram.com")
            speak("Opening Instagram....")
            time.sleep(10)

        elif 'lock the window' in query: 
            speak("locking the device")      
            ctypes.windll.user32.LockWorkStation()

        elif 'shutdown system' in query:
            speak("Hold On a Sec ! Your system is on its way to shut down")
            subprocess.call(["shutdown", "/s"])


        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
            speak("Recycle Bin Recycled")

        elif "locate me jarvis" in query or "locate me" in query:
            query = query.replace("where is", "")
            location = query
            webbrowser.open("www.earth.google.com") 
        
        elif "restart" in query:
            subprocess.call(["shutdown", "/r"])

        elif "sleep" in query:
            speak("sleeping")
            subprocess.call("shutdown / h")


        elif "log off" in query or "sign out" in query:
            speak("Make sure all the application are closed before sign-out")
            time.sleep(5)
            subprocess.call(["shutdown", "/l"])

        elif "open twitter" in query:
            webbrowser.open("www.twitter.com")
            speak("Opening Twitter....")
            time.sleep(10)
  
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        
        elif "don't listen" in query or "stop listening" in query:
            speak("for how much time you want to stop jarvis from listening commands")
            time.sleep(5)
            a = int(takeCommand())
            time.sleep(a)
            print(a)

        elif 'play' in query:
           query = query.replace("play","")
           pywhatkit.playonyt(query)


        elif 'email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "kirushakkarasu2004@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry sir. I am not able to send this email")    

        elif 'thank you' in query:
            speak("most welcome sir, it's my job")