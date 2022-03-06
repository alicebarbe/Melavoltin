
import RPi.GPIO as GPIO
import time
import datetime
import pyrebase

config = {
  "apiKey": "AIzaSyCD7-h-8fpIZJUqNz_RddVG6bgg9F_BmkM",
  "authDomain": "melavoltin.firebaseapp.com",
  "projectId": "melavoltin",
  "storageBucket": "melavoltin.appspot.com",
  "databaseURL": "https://melavoltin-default-rtdb.europe-west1.firebasedatabase.app/",
  "serviceAccount": "../firebase_credentials.json"
}
#wakeup = time.strftime('%H:%M',time.strptime('07:00', '%H:%M'))
wakeup = 700
sleep = 0
firebase = pyrebase.initialize_app(config)

db = firebase.database()
path_init = None

def stream_handler(message):
    #print(message["event"]) # put
    print(message["path"]) # /-K7yGTTEp7O549EzTYtI
    #print(str(message["path"]))
    print(message["data"]) # {'title': 'Pyrebase', "body": "etc..."}

    path = str(message["path"])
    data = str(message["data"])

    if type(message["data"]) is dict:
        print("Found initial dict")
        global wakeup 
        wakeup = int(message["data"]["wakeup"])
    else:
        global path_init
        if path_init == None:
            path_init = path

       


def stream_handler2(message):
    #print(message["event"]) # put
    print(message["path"]) # /-K7yGTTEp7O549EzTYtI
    #print(str(message["path"]))
    print(message["data"]) # {'title': 'Pyrebase', "body": "etc..."}

    path = str(message["path"])
    data = str(message["data"])

    if type(message["data"]) is dict:
        print("Found initial dict")
        global sleep 
        sleep = str(message["data"]["SleepyTime"])
    else:
        global path_init
        if path_init == None:
            path_init = path

        #print(path == path_init)

    if sleep == "1":
        kalm_me(50)
        print("Sleepy time go brrrrr")
    elif sleep == "0":
        kalm_me(0)
        print("You should be asleep now")
    else:
            #global wakeup
            #wakeup = datetime.datetime.strptime(data, '%H:%M').time()
            #wakeup= time.strftime('%H:%M',time.strptime(data, '%H:%M'))
            #wakeup = int(data)
        pass 



my_stream = db.child("Control").stream(stream_handler,stream_id="wake")

my_stream = db.child("SleepOn").stream(stream_handler2,stream_id="sleep")

GPIO.setmode(GPIO.BCM)

PWM1 = 12
PWM2 = 13
PWM_EN = 19


GPIO.setup(PWM1,GPIO.OUT)
GPIO.setup(PWM2,GPIO.OUT)
GPIO.setup(PWM_EN,GPIO.OUT)
kalm = GPIO.PWM(PWM1,200)
panik = GPIO.PWM(PWM2,5)

kalm.start(0)
panik.start(0)

def kalm_me(dutyCycle):
    GPIO.output(PWM_EN,0)
    kalm.ChangeDutyCycle(dutyCycle)
    time.sleep(0.1)
    GPIO.output(PWM_EN,1)

def panik_me(dutyCycle):
    panik.ChangeDutyCycle(dutyCycle)


try:
    while True:
        now = int(time.strftime("%H%M"))
        print("Alarm: " + str(wakeup) + "          Current: " + str(now))
        time.sleep(5)
        if now == wakeup:
            print("WAKEUP")
            panik_me(50)
        else:
            panik_me(0)
        pass
except KeyboardInterrupt:
    GPIO.cleanup()
