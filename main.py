import pyttsx3
import speech_recognition as sr
import webbrowser
import wikipedia
import pywhatkit
import time
from urllib.parse import quote
import os
import pyautogui
import datetime
#from playsound import playsound
import keyboard
import pyjokes

import sys
import requests 
from bs4 import BeautifulSoup
import subprocess
import wolframalpha
import pyttsx3
import tkinter
import json
import random
import operator
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import winshell
import feedparser
import smtplib
import ctypes
import time
import requests
import shutil
#import twilio
#from twilio.rest import Client
#from clint.textui import progress
#from ecapture import ecapture as ec
from bs4 import BeautifulSoup
import win32com.client as wincl
from urllib.request import urlopen


Assistant = pyttsx3.init('sapi5')
voices = Assistant.getProperty('voices')
print(voices)
Assistant.setProperty('voices', voices[1].id)
Assistant.setProperty('rate', 150)


def speak(audio):
    print("    ")
    Assistant.say(audio)
    print(f":(audio)")
    print("   ")
    Assistant.runAndWait()

def takecommand():
    command = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        command.pause_threshold = 1
        command.energy_threshold = 350
        audio = command.listen(source)
    try:
        print("Recognizing....")
        query = command.recognize_google(audio, language='en-in')
        print(f"you said : {query}")

    except Exception as Error:
        return "none"

    return query.lower()


def wishme():
    import datetime
    hour = int(datetime.datetime.now().hour)
    
    if hour >= 0 and hour < 12:
        speak("Good Morning sir,")

    elif hour >= 12 and hour < 15:
        speak("Good afternoon sir")
    elif hour >= 15 and hour < 18:
        speak("Good evening sir")
    else:
        speak("Good night sir")
    speak(" how can i help you")       


def taskexe():
    
    def Music():
        speak("Tell me the name of song")
        musicname = takecommand()
        print(musicname)

        if 'happy' in musicname:
            os.startfile(r"D:\Hackathon\Nadaaniyan Akshath 320 Kbps.mp3")

        
        elif 'change' in musicname:
            os.startfile(r"D:\Hackathon\Tharam-Padippicha-Koodaram.mp3")

        else:
            pywhatkit.playonyt(musicname)
        
        speak("your song has been started")
    
    def Time():
        import time
        from re import I, M, S
        tt = time.strftime("%I:%M %p")
        speak(tt)

    def sendwhatmessage(wait_time: int = 20, tab_close: bool = False, close_time: int = 3) -> None:
        import pyautogui as pg
        import time
        
        speak("please tell me the persons name")
        name_ = takecommand()

        if 'abc' in name_:
            phone_no = '0123456789'
        elif 'def' in name_:
            phone_no = '1234567890'
        elif 'hij' in name_:
            phone_no = '2345678901'
        else:
            phone_no = input("Enter the phone number:")
        

        speak("Tell me the message")
        message = takecommand()

        parsed_message = quote(message)
        webbrowser.open('https://web.whatsapp.com/send?phone=' +
                phone_no + '&text=' + parsed_message)
        time.sleep(2)
        width, height = pg.size()
        pg.click(width / 2, height / 2)
        time.sleep(wait_time - 2)
        pg.press('enter')

        speak("done")

    def OpenApps():
        speak("Ok , Wait a second")
        
        # if 'notion' in query:
        #     os.startfile('C:\\Users\\shemi\\AppData\\Local\\Programs\\Notion\\Notion.exe')
        # elif 'zoom' in query:
        #     os.startfile('C:\\Users\\shemi\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe')
        # el
        if 'youtube' in query:
            webbrowser.open('https://www.youtube.com/')
        elif 'whatsapp' in query:
            webbrowser.open('https://web.whatsapp.com/')
        elif 'chrome' in query:
            os.startfile('"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"')
        # elif 'brave' in query:
        #     os.startfile('C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe')
        elif 'command prompt' in query:
            os.system("start cmd")
        
        speak("opening")

    def CloseApps():
        speak("ok sir,wait a second")
        #if 'notion' in query:
            #os.system("TASKKILL /F /im Notion.exe")
        #elif 'zoom' in query:
           # os.system("TASKKILL /F /im Zoom.exe")
        if 'youtube' in query:
            os.system("TASKKILL /F /im msedge.exe")
           # keyboard.press_and_release("ctrl+w")
        elif 'whatsapp' in query:
            os.system("TASKKILL /F /im msedge.exe")
        elif 'chrome' in query:
            os.system("TASKKILL /F /im chrome.exe")
        #elif 'brave' in query:
           # os.system("TASKKILL /F /im brave.exe")
        elif 'command prompt' in query:
            os.system("TASKKILL /F /im cmd.exe")
            
        speak("closing")

    def youtubeauto():
        speak("What is your command")
        comm = takecommand()

        if 'pause' in comm:
            keyboard.press('space bar')

        elif 'restart' in comm:
            keyboard.press('0')

        elif 'mute' in comm:
            keyboard.press('m')

        elif 'skip' in comm:
            keyboard.press('1')

        elif 'back' in comm:
            keyboard.press('j')

        elif 'full screen' in comm:
            keyboard.press('f')
        
        elif 'film mode' in comm:
            keyboard.press('t')
        
        elif 'next video' in comm:
            keyboard.press('shift + N')

        elif 'previous video' in comm:
            keyboard.press('shift + P')

        speak("done sir")

    def chromeauto():
        speak("Chrome automation started")

        command = takecommand()

        if 'close this tab' in command:
            keyboard.press_and_release('ctrl + w')

        elif 'open new tab' in command:
            keyboard.press_and_release('ctrl + t')

        elif 'open new window' in command:
            keyboard.press_and_release('ctrl + n')

        elif 'history' in command:
            keyboard.press_and_release('ctrl + h')

    def screenshot():
        speak("Ok sir, What should i name the file ?")
        namei = takecommand()
        imga = pyautogui.screenshot()
        imga.save(f"{namei}.png")
        speak("screen captured")
    def tell_date():
         today = datetime.date.today().strftime("%B %d, %Y")
         print(f"Today's date is {today}")
         speak(f"Today's date is {today}")







#query section begins

    while True:
        query = takecommand()

        #conversation begin
  
        if 'hello' in query:
            speak("Hello sir,")  
            
        elif 'how are you' in query:
            speak(random.choice(["iam fine", "i am good "," doing great","i am fine sir , what about you"]))

        elif 'who are you' in query:
            speak("i am Evo, your virtual assistant")

        elif 'how old are you' in query:
            speak(random.choice(["i don't know . you tell me!","Next question, please!","I had no idea that it changes every year. How do you manage to keep track?","I remember having a pet dinosaur.","That question is my least favorite.","Not as old as you!","I’m a day older than I was yesterday.","Age is just a number. Numbers are infinite, and so are the possible answers to this question."]))

        elif 'can you prove that you are self aware' in query:
            speak("Its really tough question ,are you self aware, can you prove that!")

        elif 'what is artificial intelligence' in query:
            speak("Artificial intelligence is intelligence demonstrated by machines, as opposed to the natural intelligence displayed by animals including humans")

        elif 'what is machine learning' in query:
            speak("Machine learning is a field of inquiry devoted to understanding and building methods that 'learn', that is, methods that leverage data to improve performance on some set of tasks. It is seen as a part of artificial intelligence")

        elif 'why i cannot see you' in query:
            speak("because, i dont have any physical body, i am virtual")

        elif 'where are you' in query:
            speak("i am here ,but you can't see me ")

        elif 'who created you' in query or 'who made you' in query:
            speak("iam created by team Error_404,")  
            
        elif 'repeat the answer' in query or 'repeat that' in query:
            speak("could you please repeat the question")

        elif 'what is' in query or 'what are' in query or 'who is' in query or 'who was' in query:
            query = query.replace("Evo", "")
            query = query.replace("wikipedia", "")
            wiki = wikipedia.summary(query, 2)
            speak(f":{wiki}")

        elif "where is" in query :
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.nl / maps / place/" + location + "")
 
        elif "who i am" in query:
            speak("If you talk then definitely your human.")

        elif 'your opinion about love' in query:
            speak(random.choice(["It is 7th sense that destroy all other senses","It’s temporary madness.","Love is like a webpage error. It says 404 not found!","Neurologically, it’s something similar to addictive drugs.","It’s a chemical reaction in the brain that turns people into idiots","It’s your brain overflowing with serotonin.","It’s a symptom of life."]))

        elif "don't listen" in query or "stop listening" in query:
            speak("okay. paused listening for a minute")
            import time
            #speak("for how much time you want to stop tom from listening commands")
            #a = int(takecommand())
            print("paused for one minute")
            time.sleep(60)
            

        elif "Evo" in query:
             
            wishme()
            speak("Evo 1 point o in your service Mister")
            speak("Evo")
 
        elif "i love you" in query:
            speak("It's hard to understand")

        elif "will you be my gf" in query or "will you be my bf" in query:  
            speak("I'm not sure about, may be you should give me some time")
         
        #elif "what is" in query or "who is" in query:
             
            # Use the same API key
            # that we have generated earlier
            #client = wolframalpha.Client("API_ID")
            #res = client.query(query)
             
            #try:
                #print (next(res.results).text)
                #speak (next(res.results).text)
           # except StopIteration:
                #print ("No results")
 
        # elif "" in query:
            # Command go here
            # For adding more commands   
            
            
            

        #conversation end


        elif "log off" in query or "sign out" in query:
            speak("Make sure all the application are closed before sign-out")
            time.sleep(5)
            subprocess.call(["shutdown", "/l"])
 
    
        # elif 'open stackoverflow' in query:
        #     speak("Here you go to Stack Over flow.Happy coding")
        #     webbrowser.open("stackoverflow.com") 
        
        elif 'change background' in query or 'change wallpaper' in query:
            wallpapers = random.choice([r"D:\Hackathon\download.jpeg",r"D:\Hackathon\images (1).jpeg",r"D:\Hackathon\images (2).jpeg",r"D:\Hackathon\images (3).jpeg",r"D:\Hackathon\images.jpeg"])
            ctypes.windll.user32.SystemParametersInfoW(20,
                                                       0,
                                                       wallpapers,
                                                       0)
            speak("Background changed successfully")

        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
            speak("Recycle Bin Recycled")

        elif "write a note" in query:
            speak("What should i write, sir")
            note = takecommand()
            file = open('jarvis.txt', 'w')
            speak("Sir, Should i include date and time")
            snfm = takecommand()
            if 'yes' in snfm or 'sure' in snfm:
                print(snfm)
                strTime = datetime.datetime.now().strftime("% H:% M:% S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)

        elif "show note" in query:
            speak("Showing Notes")
            file = open("jarvis.txt", "r")
            print(file.read())
            speak(file.read())

        elif 'news' in query:
             
            try:
                jsonObj = urlopen('''https://newsapi.org / v1 / articles?source = the-times-of-india&sortBy = top&apiKey =\\times of India Api key\\''')
                data = json.load(jsonObj)
                i = 1
                 
                speak('here are some top news from the times of india')
                print('''=============== TIMES OF INDIA ============'''+ '\n')
                 
                for item in data['articles']:
                     
                    print(str(i) + '. ' + item['title'] + '\n')
                    print(item['description'] + '\n')
                    speak(str(i) + '. ' + item['title'] + '\n')
                    i += 1
            except Exception as e:
                 
                print(str(e))

        elif 'lock screen' in query or 'lock window'in query or 'lock the screen' in query:
                speak("locking the device")
                ctypes.windll.user32.LockWorkStation()

        elif 'youtube search' in query:
            speak("ok sir, this is what i found on youtube")
            query = query.replace("jarvis", "")
            query = query.replace("youtube search", "")
            web = 'https://www.youtube.com/results?search_query=' + query
            webbrowser.open(web)
            speak("done sir")
        
        elif 'ip address' in query:
            from requests import get
            ip = get('https://api.ipify.org/').text
            print(ip)
            speak(f"your ip address is {ip}")

        elif 'google search' in query or 'hey google' in query:
            speak("ok sir, this is what i found on google")
            query = query.replace("tom", "")
            query = query.replace("google search", "")
            pywhatkit.search(query)
            speak("done sir")
            
        
        # elif "calculate" in query:
             
        #     app_id = "Wolframalpha api id"
        #     client = wolframalpha.Client(app_id)
        #     indx = query.lower().split().index('calculate')
        #     query = query.split()[indx + 1:]
        #     res = client.query(' '.join(query))
        #     answer = next(res.results).text
        #     print("The answer is " + answer)
        #     speak("The answer is " + answer)

        elif 'website' in query:
            speak("ok sir, launching....")
            query = query.replace("Evo", "")
            query = query.replace("website", "")
            query = query.replace(" ", "")
            web1 = query.replace("open ", "")
            web2 = 'https://www.' + web1 + '.com'
            webbrowser.open(web2)
            speak("launched")

        elif 'launch' in query:
            speak("tell me the name of website")
            name = takecommand()
            web = 'https://www.' + name + '.com'
            webbrowser.open(web)
            speak("done sir")

        elif 'open email' in query:
            speak("ok sir")
            webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
            speak("done sir")

        elif 'music' in query:
            Music()

        elif 'wikipedia' in query:
            speak("Searching wikipedia")
            query = query.replace("tom", "")
            query = query.replace("wikipedia", "")
            wiki = wikipedia.summary(query, 2)
            speak(f"According to wikipedia :{wiki}")

        elif 'whatsapp message' in query:
            sendwhatmessage()

        elif 'screenshot' in query:
            screenshot()

        #elif hour >= 12 and hour < 15:
        #speak("Good afternoon sir")

        #elif 'open zoom' in query:
           # OpenApps()
        
        elif 'open youtube' in query:
            OpenApps()

        elif 'open whatsapp' in query:
            OpenApps()

        elif 'open chrome' in query:
            OpenApps()

        elif 'open browser' in query:
            OpenApps()
            
        elif 'open command prompt' in query:
            OpenApps()

       # elif 'close notion' in query:
           # CloseApps()

        #elif 'close zoom' in query:
         #   CloseApps()

        elif 'close youtube' in query:
            CloseApps()

        elif 'close whatsapp' in query:
            CloseApps()

        elif 'close chrome' in query:
            CloseApps()
            
        elif 'close browser' in query:
            CloseApps()

        elif 'close vs code' in query:
            CloseApps()

        elif 'pause' in query:
            keyboard.press('space bar')

        elif 'play' in query:
            keyboard.press('space bar')

        elif 'restart' in query:
            keyboard.press('0')

        elif 'mute' in query:
            keyboard.press('m')

        elif 'skip' in query:
            keyboard.press('1')

        elif 'back' in query:
            keyboard.press('j')

        elif 'full screen' in query:
            keyboard.press('f')
        
        elif 'film mode' in query:
            keyboard.press('t')

        elif 'next video' in query:
            keyboard.press('shift + N')

        elif 'previous video' in query:
            keyboard.press('shift + P')

        elif 'youtubetool' in query:
            youtubeauto()

        elif 'close this tab' in query:
            keyboard.press_and_release('ctrl + w')

        elif 'open new tab' in query:
            keyboard.press_and_release('ctrl + t')

        elif 'open new window' in query:
            keyboard.press_and_release('ctrl + n')

        elif 'history' in query:
            keyboard.press_and_release('ctrl + h')

        elif 'chrome automation' in query:
            chromeauto()

        elif 'joke' in query:
            get = pyjokes.get_joke()
            speak(get)
        
        elif 'repeat my words' in query:
            speak("speak sir")
            jj = takecommand()
            speak(f"you said:{jj}")
        
        elif 'my location' in query:
            speak("ok sir, wait a second, let me check")
            try:
                from requests import get
                ip = get('https://api.ipify.org/').text
                print(ip)
                url = 'https://get.geojs.io/v1/ip/' + ip + '.json'
                geo_requests = requests.get(url)
                geo_data = geo_requests.json()
                city = geo_data['city']
                country = geo_data['country']
                speak(f"sir iam not sure , but i think we are in {city} city of {country} country")
            except Exception as e:
                speak("sorry sir, Due to network issue iam not able to find where we are.")
                pass

        elif "camera" in query or "take a photo" in query:
            ec.capture(0, "Jarvis Camera ", "img.jpg")
        
        elif 'alarm' in query:
            speak("enter the time")
            time = input(":enter the time:")

            while True:
                Time_Ac = datetime.datetime.now()
                now = Time_Ac.strftime("%H:%M")

                if now == time:
                    speak("time to wake up sir")
                    os.startfile(r"D:\Hackathon\germany-eas-alarm-1945-242750.mp3")

                elif now > time:
                    os.system("TASKKILL /F /im germany-eas-alarm-1945-242750.mp3 ")
                    speak("Alarm closed")
                    break

        elif 'take a break' in query or 'exit' in query:
            speak("ok sir, you can call me any time.")
            sys.exit()

        elif 'shutdown' in query or 'shut down' in query:
            speak("Do you really want to shutdown the system sir?")
            ch = takecommand()
            if "shutdown" or "yes" in ch:

                os.system("shutdown /s /t 1")
            else:
                speak("ok sir")

        elif "restart" in query:
            subprocess.call(["shutdown", "/r"])

        elif 'time' in query:
            Time()
        elif "date" in query:
            tell_date()




wishme()
taskexe()