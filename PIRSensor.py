import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
#GPIO.s(GPIO.BOARD)
GPIO.setup(11, GPIO.IN)         #Read output from PIR motion sensor
GPIO.setup(3, GPIO.OUT)         #LED output pin
import urllib.request


#this function return 1 if the PIR Sensor has a motion, return 0 if no motion
def readPIR(delay=1):
    
    
    i=GPIO.input(11)
    if i==0:                 #When output from motion sensor is LOW
        print ("No intruders"),i
        time.sleep(.1)

    elif i==1:               #When output from motion sensor is HIGH
        print ("Intruder detected"),i
        time.sleep(delay)

    return i


def checkConnection(host='http://google.com'):
    try:
        urllib.request.urlopen(host) #Python 3.x
        return True
    except:
        return False



print("PIR NOW : ", readPIR())