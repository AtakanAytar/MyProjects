import os


def downloads():
    os.system("py -m pip install --upgrade pip")
    
    os.system("pip install SpeechRecognition")
    
    os.sytem("pip install gTTS")
    
    
    os.system("pip install pipwin")
    os.system("pipwin install pyaudio")

    os.system("pip install pyttsx3")
    os.system("pip install pywin32")

    os.system("pip install pyjokes")
    return None

#To use pip in windows remember to add scripts  to enviorment variables
# if this is your first time add python scripts then comment out next line
#downloads()


import speech_recognition as sr 
import pyttsx3
import sys 
import time 
import datetime
import webbrowser
import pyjokes



def listen(): 
      
    r = sr.Recognizer() 
      
    with sr.Microphone() as source: 
        print("Listening...") 
        r.pause_threshold = 1
        audio = r.listen(source) 
    try: 
        print("Recognizing...")     
        voice_input_from_user = r.recognize_google(audio, language ="en")
        print("You said "+voice_input_from_user)
    except Exception as e:     
        print("There was a error") 
        #raise SystemExit  
        return "None"
    
    voice_input_from_user=voice_input_from_user.lower() 
   
    return voice_input_from_user

def speak(engine,sentence):
    engine.say(sentence) 
    engine.runAndWait() 
    return None

def respond_to_user_input(engine,sentence,name):
    print(sentence)
    if(sentence.count("terminate")>=1):
        speak(engine,"I am terminating the execution of the machine")
        raise SystemExit 
    elif sentence =="open youtube":
        webbrowser.open('https://www.youtube.com/')
    elif sentence=="open google" :
        webbrowser.open('https://www.google.com/')
    elif sentence.count("google")>0:
        query=sentence.replace("google","");
        search="https://www.google.com/search?q="+query+"&oq="+query+"&aqs=chrome..69i60j69i59j69i57j69i60l4j69i65.1805j0j7&sourceid=chrome&ie=UTF-8"
        webbrowser.open(search)
    elif(sentence=="who am i" or sentence=="what is my name"):
        speak(engine,"You are "+ name)
    elif(sentence=="tell me a joke"):
        speak(engine,pyjokes.get_joke())
    elif(sentence=="what is your name" or sentence=="who are you"):
        speak(engine,"My name is The machine")
    elif(sentence=="shutdown pc"):
        os.system("shutdown /s")
    elif(sentence.count("take note")>0):
        out_file=open("note.txt","a+")
        speak(engine,"What do you want to note?")
        note=listen()
        out_file.write(note)
        out_file.close()
    elif(sentence.count("read notes")>0):
        in_file=open("note.txt","r")
        all_file=in_file.read()
        speak(engine,all_file)
    elif(sentence=="What time is it"):
        hour=str(datetime.datetime.now().hour)
        speak(engine,hour)


        
 




    else:
        return None
    

def greetings(engine): 
    hour = int(datetime.datetime.now().hour)
    if hour>= 8 and hour<12: 
        speak(engine,"Good Morning Sir")    
    elif hour>= 12 and hour<18: 
        speak(engine,"Good Afternoon Sir")       
    elif hour>=18 and hour<24:
        speak(engine,"Good Evening Sir")
    else:
        speak(engine,"You are a late nighter Sir")
    speak(engine,"How may i adress you ?")
    name=listen()
    
    return name   

def pyttsx3_engine(gender):
    engine = pyttsx3.init('sapi5') 
    voices = engine.getProperty('voices') 
    engine.setProperty('voice', voices[gender].id)
    engine.setProperty('rate', 125)
    return engine  


def main():
    
    engine=pyttsx3_engine(0)
    name=greetings(engine)
    speak(engine,"Welcome "+ name)
    while(True):
        user_input=""
        user_input=listen()
        respond_to_user_input(engine,user_input,name)



main()


