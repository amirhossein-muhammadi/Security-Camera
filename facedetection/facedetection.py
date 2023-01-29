import cv2

face_cascade = cv2.CascadeClassifier()
eyes_cascade = cv2.CascadeClassifier()
face_cascade.load('haarcascade_frontalface_alt.xml')
eyes_cascade.load('haarcascade_eye.xml')

def detectAndDisplay(frame):
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame_gray = cv2.equalizeHist(frame_gray)
    faces = face_cascade.detectMultiScale(frame_gray)
    # if len(faces) > 0:
        # do something
    # else:
        # nothing
    for (x,y,w,h) in faces:
        
        center = (x + w//2, y + h//2)
        frame = cv2.ellipse(frame, center, (w//2, h//2), 0, 0, 360, (255, 0, 255), 4)
        faceROI = frame_gray[y:y+h,x:x+w]
        #-- In each face, detect eyes
        # eyes = eyes_cascade.detectMultiScale(faceROI)
        # for (x2,y2,w2,h2) in eyes:
        #     eye_center = (x + x2 + w2//2, y + y2 + h2//2)
        #     radius = int(round((w2 + h2)*0.25))
        #     frame = cv2.circle(frame, eye_center, radius, (255, 0, 0 ), 4)
    cv2.imshow('Face detection', frame)

try:
    
    # cap = cv2.VideoCapture(0)
    cap = cv2.VideoCapture('http://192.168.1.38:4747/video/')
    cap.set(cv2.CAP_PROP_FPS,1)

    if not cap.isOpened:
        print('--(!)Error opening video capture')
        exit(0)
    while True:
        # cv2.waitKey(100)
        cap.set(cv2.CAP_PROP_FPS,1) 
        ret, frame = cap.read()
        if frame is None:
            print('--(!) No captured frame -- Break!')
            break
        cv2.imshow('Face detection', frame)
        detectAndDisplay(frame)
        if cv2.waitKey(1) == 27:
            cap.release()
            cv2.destroyAllWindows() 
            break
except KeyboardInterrupt:
    cap.release()
    cv2.destroyAllWindows() 
finally:
    cap.release()
    cv2.destroyAllWindows() 