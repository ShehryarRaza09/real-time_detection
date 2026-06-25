import torch
import cv2

class Detector:
    def __init__(self, model_path="lib/best.pt"):
        print("[IGNITE] Loading YOLO model...")

        self.model = torch.hub.load(
            'ultralytics/yolov5',
            'yolov5s',
            pretrained=True
        )

        self.model.conf = 0.45
        self.model.iou = 0.45

        print("[IGNITE] Model loaded successfully")

    def predict(self, frame):
        results = self.model(frame)

        annotated = results.render()[0]  # draw boxes
        return results, annotated