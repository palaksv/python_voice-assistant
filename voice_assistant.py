import pyttsx3   #converts text to speech
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import time 


def sptext():
    recognizer=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio=recognizer.listen(source)
        try:
            print("recognizing...")
            data= recognizer.recognize_google(audio)
            return data
        except sr.UnknownValueError:
            print("Not understanding")
            
# sptext()
            
def speechtx(x):
    engine= pyttsx3.init()
    voices= engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)   #0 means male voice, 1 means female voice
    rate=engine.getProperty('rate')
    engine.setProperty('rate',150)
    engine.say(x)
    engine.runAndWait()
    
# speechtx("hello welcome")

if __name__ == '__main__':
    
 if  "hey peter" in sptext().lower():
    while True:
        data1=sptext().lower()
        if "your name" in data1:
            name="my name is peter"
            speechtx(name)
        elif "old are you" in data1:
            age="i am two years old"
            speechtx(age)
        elif "time" in data1:
            time=datetime.datetime.now().strftime("%I%M%p")
            speechtx(time)
        elif "youtube" in data1:
            webbrowser.open("https://www.youtube.com/")
        elif "joke" in data1:
            joke_1=pyjokes.get_joke(language='en',category='neutral')
            speechtx(joke_1)
        elif "exit" in data1:
            speechtx("thank you")
            break
        time.sleep(5)
            
 else:
        print("thanks")
        
    
    