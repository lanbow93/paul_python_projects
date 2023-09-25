import RPi.GPIO as GPIO
import time
global isRunning
isRunning = True

def make_blink(amount_of_blinks):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(11, GPIO.OUT)
    for i in range(0, amount_of_blinks, 1):
        GPIO.output(11, True)
        time.sleep(.3)
        GPIO.output(11, False)
        time.sleep(.3)
        i = i + 1
    GPIO.cleanup()    

def request_blinks():
    user_choice = input("How many blink do you want? (Limit 10)")
    # Checks to see if value is number
    if (user_choice.isnumeric()):
        converted_choice = int(user_choice)
        if(converted_choice > 10):
            print("The value you entered was too large. Try again\n")
            request_blinks()
        elif(converted_choice < 0):
            print("We cannot do negative blinks. Try again\n")
            request_blinks()
        elif(converted_choice == 0):
            print("Cool..... nothing happened\n")
            return
        elif(converted_choice > 0 and converted_choice <= 10):
            make_blink(converted_choice)
    elif (not user_choice.isnumeric):
        print("The value you entered was not a number. Try again\n")
        request_blinks()


def initial_statement():
    user_choice = input("Do you want to make light blink? (Y/N)\n")

    
    if(user_choice == "y" or user_choice == "Y"):
        request_blinks()
    
    elif(user_choice == "n" or user_choice =="N"):
        global isRunning 
        isRunning = False
    elif(user_choice != "y" or user_choice != "Y" or user_choice != "n" or user_choice != "n"):
        print("Invalid Choice, try again\n")
        initial_statement()

while (isRunning):
    initial_statement()

