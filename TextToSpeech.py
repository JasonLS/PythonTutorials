import os
 
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)


GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)
 

while 1:
    if GPIO.input(7) == GPIO.HIGH:
        os.system('flite -t "Use the force Luke!" ')

    
