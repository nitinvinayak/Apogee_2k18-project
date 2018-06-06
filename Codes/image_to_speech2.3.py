#_______________________________________________Modules used
import os
from subprocess import call
from PIL import Image,ImageOps
import numpy as np
import pyttsx3
import RPi.GPIO as GPIO
import time

#_______________________________________________functions defined
def speak(x):
    engine=pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[33].id)    
    engine.say(x)
    print(x)
    engine.runAndWait()
def click(i):
    if i%2==1:
        os.system("sudo fswebcam -d /dev/video0 -r 1280*960 image.jpg")
        speak("image clicked")
    else:
        os.system("sudo fswebcam -d /dev/video0 -r 1280*960 image2.jpg")

def image_process(i):
    if i%2==1:
        im=Image.open(image)
        im_g=ImageOps.grayscale(im)
        im_gc=ImageOps.autocontrast(im_g,cutoff=10,ignore=0)
        im_gc.save(new_image)

def text(i):
    if i%2==1:
        print("tesseract "+new_image+" "+text_file)
        call ("tesseract "+new_image+" "+text_file,shell=True)
        print ("OCR complete")
        speak("OCR complete")

def text_format(i):
    if i%2==1:
        ifile=open("text.txt","r")
        ofile=open("ftext.txt","w")
        sents=ifile.readlines()
        for sent in sents:
            print sent
            if sent!="\n":
                sent=sent.rstrip("\n")
                sent=sent.lstrip()
                ofile.write(sent+"\n")
        ifile.close()
        ofile.close()


GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#_______________________________________________variable names (set here)
image="image.jpg"
text_file="text"
new_image="formatted1.jpg"
text_file_format="ftext"
counter=1
#_______________________________________________Main code
while counter>=1:
    
    input_state=GPIO.input(18)
    #input_state = input("\nenter :")
    if input_state == False:
        try:
            speak('Button Pressed')
            time.sleep(0.2)
            

            #___________________________________-clicking image
            click(counter)
            
            #___________________________________Image processing
            image_process(counter)

            #___________________________________image to text
            text(counter)
            input_state=True

            #___________________________________text formatting
            text_format(counter)
            
            #______________________________Text to speech
            
            if i%2==1:
                speak("output started.")
            else:
                text_file_format="blank"
                
            file=open(text_file_format+".txt",'r')
            #sentence=file.readlines()
            
            
            sentence=file.read()
            print sentence
            sentences=sentence.split()
            speak(sentences)
            #time.sleep(30)
            
            
        except:
            sys.stdout.flush()
        
        if i%2==0:
            speak("The device is ready for use.")
        else:
            speak("Press the button to continue")
        file.close()
        i=i+1
