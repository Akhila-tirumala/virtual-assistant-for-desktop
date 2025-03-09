import pyttsx3
import speech_recognition 
import requests
from bs4 import BeautifulSoup
import datetime
import os
import pyautogui
import random
from plyer import notification
from pygame import mixer
import speedtest
import webbrowser

#paste this just below the password function
for i in range(3):
    a = input("Enter Password to open Virtual Assistant :- ")
    pw_file = open("password.txt","r")
    pw = pw_file.read()
    pw_file.close()
    if (a==pw):
        print("WELCOME SIR ! PLZ SPEAK [WAKE UP] TO LOAD ME UP")
        break
    elif (i==2 and a!=pw):
        exit()

    elif (a!=pw):
        print("Try Again")

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def alarm(query):
    timehere = open("Alarmtext.txt","a")
    timehere.write(query)
    timehere.close()
    os.startfile("alarm.py")

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)

    try:
        print("Understanding..")
        query  = r.recognize_google(audio,language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query
if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if "wake up" in query:
            from GreetMe import greetMe
            greetMe()

            while True:
                query = takeCommand().lower()
                if "go to sleep" in query:
                    speak("Ok sir , You can me call anytime")
                    break
                elif "hello" in query:
                    speak("Hello sir, how are you ?")
                elif "i am fine" in query:
                    speak("that's great, sir")
                elif "how are you" in query:
                    speak("Perfect, sir")
                elif "thank you" in query:
                    speak("you are welcome, sir") 
                elif "play a game" in query:
                    from game import game_play
                    game_play()
                elif "google" in query:
                    from SearchNow import searchGoogle
                    searchGoogle(query)
                elif "youtube" in query:
                    from SearchNow import searchYoutube
                    searchYoutube(query)
                elif "wikipedia" in query:
                    from SearchNow import searchWikipedia
                    searchWikipedia(query)
                elif "temperature" in query:
                    search = "temperature in East Godavari"
                    url = f"https://www.google.com/search?q={search}"
                    r  = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"current{search} is {temp}")
                elif "weather" in query:
                    search = "temperature in East godavari"
                    url = f"https://www.google.com/search?q={search}"
                    r  = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"current{search} is {temp}")
                elif "the time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")    
                    speak(f"Sir, the time is {strTime}")
                elif "you can sleep" in query:
                    speak("Going to sleep,sir")
                    exit()
                elif "focus mode" in query:
                    a = int(input("Are you sure that you want to enter focus mode :- [1 for YES / 2 for NO] "))
                    if (a==1):
                        speak("Entering the focus mode....")
                        os.startfile("C:\\Users\\PRASAD\\Desktop\\MYCODE\\FocusMode.py")
                        exit()
                    else:
                        pass
                elif "show my focus" in query:
                    from FocusGraph import focus_graph
                    focus_graph()
                elif "open" in query:
                    from Dictapp import openappweb
                    openappweb(query)
                elif "close" in query:
                    from Dictapp import closeappweb
                    closeappweb(query)
                elif "set an alarm" in query:
                    print("input time example:- 10 and 10 and 10")
                    speak("Set the time")
                    a = input("Please tell the time :- ")
                    alarm(a)
                    speak("Done,sir")
                elif "pause" in query:
                    pyautogui.press("k")
                    speak("video paused")
                elif "play" in query:
                    pyautogui.press("k")
                    speak("video played")
                elif "mute" in query:
                    pyautogui.press("m")
                    speak("video muted")
                elif "volume up" in query:
                    from keyboard import volumeup
                    speak("Turning volume up,sir")
                    volumeup()
                elif "volume down" in query:
                    from keyboard import volumedown
                    speak("Turning volume down, sir")
                    volumedown()
                elif "remember that" in query:
                   rememberMessage = query.replace("remember that","")
                   rememberMessage = query.replace("assistant","")
                   speak("You told me to remember that"+rememberMessage)
                   remember = open("Remember.txt","a")
                   remember.write(rememberMessage)
                   remember.close()
                elif "what do you remember" in query:
                   remember = open("Remember.txt","r")
                   speak("You told me " + remember.read())
                elif "tired" in query:
                    speak("Playing your favourite songs, sir")
                    a = (1,2,3) # You can choose any number of songs (I have only choosen 3)
                    b = random.choice(a)
                    if b==1:
                        webbrowser.open("https://www.youtube.com/watch?v=ieFdE7QvP-s")
                    if b==2:
                        webbrowser.open("https://www.youtube.com/watch?v=mR0KhrITCso")
                    if b==3:
                        webbrowser.open("https://www.youtube.com/watch?v=nGeHstBtoH0")
                    
                elif "news" in query: 
                    from NewsRead import latestnews
                    latestnews()
                elif "calculate" in query:
                    from Calculatenumbers import WolfRamAlpha
                    from Calculatenumbers import Calc
                    query = query.replace("calculate","")
                    query = query.replace("assistant","")
                    Calc(query)
                elif "whatsapp" in query:
                    from Whatsapp import sendMessage
                    sendMessage()
                elif "translate" in query: 
                    from Translator import translategl
                    query = query.replace("assistant","")
                    query = query.replace("translate","")
                    translategl(query)
                elif "schedule my day" in query:
                    tasks = [] #Empty list 
                    speak("Do you want to clear old tasks (Plz speak YES or NO)")
                    query = takeCommand().lower()
                    if "yes" in query:
                       file = open("tasks.txt","w")
                       file.write(f"")
                       file.close()
                       no_tasks = int(input("Enter the no. of tasks :- "))
                       i = 0
                       for i in range(no_tasks):
                           tasks.append(input("Enter the task :- "))
                           file = open("tasks.txt","a")
                           file.write(f"{i}. {tasks[i]}\n")
                           file.close()
                    elif "no" in query:
                          i = 0
                          no_tasks = int(input("Enter the no. of tasks :- "))
                          for i in range(no_tasks):
                              tasks.append(input("Enter the task :- "))
                              file = open("tasks.txt","a")
                              file.write(f"{i}. {tasks[i]}\n")
                              file.close()
                elif "show my schedule" in query:        
                     file = open("tasks.txt","r")
                     content = file.read()
                     file.close()
                     mixer.init()
                     mixer.music.load("notification.mp3")
                     mixer.music.play()
                     notification.notify(
                     title = "My schedule :-",
                     message = content,
                    timeout = 15
                     )
                elif "open" in query:   #EASY METHOD
                    query = query.replace("open","")
                    query = query.replace("assistant","")
                    pyautogui.press("super")
                    pyautogui.typewrite(query)
                    pyautogui.sleep(2)
                    pyautogui.press("enter")
                elif "internet speed" in query:
                    wifi  = speedtest. Speedtest()
                    upload_net = wifi.upload()/1048576         #Megabyte = 1024*1024 Bytes
                    download_net = wifi.download()/1048576
                    print("Wifi Upload Speed is", upload_net)
                    print("Wifi download speed is ",download_net)
                    speak(f"Wifi download speed is {download_net}")
                    speak(f"Wifi Upload speed is {upload_net}")

                elif "screenshot" in query:
                     import pyautogui #pip install pyautogui
                     im = pyautogui.screenshot()
                     im.save("ss.jpg")
                elif "click my photo" in query:
                    pyautogui.press("super")
                    pyautogui.typewrite("camera")
                    pyautogui.press("enter")
                    pyautogui.sleep(2)
                    speak("SMILE")
                    pyautogui.press("enter")
