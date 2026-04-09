from ultralytics import YOLO

class Detector:
    def __init__(self, model_path="yolov8n.pt"):
        self.model = YOLO(model_path)

    def detectar(self, frame):
        results = self.model(frame)

        detections = []

        for r in results:
            for box in r.boxes:
                classe_id = int(box.cls[0])
                classe_nome = self.model.names[classe_id]

                detections.append({
                    "classe": classe_nome,
                    "bbox": box.xyxy[0].tolist()
                })

        return detections