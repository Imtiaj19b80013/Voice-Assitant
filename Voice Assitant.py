import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import sys
import shutil
import webbrowser
import pywhatkit

engine = pyttsx3.init('sapi5')
voices=engine.getProperty('voices') #getting details of current voice
#print(voices[1].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe(time):
    hour=int(datetime.datetime.now().strftime('%I:%M %p'))
    if hour>=0 and hour<12:
        speak("Good Morning!")
        
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
        
    else:
        speak("Good Evening!")
    
    speak("Hello sir, I am Your personal Assistant.")
def username():
    speak("Hello sir, I am Your personal Assistant.")
    speak("What Should I Call You")
    name=takeCommand()
    speak('Welcome'+name)
    #speak(name)
    columns = shutil.get_terminal_size().columns
     
    print("#####################".center(columns))
    print("Welcome Mr.".center(columns), name.center(columns))
    print("#####################".center(columns))
     
    speak("How can i Help you, Sir?")

def takeCommand():
    #take command from mic andgive output
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio=r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User Said: {query}\n")
    
    except Exception as e:
        #print(e)
        
        print("Say that again please...")
        return "None"
    return query
if __name__=="__main__":
    #wishMe()
    #takeCommand()
    username()
    while True:
    # if 1:
        query = takeCommand().lower() #Converting user query into lower case

        # Logic for executing tasks based on query
        if 'wikipedia' in query:  #if wikipedia found in the query then this block will be executed
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2) 
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("Showing"+ location + "on google map.")
            #speak(location)
            webbrowser.open("https://www.google.com/maps/place/" + location + "")

        #elif "play" in query:
           # song=query.replace("play", "")
           # music=pywhatkit.search
           
        elif 'exit' in query:
            speak("Thanks for giving me your time")
            exit()