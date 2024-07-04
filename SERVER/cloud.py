import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from datetime import datetime

class FBDB:
    def __init__(self, path_to_service_key='optiawake-firebase-adminsdk-7afg6-097b204a01.json', databaseURL='https://optiawake-default-rtdb.firebaseio.com/'):
        if not firebase_admin._apps:
            cred = credentials.Certificate(path_to_service_key)
            firebase_admin.initialize_app(cred, {
                'databaseURL': databaseURL
            })
        self.ref = db.reference()

    def push(self, path="status", value=None):
        if value is None:
            current_time = datetime.now().strftime("%I:%M:%S %p")
            value = {
                'time': current_time,
                'temp_value': "NULL",
                'fan_speed': "NULL",
                'people_count': "NULL"
            }
        self.ref.child(path).push(value)

    def get(self, path="status"):
        return self.ref.child(path).get()

    def update(self, path, value):
        self.ref.child(path).update(value)

    def delete(self, path):
        self.ref.child(path).delete()
