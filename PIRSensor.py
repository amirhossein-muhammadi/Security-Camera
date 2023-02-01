import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)         # GPIO is faking by making a module in the root
                                # When connected to rapsberry we can use gpio of pie
#GPIO.s(GPIO.BOARD)
GPIO.setup(11, GPIO.IN)         #Read output from PIR motion sensor
GPIO.setup(3, GPIO.OUT)         #LED output pin
import urllib.request


#this function return 1 if the PIR Sensor has a motion, return 0 if no motion
def readPIR():
    
    
    i=GPIO.input(11)
    if i==0:                 #When output from motion sensor is LOW
        print ("No intruders",i)
        return i
        
    elif i==1:               #When output from motion sensor is HIGH
        print ("Intruder detected",i)
        return i



def checkConnection(host='http://google.com'):
    try:
        urllib.request.urlopen(host) #Python 3.x
        return True
    except:
        return False



print("PIR NOW : ", readPIR())
