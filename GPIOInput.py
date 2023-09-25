import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
inPin = 40
GPIO.setup(inPin, GPIO.IN)
readValue = GPIO.input(inPin)

print(readValue)
GPIO.cleanup()