import picar_4wd as fc
import time
import numpy as np
import math
import RPi.GPIO as GPIO

speed = 15

def mforward():
    speed4 = fc.Speed(25)
    speed4.start()
    fc.forward(speed)
    x = 0
    for i in range(10):
        time.sleep(0.1)
    
    speed4.deinit()
    fc.stop()
    
def mbackward():
    speed4 = fc.Speed(25)
    speed4.start()
    fc.backward(17)
    x = 0
    for i in range(10):
        time.sleep(0.1)
    
    speed4.deinit()
    fc.stop()
    
def mleft():
    speed4 = fc.Speed(25)
    speed4.start()
    fc.turn_left(15)
    x = 0
    for i in range(13):
        time.sleep(0.1)       
    speed4.deinit()
    fc.stop()    
    
    
    
def mright():
    speed4 = fc.Speed(25)
    speed4.start()
    fc.turn_right(18)
    x = 0
    for i in range(12):
        time.sleep(0.1)       
    speed4.deinit()
    fc.stop()
   
