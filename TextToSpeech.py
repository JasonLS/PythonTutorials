#Adapted from https://learn.adafruit.com/speech-synthesis-on-the-raspberry-pi/programs
#install flite using sudo apt-get install flite



import os
 
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

RedButton = 7 #Variable "RedButton" is set to pin 7 on header

GPIO.setup(RedButton, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Sets Pin 7 as an input with pullup
 

while 1:
    if GPIO.input(RedButton) == GPIO.LOW: #If the button is pushed...
        os.system('flite -t "Put " ') #Text to Speech Command
