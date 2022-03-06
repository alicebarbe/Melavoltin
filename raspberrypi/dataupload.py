# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 04:43:35 2022

@author: Alice
"""

import time
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("../firebase_credentials.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

collection_name = "biometric_data"


def upload_data(data_input):
    doc_title = str(int(time.time()))
    data = {"timestamp": doc_title}
    data = {**data, **data_input}
    db.collection(collection_name).document(doc_title).set(data)
