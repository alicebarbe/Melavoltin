import pyrebase

config = {
  "apiKey": "AIzaSyCD7-h-8fpIZJUqNz_RddVG6bgg9F_BmkM",
  "authDomain": "melavoltin.firebaseapp.com",
  "projectId": "melavoltin",
  "storageBucket": "melavoltin.appspot.com",
  "databaseURL": "https://melavoltin-default-rtdb.europe-west1.firebasedatabase.app/",
  "serviceAccount": "../firebase_credentials.json"
}



firebase = pyrebase.initialize_app(config)

db = firebase.database()


def stream_handler(message):
    print(message["event"]) # put
    print(message["path"]) # /-K7yGTTEp7O549EzTYtI
    print(message["data"]) # {'title': 'Pyrebase', "body": "etc..."}

my_stream = db.child("Test").stream(stream_handler)


all_users = db.child("Test").get()
print(all_users.val())

while True:
    pass
