import RPi.GPIO as GPIO
import time
import os
from subprocess import call
from PIL import Image,ImageOps
import numpy as np
import re
import pygame.camera
import pygame.image

GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def splitParagraphIntoSentences(paragraph):
    sentenceEnders = re.compile('[.!?]')
    sentenceList = sentenceEnders.split(paragraph)
    return sentenceList

 

#Calls the Espeak TTS Engine to read aloud a sentence
#       -ven+m7:    Male voice
#       -s180:          set reading to 180 Words per minute
#       -k20:           Emphasis on Capital letters

def sound(spk):
    cmd_beg=" espeak -ven+f7 -s180 -k20 --stdout '"
    cmd_end="' | aplay"
    print (cmd_beg+spk+cmd_end)
    call ([cmd_beg+spk+cmd_end], shell=True)

while True:
    input_state = GPIO.input(18)
    if input_state == False:

        #variable names (set here)
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


        #Image formatting
        im=Image.open(image)
        im_g=ImageOps.grayscale(im)
        im_gc=ImageOps.autocontrast(im_g,cutoff=10,ignore=0)
        im_gc.save(new_image)

        #image to text
        print("tesseract "+new_image+" "+text_file)
        call ("tesseract "+new_image+" "+text_file,shell=True)
        print ("OCR complete")


        #Text to speech
        #Open the text file and split the paragraph to Sentences
        fname=text_file+".txt"
        f=open(fname)
        content=f.read()
        print (content)

        sentences = splitParagraphIntoSentences(content)
        sound("Its gonna start")

        #Speak aloud each sentence in the paragraph one by one

        for s in sentences:

            sound(s.strip())
            time.sleep(0.2)
