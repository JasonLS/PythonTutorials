#Adapted from https://learn.adafruit.com/speech-synthesis-on-the-raspberry-pi/programs
#install flite using sudo apt-get install flite



import os
 
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

Thames = 3 
Belgium = 5 
Coast = 7 #Variable "v3" is set to pin 7 on header
Firststation = 8 
Steamboat = 10 
Centralstation = 11 
Innerstation = 12 


GPIO.setup(3, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Sets Pin 3 as an input with pullup
GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(8, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)

BelgiumVal = 0
SteamboatVal = 0

while 1:
    if GPIO.input(Thames) == GPIO.LOW: #If the button is pushed...
        os.system('flite -voice slt -f Thames.txt') #Text to Speech Command
    elif GPIO.input(Belgium) == GPIO.LOW and BelgiumVal == 0:
        os.system('flite -voice slt -f Belgium.txt')
        BelgiumVal += 1
    elif GPIO.input(Belgium) == GPIO.LOW and BelgiumVal == 1:
        os.system('flite -voice slt -f BelgiumReturn.txt')
        BelgiumVal -= 1
     elif GPIO.input(Coast) == GPIO.LOW:
        os.system('flite -voice slt -f Coast.txt')
     elif GPIO.input(Firststation) == GPIO.LOW:
        os.system('flite -voice slt -f Firststation.txt')
     elif GPIO.input(Steamboat) == GPIO.LOW and SteamboatVal = 0:
        os.system('flite -voice slt -f Steamboat.txt')
        SteamboatVal += 1
     elif GPIO.input(Coast) == GPIO.LOW and SteamboatVal = 1:
        os.system('flite -voice slt -f SteamboatReturn.txt')
        SteamboatVal -= 1
     elif GPIO.input(Cantralstation) == GPIO.LOW:
        os.system('flite -voice slt -f Centralstation.txt')
     elif GPIO.input(Innerstation) == GPIO.LOW:
        os.system('flite -voice slt -f Innerstation.txt')       
       
       
