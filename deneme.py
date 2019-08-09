# -*- coding: utf-8 -*-
import speech_recognition as sr
import os
import sys
#from playsound import playsound
#import time
#from gtts import gTTS

r = sr.Recognizer()

#hmrway = os.path.dirname(os.path.abspath(__file__)) + "/audio.wav"
#hmr = sr.AudioFile("/home/closx/tools/ai/davis/audio.wav")
with sr.Microphone() as source:
     print("Birşeyler Söyle!")
     audio = r.listen(source)

data = ""
try:
   data = r.recognize_google(audio, language='tr-tr')
   data = data.lower()
   print("Bunu Söyledin :" + data)
except sr.UnknownValueError:
       print("Ne dediğini anlamadım")