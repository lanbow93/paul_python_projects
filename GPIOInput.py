import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
inPin = 40
GPIO.setup(inPin, GPIO.IN)
try:
    while(True):
        readValue = GPIO.input(inPin)
        print(readValue)
        sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()