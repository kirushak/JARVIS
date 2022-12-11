import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
import wolframalpha
import requests
import pywhatkit


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("Sir, how can i help you")

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

## Edited

if __name__=='__main__':


    while True:
        speak("Tell me how can I help you now?")
        statement = takeCommand().lower()
        if statement==0:
            continue

        if "good bye" in statement or "ok bye" in statement or "stop" in statement:
            speak('Jarvis is shutting down,Good bye')
            print('Jarvis is shutting down,Good bye')
            break

            
            ## Code for opening local applications on host's device (Saket) - Pending

            
            
            
            if 'wikipedia' in statement:
            speak('Searching Wikipedia...')
            statement =statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("Opening Youtube....")
            time.sleep(5)

        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Opening Google Chrome...")
            time.sleep(5)

        elif 'open gmail' in statement:
            webbrowser.open_new_tab("gmail.com")
            speak("Opening Gmail...")
            time.sleep(5)
      

        elif "open facebook" in statement:
            webbrowser.open_new_tab("https://facebook.com/login")
            speak("Opening Facebook....")
   
        elif "open instagram" in statement:
            webbrowser.open_new_tab("https://instagram.com/login")
            speak("Opening Instagram....")
            
          elif "open twitter" in statement:
            webbrowser.open_new_tab("https://twitter.com/login")
            speak("Opening Twitter....")
            
            
            elif "open github" in statement:
            webbrowser.open_new_tab("https://github.com/login")
            speak("Opening Github....")
           
         
          elif 'search'  in statement:
            statement = statement.replace("search", "")
            webbrowser.open_new_tab(statement)
            time.sleep(5)
            
           
        elif 'time' in statement:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")
            
            
        elif 'news' in statement:
            news = webbrowser.open_new_tab("https://ndtv.com")
            speak('Here are some latest headlines')
            time.sleep(6)

        elif "log off" in statement or "sign out" in statement:
            speak("Logging off all applications...")
            subprocess.call(["shutdown", "/l"])

            time.sleep(3)





         ## Whatsapp Messaging Feature (Kirushak)
                  
                  
                  
                  
                  
                  
                  
                  
                  
       ##Conversation and Random Module Feature (Sanjay)

                  
                  
                  
      
                  
                  
                  
                  
          
                  
                  
                  
                  
