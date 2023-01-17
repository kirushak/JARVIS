import speech_recognition as sr  # pip install speechRecognition
import pyttsx3
import datetime
import wikipedia  # pip install wikipedia
import webbrowser # pip install web browser
import os 
import time
import subprocess
import wolframalpha # pip install wolframalpha
import requests
import pywhatkit 
from random import choice 
from pprint import pprint
import smtplib  # pip install smtplib
import pyjokes  # pip install pyjokes

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

            
            ## GUI with all the features including opening local host applications (Saket, Sanjay, Bhashay) - Built for windows only

            
 def find_my_ip():
    ip_address = requests.get('https://api64.ipify.org?format=json').json()
    return ip_address["ip"]
        
        
         if 'ip address' in statement:
            ip_address = find_my_ip()
            speak(f'Your IP Address is {ip_address}.\n Printing your IP address on the screen.')
            print(f'Your IP Address is {ip_address}')
        
         elif 'wikipedia' in statement:
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
            
        elif "open discord" in statement:
            webbrowser.open_new_tab("https://discord.com/channels/@me")
            speak("Opening Discord....")
            
        elif "open whatsapp" in statement:
            webbrowser.open_new_tab("https://web.whatsapp.com/")
            speak("Opening Whatsappp....")
            
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
       
           
def email():
    """Sending email through voice"""
    speak("What is the content of the email?")
    self.query = self.voicecom().lower()

    gmail = input("Enter your email address: ")
    password = input("Enter your password: ")
    send_to_person = input("Enter the receiver email address:")
    message = self.query

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(gmail, password)
    server.sendmail(gmail, send_to_person, message)
    server.quit()
    speak("email has been sent to %s" % send_to_person)
       
        
def jokes():
    """tells joke"""
    joke = pyjokes.get_joke()
    speak(joke)


def date():
    """Returns present date"""
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date1 = int(datetime.datetime.now().day)
    speak("the current date is")
    speak(date1)
    speak(month)
    speak(year)
    
    
    

         ## Whatsapp Messaging Feature (Kirushak) 
                  
                  
                  
                  
                  
                  
                  
                  
                  
       ##Conversation and Random Module Feature (Sanjay and Kirushak)

                  
def get_random_advice():
    res = requests.get("https://api.adviceslip.com/advice").json()
    return res['slip']['advice']
                  
      elif "advice" in query:
            speak(f"Here's an advice for you, sir")
            advice = get_random_advice()
            speak(advice)
            speak("Printing the advice on the screen.")
            pprint(advice)
                  
                  
                  
                  
          
                  
                  
                  
                  
