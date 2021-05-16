import time
from time import sleep
import GrovePi
import RPi.GPIO as GPIO
from GrovePi import *

GPIO.setmode(GPIO.BCM)

blinkCount = 3
count = 0
LEDPin = 4
buttonPin = 3
#buttonPin2 = 4
#buttonPin3 = 5


GPIO.setup(LEDPin, GPIO.OUT)

GPIO.setup(buttonPin, GPIO.IN, pull_up_down = GPIO.PUD_UP)
#GPIO.setup(buttonPin2, GPIO.IN, pull_up_down = GPIO.PUD_UP)
#GPIO.setup(buttonPin3, GPIO.IN, pull_up_down = GPIO.PUD_UP)

buttonPress = True
ledState = False

try:
    while count < blinkCount:
        print("Play the E-Minor chord")
        buttonPress = GPIO.input(buttonPin)
        if buttonPress == False and ledState == False:
            GPIO.output(LEDPin, True)
            print ("LED ON")
            ledState = True
            Sleep(3)
        elif buttonPress == False and ledState == True:
            GPIO.output(LEDPin, False)
            print("CORRECT!")
            ledState = False
            count += 1
            sleep(0.5)
        sleep(2.0)
        
#try:
 #   while count < blinkCount:
       # print("Play the C-Major chord")
       # buttonPress = GPIO.input(buttonPin)
       # buttonPress2 = GPIO.input(buttonPin2)
       # buttonPress3 = GPIO.input(buttonPin3)
       # if buttonPress == False and buttonPress2 == False and buttonPress3 == False and ledState == False:
         #   GPIO.output(LEDPin, True)
          #  print ("LED ON")
          #  ledState = True
         #   Sleep(3)
      #  elif buttonPress == False and buttonPress2 == False and buttonPress3 == False and ledState == True:
       #     GPIO.output(LEDPin, False)
        #    print("CORRECT!")
         #   ledState = False
        #    count += 1
         #   sleep(0.5)
        #sleep(2.0)
finally:
    GPIO.cleanup()
    