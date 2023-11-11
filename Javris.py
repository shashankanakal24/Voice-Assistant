import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import subprocess
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = datetime.datetime.now().hour # Corrected the datetime usage
    if 0 <= hour < 12:
        speak("Good Morning")
    elif 12 <= hour < 18:
        speak("Good Afternoon")
    elif 18 <= hour < 24:  # Corrected the condition for evening
        speak("Good Evening")
    else:
        speak("Good Night")

    speak("I am Aroshi Sir. Please tell me how may I help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening Dear....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print(f"Error: {e}")
        print("Say that again, Please...")
        return "None"

    return query

def sendEmail(to,content):
    server =  smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('shashankanakal247@gmail.com','password')
    server.sendmail.com('shashankanakal247@gmail.com',to,content)
    server.close()
    
    

if __name__ == "__main__":
    wishMe()

while True: # can be used if you want command continously
#if 1: 
    query = takeCommand().lower()  # Logic for Executing Task
    if 'wikipedia' in query:
        speak("Searching Wikipedia...")
        query = query.replace("wikipedia", "")  # Remove 'wikipedia' from the query
        try:
            results = wikipedia.summary(query, sentences=2)  # Correct the spelling of 'sentences'
            speak("According to Wikipedia")
            speak(results)
        except wikipedia.exceptions.DisambiguationError as e:
            speak("It seems there are multiple possibilities. Please be more specific.")
        except wikipedia.exceptions.PageError as e:
            speak("I couldn't find any information on that topic.")
            
            
    elif 'open youtube'in query:
        webbrowser.open("youtube.com")
        
    elif 'open google' in query:
        webbrowser.open("google.com")
        
    elif 'open stack overflow' in query:
        webbrowser.open("stackoverflow.com")
        
    elif  'play music' in query:
        music_dir = r'E:\Mp3 Player using Python\Music'
        songs= os.listdir( music_dir)
        print(songs)
        os.startfile(os.path.join(music_dir,songs[0]))
        
    elif 'the time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The time is {strTime}") 
        
    elif 'open code' in query:
        codePath = r'C:\Program Files\JetBrains\PyCharm Community Edition 2023.2.3\bin\pycharm64.exe'
        try:
            result = subprocess.run([codePath], check=True, capture_output=True, text=True)
            print(result.stdout)
            print(result.stderr)
        except subprocess.CalledProcessError as e:
            print(f"Error opening Visual Studio Code: {e}")
            speak("Sorry, I couldn't open PyCharm. Please check if it's installed.")

    elif 'send email' in query:
        try:
            speak("what should I send Send?")
            content = takeCommand()
            to = "shashankanakal247@gmail.com"
            sendEmail(to,content)
            speakk("Email has been sent!")
        except Exception as e:
            print(e)
            speak("Sorry Iam not able to send an Email")
            
            


        
    
        
        
    
        
        
            


            
            
    
    




