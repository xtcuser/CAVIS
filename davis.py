# -*- coding: utf-8 -*-
#import speech_recognition as sr
#from playsound import playsound
import os
import sys
import time
import wikipedia
import selenium
from selenium import webdriver
#from gtts import gTTS
 
def speak(audioString):
    print("davis: " + audioString)
    #tts = gTTS(text=audioString, lang='tr')
    #apath = os.path.dirname(os.path.abspath(__file__)) + "/audio.wav"
    #tts.save(apath)
    #playsound(apath)

def listen():
    #data = recordAudio()
    data = input("closx: ")
    datalw = data.lower()
    general(datalw)

def listensup():
    #data = recordAudio()
    data = input("closx: ")
    datalw = data.lower()
    sup(datalw)

def listenwyd():
    #data = recordAudio()
    data = input("closx: ")
    process(data)

#def recordAudio():
    #with sr.Microphone() as source:
    #    r = sr.Recognizer()
    #    print("Bir şeyler söyle!")
    #    audio = r.listen(source)

    #data = ""
    
    #try:
        #data = r.recognize_google(audio, language='tr-tr')
        #data = data.lower()
    #except sr.UnknownValueError:
        #print("Google Speech Recognition could not understand audio")
    #return data
 
def general(data):
    if "merhaba" in data or "selam" in data or "hey" in data:
        speak("Merhaba, Onur!")
        listen()

    if "çıkış" in data:
        speak("Tamam, görüşmek üzere!")
        time.sleep(3)
        sys.exit()

    if "naber" in data:
        speak("İyiyim Onur, sen nasılsın?")
        listensup()

    if "ne yapıyorsun" in data or "nabıyon" in data or "napıyorsun" in data or "napıyon" in data:
        speak("Robot olmak dışında hiçbir şey yapmıyorum, Onur. Ya sen?")
        listenwyd()

    if "saat" in data:
        speak("Şuan saat " + time.strftime("%H %M"))

    if "teşekkür" in data:
        speak("Rica ederim!")

    if "nedir" in data:
        datalw = data.lower()
        wiki(datalw)

    else:
        #speak("Bu komutu bilmiyorum.")
        listen()

def process(data):
    speak("Bu çok güzel!")
    listen()

def wiki(data):
    sword = data.split("nedir")
    wikipedia.set_lang("tr")
    dpath = os.path.dirname(os.path.abspath(__file__)) + "/chromedriver"
    drivery = webdriver.Chrome(dpath)
    drivery.get("http://www.wikizero.biz/wiki/tr/" + sword[0]);
    select_element = drivery.find_elements_by_xpath('//*[@id="mw-content-text"]/div[1]/p[1]')
    for option in select_element:
        x = option.find_element_by_xpath('//*[@id="mw-content-text"]/div[1]/p[1]').text
        speak("Wikipedia'ya göre, " + x)
    listen()

def sup(data):
    if "ne yapıyorsun" in data or "nabıyon" in data or "napıyorsun" in data or "napıyon" in data:
        speak("Robot olmak dışında hiçbir şey yapmıyorum, Onur. Ya sen?")
        listenwyd()
    if "iyi" in data:
        if "değil" in data or "sayılma" in data:
            speak("Senin için üzüldüm.")
            listen()
        else:
            speak("İyi olman çok güzel!")
            listen()
    if "kötü" in data or "fena" in data:
        if "değil" in data or "sayılma" in data:
            speak("iyi olman çok güzel!")
            listen()
        else:
            speak("Senin için üzüldüm.")
            listen()
    else:
        speak("Cevap vermeye niyetin yok sanırım. Senin için başka ne yapabilirim?")
        listen()



speak("Merhaba Onur, Sana Nasıl Yardımcı Olabilirim?")
listen()