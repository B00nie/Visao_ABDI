from ultralytics import YOLO
import cv2
import numpy as np


class Detector:
    def __init__(self, model_path="yolov8n.pt", conf_threshold: float = 0.25, img_size: tuple = None):
        self.model = YOLO(model_path)
        self.conf_threshold = conf_threshold
        self.img_size = img_size

    def detectar(self, frame):
        try:
            img = frame
            if self.img_size is not None:
                img = cv2.resize(img, self.img_size)

            # Ultralytics expects RGB images
            img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

            results = self.model(img_rgb)

            detections = []

            for r in results:
                for box in r.boxes:
                    conf = float(box.conf[0]) if hasattr(box, 'conf') else 1.0
                    if conf < self.conf_threshold:
                        continue

                    classe_id = int(box.cls[0])
                    classe_nome = self.model.names.get(classe_id, str(classe_id))

                    bbox = [float(x) for x in box.xyxy[0].tolist()]

                    detections.append({
                        "classe": classe_nome,
                        "bbox": bbox,
                        "conf": conf,
                    })

            return detections

        except Exception:
            return []