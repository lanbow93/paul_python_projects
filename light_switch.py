import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)
light_out = 11
switch_in = 40

GPIO.setup(switch_in, GPIO.IN)
GPIO.setup(light_out, GPIO.OUT)

try:
    while(True):
        switch_value = GPIO.input(switch_in)
        GPIO.output(light_out, switch_value)
        print(switch_value)
        sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()


