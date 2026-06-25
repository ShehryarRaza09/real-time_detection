import torch

def train():
    print("[IGNITE] Starting training...")

    model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

    # Replace with your dataset path
    data_path = "data.yaml"

    model.train(
        data=data_path,
        epochs=50,
        imgsz=640
    )

if __name__ == "__main__":
    train()