from __future__ import with_statement
from tkinter import W
import pyttsx3
import requests_toolbelt
import speech_recognition as sr
import datetime
import webbrowser
import os
import random
import pywhatkit as kit
import sys
import pyautogui
import time
import operator
import requests
import subprocess
from winreg import QueryValue
import wikipedia



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 150)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir!")
    elif hour >= 12 and hour < 0:
        speak("Good Afternoon Sir!")
    else:
        speak("Good Evening")

    speak("Ready sir, What can i do for you?")


def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-id')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say again please...")
        return "none"
    return query


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            print(result)
            speak(result)

        elif "channel analystic" in query:
            webbrowser.open("https://youtube.com")

        elif 'search on youtube' in query:
            query = query.replace("search on youtube", "")
            webbrowser.open(f"www.youtube.com/result?search_query={query}")

        elif 'open youtube' in query:
            speak("what u want to like to watch?")
            qrry = takeCommand().lower()
            kit.playonyt(f"{qrry}")

        elif 'close chrome' in query:
            os.system("taskkill /f /im chrome.exe")

        elif 'close youtube' in query:
            os.system("taskkill /f /im msedge.exe")

        elif 'open google' in query:
            speak("what should I search ?")
            qry = takeCommand().lower()
            webbrowser.open(f"{qry}")
            results = wikipedia.summary(qry, sentences=2)
            speak(results)

        elif 'close google' in query:
            os.system("taskkill /f /im msedge.exe")

        elif 'play music' in query:
            music_dir = 'E:\Musics'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, random.choice(songs)))

        elif 'play iron man movie' in query:
            npath = "home\marks\ironman.mkv"

        elif 'close movie' in query:
            os.system("taskkill /f /im vlc.exe")

        elif 'close music' in query:
            os.system("taskkill /f /im vlc.exe")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif "shut down the system" in query:
            os.system("shutdown /s /t 5")

        elif "restart the system" in query:
            os.system("shutdown /r /t 5")

        elif "Lock the system" in query:
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

        elif "open leafpad" in query:
            npath = "C:\WINDOWS\system32\\notepad.exe"
            os.startfile(npath)

        elif "close notepad" in query:
            os.system("taskkill /f /im notepad.exe")

        elif "open command prompt" in query:
            os.system("start cmd")

        elif "close command prompt" in query:
            os.system("taskkill /f /im cmd.exe")

        elif "go to sleep" in query:
            speak(' alright then, I am switching off')
            sys.exit()

        elif "take screenshot" in query:
            speak('tell me a name for the file')
            name = takeCommand().lower()
            time.sleep(3)
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("screenshot saved")

        elif "calculate" in query:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                speak("ready")
                print("Listening...")
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)

            my_string = r.Recognizer_google(audio)
            print(my_string)

            def get_operator_fn(op):
                return {
                    '+': operator.add,
                    '-': operator.sub,
                    'x': operator.mul,
                    'divided': operator.__truedly__,

                }[op]

            def eval_bianary_expr(op1, oper, op2):
                op1, op2 = int(op1), int(op2)
                return get_operator_fn(oper)(op1, op2)
            speak("your result is")
            speak(eval_bianary_expr(*(my_string.split())))
        
        elif "what is my ip address" in query:
            speak("checking")

            try:
                ipAdd = requests.get('https://api.ipfy.org').text
                print(ipAdd)
                speak("Your ip address is")
                speak(ipAdd)
            
            except Exception as e:
                speak("Network is slow try again later")

        elif "volumeup" in query:
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
        
        elif "volumedown" in query:
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")

        elif "mute" in query:
            pyautogui.press("volumemute")

        elif "refresh" in query:
            pyautogui.moveTo(1551, 551, 2)
            pyautogui.click(x=1551, y=551, clicks=1, interval=0, button='right')
            pyautogui.moveTo(1620, 667, 1)
            pyautogui.click(x=1620, y=667, clicks=1, interval=0, button='left')
        
        elif "scroll down" in query:
            pyautogui.scroll(1000)

        elif "drag visual studio to the right" in query:
            pyautogui.moveTo(46, 31, 2)
            pyautogui.dragRel(1857, 31, 2)

        elif "rectangular spiral" in query:
            pyautogui.hotkey('win')
            time.sleep(1)
            pyautogui.write('paint')
            time.sleep(1)
            pyautogui.press('enter')
            pyautogui.moveTo(100, 193, 1)
            pyautogui.rightClick
            pyautogui.click()
            distance = 300
            while distance > 0:
                pyautogui.dragRel(distance, 0, 0.1, button="left")
                distance = distance - 10
                pyautogui.dragRel(0, distance, 0.1, button="left")
                pyautogui.dragRel(-distance, 0, 0.1, button="left")
                distance = distance - 10
                pyautogui.dragRel(0, -distance, 0.1, button="left")

        elif "close paint" in query:
            os.system("taskkill /f /im mspaint.exe")
            
        elif "who are you?" in query:
            print('Im Friday your virtual assistant')
            speak('Im Friday your virtual assistant')
            print('I can Do Everything that my creator programmed me to do')
            speak('I can Do Everything that my creator programmed me to do')

        elif "who create you?" in query:
            print('I created by you sir, I creataed with python language')
            speak('I created by you sir, I creataed with python language')

        elif "open fl studio" in query:
            pyautogui.hotkey('win')
            time.sleep(1)
            pyautogui.write('fl studio')
            time.sleep(1)
            pyautogui.press('enter')
            time.sleep(1)

        elif "subscribe" in query:
            print("please follow kaimarks_project on Instagram")
            speak("please follow kaimarks_project on Instagram")

        elif 'type' in query: #10
            query = query.replace("type", "")
            pyautogui.write(f"{query}")


"""

CHROME AUTOMATION

"""

import pyttsx3
import speech_recognition as sr
import pyautogui
import time
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 150)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing")
        query = r.recognize_google(audio, language='en')
        print(f"user said: {query}\n")


    except Exception as e:
        print("say that again plesae...")
        return "None"
    return query

if __name__=="__main__":
    while True:
        query = takeCommand().lower()

        if 'open chrome' in query:
            os.startfile('~/.local/share/applications/chrome-nlalbmkafgmoifbeooblidblkmlhhpnc-Default.desktop')

        elif 'maximize the window' in query:
            pyautogui.press('alt', 'space')
            time.sleep(1)
            pyautogui.press('x')

        elif 'google search' in query:
            query = query.replace("google search", "")
            pyautogui.hotkey('alt', 'd')
            pyautogui.write(f"{query}", 0.1)
            pyautogui.press('enter')

        elif 'youtube search' in query:
            query = query.replace("youtube search", "")
            pyautogui.hotkey('alt', 'd')
            time.sleep(1)
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.press('tab')
            time.sleep(1)
            pyautogui.write(f"{query}", 0.1)
            pyautogui.press('enter')

        elif 'open new window' in query:
            pyautogui.hotkey('ctrl', 'n')

        elif 'open incognito window' in query:
            pyautogui.hotkey('ctrl', 'shift', 'n')

        elif 'minimise this window' in query:
            pyautogui.hotkey('alt', 'space')
            time.sleep(1)
            pyautogui.press('n')

        elif 'open history' in query:
            pyautogui.hotkey('ctrl', 'h')


"""

Image Recognize

"""

import pyttsx3
import speech_recognition as sr
import pyautogui
import time
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 150)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-id')
        print(f"User said: {query}\n")
    
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

if __name__ == "__main__":
    while True:
        query = takeCommand().lower()

        if 'open chrome' in query:
            img = pyautogui.locateCenterOnScreen('Screenshot1.png') #[take a screenshot of chrome and crop it, then save the image in friday folder]
            pyautogui.doubleClick(img)
            time.sleep(1)
            pyautogui.hotkey('alt', 'space')
            time.sleep(1)
            pyautogui.press('x')
            time.sleep(1)

            img1 = pyautogui.locateCenterOnScreen('screenshot2.png')
            time.sleep(2)

        elif 'close chrome' in query:
            os.system("taskkill /f /im chrome.exe")

        
### SUDAH SELESAII !! 