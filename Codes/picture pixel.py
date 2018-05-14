import picamera
import picamera.array
import cv2
import numpy as np
from numpy import unravel_index
from time import time

#Set resolution here
Width = 80
Height = 60


ArrayY = 0

# Inherit from PiYUVAnalysis
class MyAnalysisClass(picamera.array.PiYUVAnalysis):
    def analyse(self, array):
        global ArrayY   
        global y
        ArrayY = array
        y = ArrayY[:, :, 0]
        (cx, cy) =  unravel_index(y.argmax(), y.shape)  


with picamera.PiCamera() as camera:
    with picamera.array.PiYUVAnalysis(camera) as output:
        camera.resolution = (80, 60)   #FOR SOME REASON, IF I SET THE RESOLUTION IN THE CORRECT ORDER, I GET IT WITH THE AXES INVERTED!
        camera.framerate = 30
        output = MyAnalysisClass(camera)  
        camera.start_recording(output, format='yuv')
        camera.wait_recording(5)
        camera.stop_recording()

print ArrayY.nbytes
print ArrayY.itemsize
print ArrayY.shape
