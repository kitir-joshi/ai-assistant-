import pyttsx3
import datetime
import time
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import pywhatkit
import pyautogui
from googletrans import Translator
import httpcore
from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtCore import QTimer,QTime,QDate,Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from qe import  Ui_MainWindow
# from playsound import playsound

engine=pyttsx3.init()
voices=engine.getProperty('voices')
rate = engine.getProperty('rate')
engine.setProperty('rate',180)
# print(voices)
engine.setProperty('voice',voices[1].id) # 1 for girl voice #0 for male voice
# engine.say("hello ritik")
# engine.runAndWait()
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)
    # print(hour)
    if (hour>=0 and hour<12):
        speak('good morning')
        
    elif (hour>=12 and hour<18):
        speak("good afternoon")
    
    else:
        speak("good evening")
    
    speak("i am raniplease tell me how can i help you")

def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening.......")  
        r.pause_threshold=1
        audio=r.listen(source)


    try:
        print("recognising.....")
        query=r.recognize_google(audio,language='hi')
        # query=transla
        # tiont(query)
        print(f"user said:{query}\n")
        return query
    except Exception as e:
        speak("sir can you speak again")
        # return None 
        rj = takecommand()
        return rj
        
        
        

    # return query


def translationt(text):
    line =str(text)
    translator =Translator()
    result= translator.translate(line)
    data=result.text
    return data
 
# class mainthread(QThread):
    # def _init_(self):
    #     super(mainthread,self)._init_()

    # def run(self):
    #     self.TaskExecution()
  
  
    # def takecommand():
    #     r=sr.Recognizer()
    #     with sr.Microphone() as source:
    #         print("listening.......")  
    #         r.pause_threshold=1
    #         audio=r.listen(source)


    #     try:
    #         print("recognising.....")
    #         query=r.recognize_google(audio,language='hi')
    #         # query=transla
    #         # tiont(query)
    #         print(f"user said:{query}\n")
    #         return query
    #     except Exception as e:
    #         speak("sir can you speak again")
    #         # return None 
    #         rj = takecommand()
    #         return rj
        
        
        

    # return query

    
        
        

    # return query









   
def take():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print('tell...')
        r.pause_threshold=1
        audio=r.listen(source)
    
    try:
        print("recognising.....")
        red=r.recognize_google(audio,language='en-in')
        print(f"user said:{red}\n")
        return red

    except Exception as e:
        speak(" sorry sir  can you please say that again")
        r= take()
        return r
        
    




if __name__=="__main__":
    
    wishme()
    while True:
        query = takecommand()
        pi=translationt(query).lower()
        print(pi)
        
        
        
        
        if 'wikipedia' in pi:
            speak('searching..')
            # query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("acoording to wikipedia")
            print(results)
            speak(results)
            time.sleep(2)
        
        elif 'youtube' in pi or 'open youtube' in pi or 'utub' in pi:
            speak("this is what i found")  
            pi=pi.replace("youtube","")
            pi=pi.replace("utub","")
            pi=pi.replace('open',"")
            pi=pi.replace('and',"")
            web="https://www.youtube.com/results?search_query="+ pi
            webbrowser.open(web)
            pywhatkit.playonyt(pi)
            time.sleep(2)
            pyautogui.press('enter')
            time.sleep(4)
             
            # webbrowser.open("youtube.com")   
            
            
        elif 'google' in pi or 'open google' in pi:
        
         import wikipedia as googlescrap
         pi=pi.replace("jarvis","")
         pi=pi.replace("google search","")
         speak("this is what i found on google")
        
        
         try:
             pywhatkit.search(pi)
             result=googlescrap.summary(pi,1)
             speak(result)
             
         except:
             speak('no speakable ouput available')
            
         time.sleep(2) 
        #    webbrowser.open('google.com')    
        
        elif 'thank' in pi:
            speak('welcome have a nice day')
            exit()
       
        elif 'song' in pi or "music" in pi:
            # playsound("C:\\Users\\dell\\OneDrive\\Desktop\\music\\83 - Labon Ko (Bhool Bhulaiyaa) - K.K.-(Mr-Jat.in).mp3")
            # input("press enter to stop")
            # continue
    
            music_1="C:\\Users\\dell\\Music\\Playlists"
            songs= os.listdir(music_1)
            print(songs)
            os.startfile(os.path.join(music_1,songs[2]))
            time.sleep(2)
            
        elif 'introduce'  in pi or "hello rani introduce about yourself" in pi or "hi rani introduce about yourself" in pi or 'yourself' in pi or 'yorself' in pi:
            speak("hi everyone my name is rani i am an artifical intelligence program discovered by ritik joshi,divyanshu bisht ,sanidhya singh bhandari")
            speak('how are you sir')      
            
            
            
            
            
            
        elif 'how are you' in pi or 'hi' in pi or "hello" in pi:
            speak("hi sir how are you and  how can i help you")
     
        elif 'open photo' in pi or 'open images' in pi:
            path="D:\\Photos\\8344.jpg"
            os.startfile(path)
     
        elif "instagram" in pi:
            speak('opening sir ')
            webbrowser.open("instagram.com")

        elif "i am fine"  in pi or 'fine' in pi:
            speak("what help can i do for you sir")
         
    
        elif "open" in pi:
            speak("opening sir")
            # dictapp={"command prompt":"cmd","powerpoint":"powerpnt","word":"winword","excel":"excel","chrome":"chrome","vscode":"vscode","notepad":"Notepad"}
            if ".com" in pi or".co.in" in pi:
                pi=pi.replace("open","")
                pi=pi.replace('rani',"")
                webbrowser.open(f'https://www.{pi}')
            
            else:
               pi=pi.replace("open","")
               pyautogui.press("super")
               pyautogui.typewrite(pi)
               pyautogui.press('enter')
               
            time.sleep(2) 
    
        elif "close" in pi:
            speak("closing sir")
            if "stop it too" in pi or '1 tab' in pi or 'close 1 tab' in pi or 'close the tab' in pi :
                pyautogui.hotkey("ctrl","w")
                speak("all tabs closed")
            elif "close  all  the tabs" in pi or 'two tab' in pi or 'stop all then' in pi or 'all the tabs' in pi :
                pyautogui.hotkey("ctrl","w")
                time.sleep(0.5)
                pyautogui.hotkey("ctrl","w")
                speak("all tabs closed") 
   
            elif "3 tab" in pi or 'three tab' in pi:
                pyautogui.hotkey("ctrl","w")
                time.sleep(0.5)
                pyautogui.hotkey("ctrl","w")
                time.sleep(0.5) 
                
                pyautogui.hotkey("ctrl","w")
                time.sleep(0.5)
                speak("all tabs closed")
            
            elif "app" in pi or 'close the app' in pi :
                pyautogui.hotkey("alt","f4")
            
            
            
              
            else:
                pyautogui.hotkey("ctrl","w")    
                
                
        elif 'message'  in pi or 'whatsapp' in pi or 'send' in pi:
            li={"sanu":"+917302207730","abhishek bro":"+918630264853","harshit":"+918439927997","ayushman":"+918476883881","akshat":"+917819883858","bishal":"+917351601920","divyanshu":"+918218752399","sir":"=917477764777","khushi":"+919634744949","mummy":"+917310841093"}
            speak("whom you want to send message")
            name =take().lower()
            speak('what message what you want to send')
            message=take()
            # print(li['name'])
            pywhatkit.sendwhatmsg_instantly(li[name],message)
            time.sleep(10)
            
         
         
         
        elif 'wait a minute' in pi or 'wait' in pi or "hold" in pi or "wet" in pi or 'minit' in pi:
            speak('holding sir')
            time.sleep(1)
         
        # elif 'introduce'  in pi or "hello rani introduce about yourself" in pi or "hi rani introduce about yourself" in pi or 'yourself' in pi or 'yorself' in pi:
        #     speak("hi everyone my name is rani i am an artifical intelligence program discovered by ritik joshi,divyanshu bisht ,sanidhya singh bhandari")
        #     speak('how are you sir')  
            
        else:
           speak("your voice is not recognisble ")          