import sys
import time
import cv2
from core.capture import ScreenCapture
from core.detector import Detector

def main():
    print("[IGNITE] Starting real-time detection system...")

    capture = ScreenCapture(region_size=416)
    detector = Detector(model_path="lib/best.pt")

    while True:
        frame = capture.get_frame()

        if frame is None:
            continue

        results, annotated_frame = detector.predict(frame)

        cv2.imshow("Ignite - Detection View", annotated_frame)

        # FPS calculation (safe)
        fps = int(1 / max(time.time() - capture.last_time, 1e-5))
        capture.last_time = time.time()

        cv2.setWindowTitle(
            "Ignite - Detection View",
            f"Ignite | FPS: {fps}"
        )

        # ✅ MUST be inside loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()