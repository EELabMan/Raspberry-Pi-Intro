import RPi.GPIO as GPIO
import sys
from time import sleep


butPin = 17 
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)  # GPIO.BOARD to reference pin numbers
GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(butPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try: 
    while 1: 
        if GPIO.input(butPin): 
            GPIO.output(18, GPIO.HIGH)
            GPIO.output(23, GPIO.LOW)
            sleep(.2)
            GPIO.output(18, GPIO.LOW)
            GPIO.output(23, GPIO.HIGH)
            sleep(.2)
            #Pressed
            
        else:
            GPIO.output(18, GPIO.LOW)
            GPIO.output(23, GPIO.HIGH)
            sleep(1)
            GPIO.output(18, GPIO.HIGH)
            GPIO.output(23, GPIO.LOW)
            sleep(1)
        

except KeyboardInterrupt: 
    GPIO.cleanup()   
    
     
