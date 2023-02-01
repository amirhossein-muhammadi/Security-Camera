import os
from email.message import EmailMessage
import ssl
import smtplib
import imghdr
import time
import urllib.request

#connect function check the situation of internet connection
def connect(host='http://google.com'):
    try:
        urllib.request.urlopen(host) #Python 3.x
        return True
    except:
        return False

#this function Send an Alert by Email , the image must be set by the path of image
def sendAlertEmail(image,email_sender = "***********",
            e_pass = "********",

             email_rec = "*********") :

    


    body = """
    Your secure camera recived some unsual movement in your room please check the Attachment
    """

    em = EmailMessage()

    em['From'] =email_sender
    em['To'] = email_rec

    em["Subject"] = "Security System Alert"

    em.set_content(body)

    context = ssl.create_default_context()

    with open(image, 'rb') as f:
        image_data = f.read()
        image_type = imghdr.what(f.name)
        image_name = f.name
    em.add_attachment(image_data, maintype='image', subtype=image_type, filename=image_name)


    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context= context) as smtp:
        smtp.login(email_sender, e_pass)
        #smtp.sendmail(email_sender, email_rec, em)
        while(connect()==False):
            print("No Internet connection: waiting for 30 second")

        else:
            smtp.send_message(em)
        
        
