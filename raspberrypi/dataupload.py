# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 04:43:35 2022

@author: Alice
"""

import time
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("firebase_credentials.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

model_collection_name = "emotions"


def upload_model_emotion(emotion):
    doc_title = str(int(time.time()))
    data = {"timestamp": doc_title,
            "emotion": emotion}
    db.collection(model_collection_name).document(doc_title).set(data)
