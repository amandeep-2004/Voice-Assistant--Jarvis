

import out as out
import pyttsx3
import speech_recognition as sr
import datetime
import os
import wikipedia
import webbrowser
import random
import requests
from requests import get
import pyjokes
from pyautogui import pyscreeze
import pywhatkit as kit
import pyautogui
import time
from playsound import playsound
import sys
import smtplib
import playsound
import calendar
from pygame import mixer
import pywikihow 
from pywikihow import search_wikihow
import getpass
from bs4 import BeautifulSoup
import imdb
import phonenumbers as ph
from phonenumbers import carrier
import instaloader
import datefinder
import winsound
import wolframalpha
import psutil
import json
import cv2
import smtplib
import sounddevice
import getpass
mixer.init()
client = wolframalpha.Client("48LJKJ-X7L49VVGGY")
import numpy as np
import PyPDF2
from google_trans_new import google_translator  
from datetime import date

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voices', voices[0].id)
engine.setProperty('rate',230)


#text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

#To convert voice into text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=3,phrase_time_limit=5)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")

    except Exception as e:
        speak("say that again please...")
        
        return "none"
    return query

    
def take_mallu():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=5,phrase_time_limit=5)

    try:
        print("Recognizing...")
        speak('sir please enter the code of the language that you want to translate')
        lan=input('enter the code: ')
        query = r.recognize_google(audio, language=f'{lan}-in')
        print(f"user said: {query}")

    except Exception as e:
        speak("say that again please...")
        
        return "none"
    return query

def tran():
    translator = google_translator()  
    line=take_mallu()
    translate_text = translator.translate(line,lang_tgt='en')  
    speak(translate_text)




def news():
    main_url = 'https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=f553424e2d644ce39e742701810e7f49'

    main_page = requests.get(main_url).json()
    # print(main_page)
    articles = main_page["articles"]
    # print(articles)
    head =[]
    day=["first","second","third","fourth","fifth","sixth","seventh","eighth","ninth","tenth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range (len(day)):
        # print(f"today's {day[i]} news is: ", head[i])
        speak(f"today's {day[i]} news is: {head[i]}")






def record():
    fs=44100
    speak('please enter the duration of the recording:')
    second = int(input('enter the length of recording: '))
    print('recording...')
    record_voice=sounddevice.rec(int(second * fs),samplerate=fs, channels=2)
    sounddevice.wait()
    speak('please enter the name of the recording')
    name=input('enter the name of recording: ')
    write(name, fs,record_voice)


def stoplistening():
    speak("for how much second  you want to stop jarvis  from listening commands")
    try:
        a = int(takecommand())
        speak(f"going to sleep for {a} second")
        
        time.sleep(a)
    except Exception as e:
        speak(" I could not understand what did you say could not got to sleep")
        stoplistening()

def secs2hours(secs):
    mm, ss = divmod(secs, 60)
    hh, mm = divmod(mm, 60)
    return "%dhour, %02d minute, %02s seconds" % (hh, mm, ss)

#to wish
def wishMe():
    now = datetime.datetime.now()
    my_date = datetime.datetime.today()
    weekday = calendar.day_name[my_date.weekday()]
    monthNum = now.month
    dayNum = now.day
    month_names = ['January', 'Febraury', 'March', 'April', 'May',  'June', 'July', 'August', 'September', 'October', 'November', 'December']

    ordinalNumbers = ['1st', '2nd', '3rd', '4th', '5th', '6th','7th', '8th', '9th',  '10th', '11th', '12th', '13th', '14th', '15th', '16th', '17th', '18th', '19th','20th', '21st', '22nd', '23rd', '24th', '25th', '26th', '27th', '28th', '29th', '30th', '31st']
    hour = int(datetime.datetime.now().hour)
    strTime = datetime.datetime.now().strftime("%I:%M")
    if hour>=0 and hour<12:
        speak(f'Good morning Amandeep!.Today is {weekday}  {month_names[monthNum - 1]} {ordinalNumbers[dayNum - 1]}. Time is {strTime} am')

    elif hour>=12 and hour<18:
        speak(f'Good afternoon Amandeep!Today is {weekday}  {month_names[monthNum - 1]} {ordinalNumbers[dayNum - 1]}. Time is {strTime} pm')


    elif hour >= 18 and hour<24:
        speak(f'Good evening Amandeep!Today is {weekday}  {month_names[monthNum - 1]} {ordinalNumbers[dayNum - 1]}. Time is {strTime} pm')
    
 
    
    speak("I am Jarvis sir . Please tell me how may I help you")
    

def getDate():
    now = datetime.datetime.now()
    my_date = datetime.datetime.today()
    weekday = calendar.day_name[my_date.weekday()]
    monthNum = now.month
    dayNum = now.day
    month_names = ['January', 'Febraury', 'March', 'April', 'May',  'June', 'July', 'August', 'September', 'October', 'November', 'December']

    ordinalNumbers = ['1st', '2nd', '3rd', '4th', '5th', '6th','7th', '8th', '9th',  '10th', '11th', '12th', '13th', '14th', '15th', '16th', '17th', '18th', '19th','20th', '21st', '22nd', '23rd', '24th', '25th', '26th', '27th', '28th', '29th', '30th', '31st']
    return 'Today is '+weekday+' '+ month_names[monthNum - 1]+' the '+  ordinalNumbers[dayNum - 1]+'. '




def chargeper():
    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    percent = int(battery.percent)
    time_left = secs2hours(battery.secsleft)
    print(f'{percent}% charge')

    if percent<=25 and plugged==False:
        speak('battery low plug in the charger')
        
        time.sleep(1)



def screen_recorder():
    screen_size=(1920,1080)
    fourcc=cv2.VideoWriter_fourcc(*'XVID')
    out=cv2.VideoWriter('output.avi',fourcc,20.0,(screen_size))




def tracker():
    num = input('enter the phone number:')
    ch_num=ph.parse(num,"CH")
    print(geocoder.description_for_number(ch_num,'en'))
    print(carrier.name_for_number(ch_num,'en'))





def temp():
    q="temperature"
    res = client.query(q)
    results = next(res.results).text
    speak(f'temperature outside is {results}')

if __name__ == "__main__":

    wishMe()
    getDate()
    temp()
    chargeper()
    while True:

       query = takecommand().lower()
       
       #logic building for tasks
       if 'take screenshot' in query or 'screenshot' in query:
           speak("sir,tell me the name for this screenshot")
           name = takecommand().lower()
           speak("sir, please hold the screen for a few seconds")
           time.sleep(3)
           img = pyautogui.screenshot()
           img.save(f"{name}.png")
           speak("I am done sir , the screenshot is saved in our main folder")
           speak('sir do you want to see the screenshot just taken')
           m=takecommand().lower()
           if m=='yes':
               img = cv2.imread(f'{name}.png',1)
               cv2.imshow('image',img)
               cv2.waitKey(50000)
               cv2.destroyAllWindows()
           else:
               speak('ok sir')

       if 'wikipedia' in query:
           speak('searching wikipedia...')
           query = query.replace("wikipedia", "")
           results = wikipedia.summary(query, sentences=4)
           speak('according to wikipedia')
           speak(results)

       elif 'tell me about' in query:
           speak('searching wikipedia....')
           query=query.replace('tell me about','')
           results = wikipedia.summary(query, sentences=3)
           speak(results)



       elif 'speak about ' in query:
           query = query.replace('speak about','')
           moviesDB = imdb.IMDb()
           movies = moviesDB.search_movie(query)
           id = movies[0].getID()
           movie = moviesDB.get_movie(id)
           title = movie['title']
           year = movie['year']
           rating = movie['rating']
           directors = movie['directors']
           casting = movie['cast']
           print('Movie info:')
           speak(f'{title} - {year}')
           speak(f'rating: {rating}')
           direcStr = ' '.join(map(str,directors))
           speak(f'directors: {direcStr}')
           actors = ', '.join(map(str, casting))
           speak(f'actors are: {actors}')  



       elif 'make a google search' in query:
           speak("sir, what should I search on google?")
           cm = takecommand().lower()
           webbrowser.open(f"{cm}")
           speak('here you go')

       elif 'what\'s your age' in query:
           f=(calculateAge(date(2020,9,21)))
           speak(f'{f} years old')




       elif 'instagram profile' in query or "profile on instagram" in query:
           speak("sir please enter the user name correctly.")
           name = input("enter username here:")
           webbrowser.open(f"www.instagram.com/{name}")
           speak(f"sir here is the profile of the user {name}")
           time.sleep(5)
           speak("sir would you like to download the profile picture of this account.")
           condition = takecommand().lower()
           
           if "yes" in condition or "yeah" in condition:
               mod = instaloader.Instaloader()
               mod.download_profile(name, profile_pic_only=True)
               speak("i am done sir, profile picture is saved in our main folder.now i am ready sir")
           else:
                pass


       elif 'translate this please' in query or 'translate' in query:
           speak('tell me the line')
           tran()


       elif 'read the pdf' in query:
           pdf_reader()


       elif 'can you search this video on youtube' in query:
           speak('oh sure sir!')
           speak('what should I search  on youtube ?')
           search = takecommand().lower()
           r =('results?search_query=')
           webbrowser.open(f"https://www.youtube.com/{r}{search}")
           speak('opening youtube')

       elif 'start screen recording' in query or 'record the screen' in query:
           
           while True:
               
               img=pyautogui.screenshot()
               frame=np.array(img)
               frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
               out.write(frame)
               cv2.imshow('show',frame)
               if cv2.waitKey(1)==ord('q'):
                   
                   break                      
           out.release()
           cv2.destroyAllWindows()


       elif "hide all files" in query or "hide this folder" in query or "visible for everyone" in query:
            speak("sir please tell me you want to hide this folder or make it visible to everyone")
            condition = takecommand().lower()
           
            if "hide" in condition:
                os.system("attrib +h /s /d") #os module
                speak("sir, all files in this folder are now hidden.")

            elif "visible" in condition:
                os.system("attrib -h /s /d")
                speak("sir,all the files in this folder is now visible to everyone.I wish you are taking this decision in your own peace. ")

            elif "leave it" in condition or "leave for now" in condition:
                speak("ok sir")
       
       elif 'activate how to do mod' in query:
           speak('how to do mode activated please tell me what you want to know')
           how = takecommand()
           max_results = 1
           how_to = search_wikihow(how,max_results)
           assert len(how_to) == 1
           how_to[0].print()
           speak(how_to[0].summary)

       elif 'tell me the news' in query:
           speak("please wait sir ,fetching the latest news")
           news()


       elif "my ip address" in query:
           ip =  get('https://api.ipify.org').text
           speak(f"your IP address is {ip}")

       elif 'switch window' in query:
           pyautogui.keyDown("alt")
           pyautogui.press("tab")
           time.sleep(1)
           pyautogui.keyUp("alt")
       
       elif 'check the internet speed'in query:
           import speedtest
           st = speedtest.speedtest()
           dl = st.download()
           up = st.upload()
           speak(f'sir we have {dl} bit per second downloading speed and {up} bit per second uploading speed')
  
       if 'play music' in query or 'playe me a song' in query:
           music()
           time.sleep(30)

       elif 'temperature' in query:
           a=query.replace('what is the temperature in','')
           search =(f'temperature in {a}')
           url=f'https://www.google.com/search?q={search}'
           r=requests.get(url)
           data = BeautifulSoup(r.text,'html.parser')
           temp = data.find('div',class_='BNeawe').text
           speak(f'current {search} is {temp}')


       elif 'record the following' in query or 'record the voice' in query or 'start recording' in query:
           record()
        
       elif 'where am I ' in query or 'where are we' in query:
           import json
           speak("wait sir ,let me check")
           try:
                               
               ipAdd = requests.get('https://api.ipify.org').text
               print(ipAdd)
               url = 'https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
               geo_requests = requests.get(url)
               geo_data = geo_requests.json()
               city = geo_data['city']
               state = geo_data['region'] 
               country  = geo_data['country']
               speak(f'sir  I think we are in {city} city  of {state} state and {country} country')            
           except Exception as e:
                                   
               speak('sorry sir due to network error I am not able to find where we are')

       elif 'hello' in query or 'hello jarvis' in query:
           speak('hello sir ')

       elif 'open camera' in query:
           import cv2
           cap = cv2.VideoCapture(0)
           while True:
               ret, img = cap.read()
               cv2.imshow('webcam',img)
               k=cv2.waitKey(50)
               if k==27:
                   break
           cap.release()
           cv2.destroyAllWindows()

       elif 'track this number please' in query:
           tracker()

       elif 'remember that' in query:
           speak("what should I remember?")
           data = takecommand()
           f = open("data.txt", "a")
           print(f.writable())
           speak("you said me to remember that" +data)
           remember = open('data.txt', 'w')
           remember.write(data)
           remember.close()

           
       elif "move away" in query or "take rest" in query or 'stop listening' in query:
           speak("for how much seconed  you want to stop jarvis  from listening commands")

           try:
               a = int(takecommand())
               speak("going to sleep sir")
               speak(a)
               time.sleep(a)
           except Exception as e:
               speak("I could not understand")
               stoplistening()           

       elif 'do you know anything' in query:
           remember =open('data.txt', 'r')
           speak("you said to remember" +remember.read())

        
         
       elif 'good morning' in query:
           speak('good morning sir')
        



       
       elif 'good afternoon jarvis' in query:
           speak('good afternoon sir, have you had your lunch')
       
       elif 'yes' in query:
           speak('ok sir')

       elif 'good evening' in query:
           speak('good evening sir, how was your day?')

         

       elif 'bye' in query or "you can sleep" in query or 'go offline' in query:
           speak("bye amandeep, happy to help you")
           
           exit()



       elif 'what is your name' in query:
           speak('my name is jarvis')



       elif 'open notepad' in query:

            speak("ohh, sure sir")
            npath = "C:\\WINDOWS\\system32\\notepad.exe"
            os.startfile(npath)

       elif 'thank you jarvis' in query:
           speak("its my pleasure sir")

       elif 'shutdown the system' in query:
           os.system("shutdown /s /t 5")
            
       else:
           try:
               try:
                   if 'who' in query:
                       query=query.replace('who','')
                       a=(f'who {query}')
                       res = client.query(a)
                       results = next(res.results).text
                       speak(results)
                   elif 'what' in query:
                       query=query.replace('what','')
                       a=(f'what {query}')
                       res = client.query(a)
                       results = next(res.results).text
                       speak(results)

                   elif 'which' in query:
                       query=query.replace('which','')
                       a=(f'which {query}')
                       res = client.query(a)
                       results = next(res.results).text
                       speak(results)
                   elif 'when' in query:
                       query=query.replace('when','')
                       a=(f'when {query}')
                       res = client.query(a)
                       results = next(res.results).text
                       speak(results)
                   elif 'how' in query:
                       query=query.replace('how','')
                       a=(f'how {query}')
                       res = client.query(a)
                       results = next(res.results).text
                       speak(results)

                   elif 'why' in query:
                       query=query.replace('why','')
                       a=(f'why {query}')
                       res = client.query(a)
                       results = next(res.results).text
                       speak(results)

                   elif 'where' in query:
                       query=query.replace('where','')
                       a=(f'where {query}')
                       res = client.query(a)
                       results = next(res.results).text
                       speak(results)

                   else:
                       
                       query = takecommand().lower()
                       res = client.query(query)
                       results = next(res.results).text
                       speak(results)
               except:
                   
                   results = wikipedia.summary(query, sentences=2)             
                   speak(results)  
        
           except:
               
               speak('sorry sir I don\'t have enough data. I Will try to get it as soon as possible')
      




