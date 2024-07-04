import cv2
from ultralytics import YOLO


class People:
    def __init__(self):
        self.model = YOLO('yolov8n.pt')
        self.cap = cv2.VideoCapture(0)
    
    def get_count(self):
        ret, frame = self.cap.read()
        if not ret :
            return None
        results = self.model.predict(frame, conf = 0.5)
        result = results[0]
        person_count = 0
        for box in result.boxes :
            if box.cls == 0 :
                person_count += 1

        result = f"Person Count : {person_count}"
        return person_count
    




