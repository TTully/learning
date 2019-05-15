import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)    # choose BCM(for GPIO numbering) or BOARD(for pin numbering)
GPIO.setwarnings(False)     # turned off warnings


Pir = 29 # Assigning pin number to variable
GPIO.setup(Pir,GPIO.IN)     # Setting Pir (Pin) as an Input Pin
State = 0 # Global variable 

def MotionDection(x):
    global State
    State =1

GPIO.add_event_detect(Pir, GPIO.FALLING, MotionDection)

while(True):
    if (State ==1):
        print("motion Detected! ")
        time.sleep(6)
        State =0
    else:
        print("waiting for motion to be detected....")
        time.sleep(2)


