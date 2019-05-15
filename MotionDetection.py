import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)    # choose BCM(for GPIO numbering) or BOARD(for pin numbering)
GPIO.setwarnings(False)     # turned off warnings

# Assigning pin number to variable
Pir = 29;

GPIO.setup(Pir,GPIO.IN)     # Setting Pir (Pin) as an Input Pin

while(True):
    if (GPIO.input(Pir)):
        print("waiting for motion to be detected....")
        time.sleep(2)
        
    else:
        print("motion Detected! ")
        time.sleep(7)

