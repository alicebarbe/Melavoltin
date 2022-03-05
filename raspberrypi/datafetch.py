import time
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("../firebase_credentials.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

model_collection_name = "biometric_data"


def get_data():
    data_ref = db.collection(model_collection_name).order_by(
        'timestamp', direction=firestore.Query.DESCENDING).limit(1)
    docs = data_ref.stream()

    for doc in docs:
        latest_data = doc.to_dict()
        print(latest_data)
