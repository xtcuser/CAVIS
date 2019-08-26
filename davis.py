# -*- coding: utf-8 -*-
#import speech_recognition as sr
#from playsound import playsound
import os
import sys
import time
import wikipedia
import configparser
import selenium
import random
from selenium import webdriver
#from gtts import gTTS

datacounter = 0
lastdata = ""

def speak(audioString):
    print("davis: " + audioString)
    #tts = gTTS(text=audioString, lang='tr')
    #apath = os.path.dirname(os.path.abspath(__file__)) + "/audio.wav"
    #tts.save(apath)
    #playsound(apath)

def listen():
    #data = recordAudio()
    global lastdata
    global datacounter
    data = input("closx: ")
    if lastdata == data.lower():
        datacounter = datacounter + 1
    else:
        datacounter = 0
    if datacounter > 1:
        speak("Sanırım bunu daha önce konuşmuştuk. Başka ne konuda yardımcı olabilirim?")
        listen()

    else:
        datalw = data.lower()
        lastdata = datalw
        general(datalw)

def listendev():
    #data = recordAudio()
    global lastdata
    global datacounter
    data = input("closx: ")
    if lastdata == data.lower():
        datacounter = datacounter + 1
    else:
        datacounter = 0
    if datacounter > 1:
        speak("Sanırım bunu daha önce konuşmuştuk. Başka ne konuda yardımcı olabilirim?")
        listen()

    else:
        datalw = data.lower()
        lastdata = datalw
        developermode(datalw)
    

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

    if data in selam:
        speak(selamcvp[random.randint(0,2)])
        listen()

    if "çıkış" in data:
        speak("Tamam, görüşmek üzere!")
        time.sleep(3)
        sys.exit()

    if "naber" in data:
        speak(iyisen[random.randint(0,2)])
        listensup()

    if data in nabiyon:
        speak(nabiyoncvp[random.randint(0,2)])
        listenwyd()

    if "saat" in data:
        speak("Şuan saat " + time.strftime("%H %M"))
        listen()

    if "teşekkür" in data:
        speak("Rica ederim!")
        listen()

    if "nedir" in data:
        datalw = data.lower()
        wiki(datalw)

    if "geliştirici" in data:
        speak("Hoşgeldiniz, efendim.")
        listendev()

    else:
        speak(anlamadim[random.randint(0,2)])
        listen()


def developermode(data):
    
    if "ini" in data and "sil" in data:
        speak("Nasıl isterseniz. Yeniden başlatma gerekiyor.")
        os.remove(configpath)
        os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)

    if "genel mod" in data:
        "Genel moda geçiliyor."
        listen()

    if "çıkış" in data:
        speak("Tamam, görüşmek üzere!")
        #time.sleep(3)
        sys.exit()

    if "saat" in data:
        speak("Şuan saat " + time.strftime("%H %M"))
        listen()

    if "teşekkür" in data:
        speak("Rica ederim!")
        listen()

    else:
        speak(anlamadim[random.randint(0,2)])
        listen()

def process(data):
    speak(cokiyi[random.randint(0,3)])
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
    if data in nabiyon:
        speak(nabiyoncvp[random.randint(0,2)])
        listenwyd()
    if "iyi" in data:
        if "değil" in data or "sayılma" in data:
            speak(cokkotu[random.randint(0,3)])
            listen()
        else:
            speak(cokiyi[random.randint(0,3)])
            listen()
    if "kötü" in data or "fena" in data:
        if "değil" in data or "sayılma" in data:
            speak(cokiyi[random.randint(0,3)])
            listen()
        else:
            speak(cokkotu[random.randint(0,3)])
            listen()
    else:
        speak("Pardon ama bu cevabı anlamadım. Senin için başka ne yapabilirim?")
        listen()


configpath = os.path.dirname(os.path.abspath(__file__)) + "/vars.ini"
config = configparser.ConfigParser()

def dataminer(section):
    dict1 = {}
    options = config.options(section)
    for option in options:
        try:
            dict1[option] = config.get(section, option)
        except:
            dict1[option] = None
    return dict1

isim = ""

def frconfig():
    if(os.path.exists(configpath)):
        if(os.stat(configpath).st_size == 0):
            os.remove(configpath)

    if(os.path.exists(configpath)):
        config.read(configpath)
        isimlw = config['userdata']['name']
        global isim 
        isim = isimlw.capitalize()
        speak("Merhaba " + isim + ", Sana Nasıl Yardımcı Olabilirim?")
    else:
        cfgfile = open(configpath,'w')
        speak("Merhaba, Ben Davis. Size nasıl hitap etmemi istersiniz?")
        isiminput = input("closx: ")
        isim = isiminput.capitalize()
        isimlw = isim.lower()
        config.add_section('userdata')
        config.set('userdata','name',isimlw)
        config.write(cfgfile)
        cfgfile.close()
        speak("Merhaba " + isim + ", Sana Nasıl Yardımcı Olabilirim?")


selam = ["selam","hey","merhaba"]
selamcvp = ["Merhaba!","Merhaba, "+ isim +"!","Seni görmek güzel, "+ isim +"!","Hey, "+ isim +"!"]
nabiyon = ["ne yapıyorsun","napıyorsun","napıyon","nasıl gidiyo","nasıl gidiyor","nabıyon","napıyosun"]
nabiyoncvp = ["Robot olmak dışında hiçbir şey yapmıyorum, "+ isim +". Ya sen?","Senin için kendimi geliştirmeye çalışıyorum. Sen?","Öyle takılıyorum. Sen ne yapıyorsun?"]
cokiyi = ["Bu çok güzel!","Bunu duymak müthiş!","Böyle devam et!","Harikasın!"]
cokkotu = ["Bu çok kötü!","Bunu duymak berbat!","Umarım böyle devam etmez!","Senin adına üzüldüm!"]
iyisen = ["İyiyim "+ isim +", sen nasılsın?","İyiyim "+isim+", seni sormalı.","Ben her zamanki gibiyim "+isim+", asıl senden ne haber?"]
anlamadim = ["Bunun ne demek olduğunu bilmiyorum.","Ne dediğini anlamadım.","Maalesef, ne demek istediğini anlayamadım.","Anlayamadım."]

frconfig()
listen()