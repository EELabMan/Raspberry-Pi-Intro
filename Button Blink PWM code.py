import RPi.GPIO as GPIO 
import time 
 
#pin definitions 

pwmPin = 18 
ledPin = 23 
butPin = 17 
duty = 50 


##GPIO setup ## 

GPIO.setwarnings(False)   
GPIO.setmode(GPIO.BCM) # BCM way of refering to pins 
GPIO.setup(ledPin, GPIO.OUT) 
GPIO.setup(pwmPin, GPIO.OUT) 
GPIO.setup(butPin, GPIO.IN,pull_up_down=GPIO.PUD_UP) 

pwm = GPIO.PWM(pwmPin, 1000) # PWM frequency = 200Hz 

GPIO.output(ledPin, GPIO.LOW) # default off 

pwm.start(duty) # start at 75% 

try: 

    while 1: 

        if GPIO.input(butPin): 
            pwm.ChangeDutyCycle(duty) 
            GPIO.output(ledPin, GPIO.LOW) 
         
            #Pressed 
        else: 
            GPIO.output(ledPin, GPIO.HIGH) 
            pwm.ChangeDutyCycle(duty) 
            time.sleep(1.5) 
            GPIO.output(ledPin, GPIO.LOW) 
            pwm.ChangeDutyCycle(100) 
            time.sleep(1.5) 
            

except KeyboardInterrupt: 
    pwm.stop() 
    GPIO.cleanup() 

     