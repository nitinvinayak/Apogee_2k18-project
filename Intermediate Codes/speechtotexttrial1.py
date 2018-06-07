
from PIL import Image
from pytesser import *
from speech import Speech
from time import sleep

speech = Speech()

IMAGE_FILE = 'imtest.jpg'

# loop forever
while True:

    # load image
    img = Image.open(IMAGE_FILE)

    # detect words in image
    words = image_to_string(pagetext1.txt).strip()
    print words

    # annouce the arrival of Mr Puce! 
    if(words == 'Mr Puce'):
        speech.text_to_speech("Watch out, here comes Mr Puce")

    sleep(5)
