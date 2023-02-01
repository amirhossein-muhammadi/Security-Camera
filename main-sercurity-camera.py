#OpenCv – Python Code.
# import the necessary packages 
import argparse
import datetime 
import time 
import cv2
import numpy
import time
from emailSender import sendAlertEmail
from PIRSensor import readPIR
from connection import connect
import uuid

ap = argparse.ArgumentParser()

ap.add_argument("-v","--video", help="c://Users//Numbe//Desktop//opencv")
ap.add_argument("-a", "--min-area", type=int, default=1000,)
ap.add_argument("-b", "--bdetection",action="store_true")

args=vars(ap.parse_args())


if args.get("video", None) is None:
    #The camera used  in this project is DroidCam Camera shared by a phone camera
    camera = cv2.VideoCapture("http://192.168.1.101:4747/video")
    time.sleep(1)

else:
    camera = cv2.VideoCapture(args["video"])

    print("-----------------------------video get from source you Entered--------------------")

currentFrame = None

while(True):

    #If pir sensor detect a motion ,camera start to capture    
    #if(readPIR()):
        (grabbed, frame) = camera.read()

        text = "No Motion Detected"

        if not grabbed:
                break
                print("---Frame is not get Grabbed!!----")

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (21, 21), 0)

        

        if currentFrame is None:
            currentFrame = gray 
            continue
        
        previousFrame = currentFrame 
        currentFrame = gray

        frameDelta =cv2.absdiff(previousFrame, gray)

        ret, thresh = cv2.threshold(frameDelta, 100, 255, cv2.THRESH_BINARY)
        
        thresh = cv2.dilate(thresh, None, iterations=2)
        
        (cnts, _) = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, 
    cv2.CHAIN_APPROX_SIMPLE)


        for c in cnts:
    # if the contour is too small, ignore it

            if cv2.contourArea(c) < args["min_area"]:
                continue
            
            (x, y, w, h) = cv2.boundingRect(c)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            text = "Motion Detected.."
            cv2.putText(frame, "RoomStatus: {}".format(text), (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

            cv2.putText(frame, datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S%p"),
            (10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255),
        1)

            imgName = str(uuid.uuid4())
            imgPath = "./captured images/"+imgName+".jpg"
            cv2.imshow("Security Feed", frame) 
            cv2.imwrite(imgPath, frame)

            if connect(): # check if the rapsberry is connectd to internet or not
                #sendAlertEmail(imgPath)
                print("System is in Sleep")
                time.sleep(60)
        key = cv2.waitKey(1) & 0xFF
                            
        if key== ord("q"):
            break

        cv2.destroyAllWindows()
        