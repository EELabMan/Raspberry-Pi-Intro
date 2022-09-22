import RPi.GPIO as GPIO 
import time
import sys 
 
#pin definitions 

pwmPin = 23 
ledPin = 18
butPin = 17 
duty = 10


##GPIO setup ## 

GPIO.setwarnings(False)   
GPIO.setmode(GPIO.BCM) # BCM way of refering to pins 
GPIO.setup(ledPin, GPIO.OUT) 
GPIO.setup(pwmPin, GPIO.OUT) 
GPIO.setup(butPin, GPIO.IN,pull_up_down=GPIO.PUD_UP) 

pwm = GPIO.PWM(pwmPin, 2000) # PWM frequency in Hz 

GPIO.output(ledPin, GPIO.LOW) # default off 

pwm.start(duty) # start at 10% 

try: 

    while 1: 

        if GPIO.input(butPin): 
            pwm.ChangeDutyCycle(duty) 
            GPIO.output(ledPin, GPIO.HIGH) 
         
            #Pressed 
        else: 
            GPIO.output(ledPin, GPIO.LOW) 
            for dc in range(1, 101, 1): # Increase duty cycle: 0~100
                pwm.ChangeDutyCycle(dc) # Change duty cycle
                time.sleep(0.02)
            for dc in range(100, 0, -1): # Decrease duty cycle: 100~0
                pwm.ChangeDutyCycle(dc)
                time.sleep(0.02)
            

except KeyboardInterrupt: 
    pwm.stop() 
    GPIO.cleanup() 
