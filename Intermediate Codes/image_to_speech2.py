#Modules used
import os
from subprocess import call
from PIL import Image,ImageOps
import numpy as np
import pygame.camera
import pygame.image
import pyttsx
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#functions defined


#variable names (set here)
while True:
    input_state = GPIO.input(18)
    if input_state == False:
        print('Button Pressed')
        time.sleep(0.2)
        image="q4.jpg"
        text_file="text"
        new_image="formatted1.jpg"

        #clicking image
        pygame.camera.init()
        cam=pygame.camera.Camera(pygame.camera.list_cameras()[0])
        cam.start()
        img=cam.get_image()
        pygame.image.save(img,"q4.jpg")
        pygame.camera.quit()
        print "image captured"
        

        #Image formatting
        im=Image.open(image)
        im_g=ImageOps.grayscale(im)
        im_gc=ImageOps.autocontrast(im_g,cutoff=10,ignore=0)
        im_gc.save(new_image)

        #image to text
        print("tesseract "+new_image+" "+text_file)
        call ("tesseract "+new_image+" "+text_file,shell=True)
        print ("OCR complete")
        input_state=True


        #Text to speech
        #text_file="sample"
        engine=pyttsx.init()
        voices=engine.getProperty('voices')
        engine.setProperty('voice',voices[33].id)
        file=open(text_file+".txt",'r')
        sentences=file.readlines()
        for sentence in sentences:
            words=sentence.split(" ")
            for word in words:
                engine.say(word)
        engine.runAndWait()
        file.close()
        print "complete"



