#_______________________________________________Modules used
import os
from subprocess import call
from PIL import Image,ImageOps
import numpy as np
import pyttsx3
import RPi.GPIO as GPIO
import time

#_______________________________________________functions defined
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#_______________________________________________variable names (set here)
i=True

while True:
    
    input_state=GPIO.input(18)
    #input_state = input("\nenter :")
    if input_state == False:
        if i:
            i=False
        else:
            i=True
        try:
            engine=pyttsx3.init()
            if i:
                engine.say('Button Pressed')
            
                print('Button Pressed')
                engine.runAndWait()
            time.sleep(0.2)
            image="image.jpg"
            text_file="text"
            new_image="formatted1.jpg"

            #___________________________________-clicking image
            os.system("sudo fswebcam -d /dev/video0 -r 1280*960 image.jpg")
            if i:
                engine.say("image clicked")
                engine.runAndWait()
                print "image clicked"
            
            #___________________________________Image formatting
            im=Image.open(image)
            im_g=ImageOps.grayscale(im)
            im_gc=ImageOps.autocontrast(im_g,cutoff=10,ignore=0)
            im_gc.save(new_image)

            #___________________________________image to text
            if i:
                print("tesseract "+new_image+" "+text_file)
                engine.say("OCR complete")
                engine.runAndWait()
                print ("OCR complete")
            call ("tesseract "+new_image+" "+text_file,shell=True)
            
            input_state=True

            #___________________________________text formatting
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
            
            #______________________________Text to speech
            engine=pyttsx3.init()
            text_file="ftext"
            if not i:
                text_file="blank"
            voices=engine.getProperty('voices')
            engine.setProperty('voice',voices[33].id)
            file=open(text_file+".txt",'r')
            #sentence=file.readlines()
            for i in "output started.".split():
                engine.say(i)
            sentence=file.read()
            print sentence
            sentences=sentence.split()
            for word in sentences:
                word=word.rstrip()
                word=word.lstrip()
                print word
                #engine.say(word)
                #time.sleep(2)
            engine.say(sentences)
            engine.runAndWait()
            #time.sleep(30)
            
        except:
            sys.stdout.flush()
        print "complete"
        engine.say("Press the button to continue.")
        engine.runAndWait()
        file.close()
