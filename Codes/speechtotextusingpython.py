import os
import pyttsx
#from subprocess import call
#call ("tesseract preimage.jpg out2", shell=True)

#using pyttsx
'''
engine=pyttsx.init()
engine.say('The quick brown fox jumped over the lazy dog')
engine.runAndWait()
'''
from PIL import Image
import numpy as np
'''from PIL import ImageEnhance
from PIL import ImageFilter
from scipy.misc import imsave


image_file = Image.open("IMAG0214.jpg") # open colour image
image_file= image_file.convert('L') # convert image to monochrome - this works
image_file= image_file.convert('1') # convert image to black and white
image_file.save('result_col.png')
#im=Image.open("1.jpg")
#im=im.rotate(1)
#im.save("e.jpg")
#im2=im.convert("L")
#im2.save("b.jpg")
threshold = 50

im = image_file.point(lambda p: p < threshold and 100) #
#im = image_file.point(lambda p: p > threshold and 255)
im.save("d.jpg")
img="d.jpg"
#result = tesseract.ProcessPagesWrapper(img,api)
#print result
'''

engine=pyttsx.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[33].id)
file=open("out2.txt",'r')
text=file.readlines()
for i in text:
    engine.say(i)
engine.runAndWait()
file.close()


'''
#Different voices
engine=pyttsx.init()
voices=engine.getProperty('voices')
for i in [33,68]:
    engine.setProperty('voice',voices[i].id)
    engine.say()
engine.runAndWait()
'''

