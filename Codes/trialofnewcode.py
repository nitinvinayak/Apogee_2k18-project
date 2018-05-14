import time

from subprocess import call

import re

import urllib2

 

 

#Function splits a big paragraph into smaller sentences for easy TTS

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

        print cmd_beg+spk+cmd_end

        call ([cmd_beg+spk+cmd_end], shell=True)

 

def download_web_image(url):

    #name = random.randrange(1,1000)

    full_name = str('j2') + ".jpg"

    request = urllib2.Request(url)

    img = urllib2.urlopen(request).read()

    with open (full_name, 'w') as f: f.write(img)

 

 

running =True

while running:

 

        running=False

        #download_web_image("https://lists.w3.org/Archives/Public/public-comments-wcag20/2011Nov/att-0005/anti-aliased_text_screen300pc.jpg")

        #Start the Tesseract OCR and save the text to out1.txt

        call ("tesseract preimage.jpg out1", shell=True)

        print "OCR complete"

        

        #Open the text file and split the paragraph to Sentences

        fname="out1.txt"

        f=open(fname)

        content=f.read()

        print content

        sentences = splitParagraphIntoSentences(content)
        sound("fuck you, maadarrchoodh)

 

        #Speak aloud each sentence in the paragraph one by one

        for s in sentences:

                sound(s.strip())
