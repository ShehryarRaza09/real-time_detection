import cv2
import time

class ScreenCapture:
    def __init__(self, region_size=416):
        self.cap = cv2.VideoCapture(0)  # 0 = front camera
        self.last_time = time.time()

        if not self.cap.isOpened():
            print("[IGNITE] ERROR: Camera not found")

    def get_frame(self):
        ret, frame = self.cap.read()

        if not ret:
            print("[IGNITE] Failed to read camera frame")
            return None

        return frame