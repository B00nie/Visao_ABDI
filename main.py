import cv2
from detector import Detector
from especialista import avaliar_epi

detector = Detector("yolov8n.pt")

cap = cv2.VideoCapture(0)  # webcam

while True:
    ret, frame = cap.read()
    if not ret:
        break

    detections = detector.detectar(frame)

    # Desenhar bounding boxes
    for d in detections:
        x1, y1, x2, y2 = map(int, d["bbox"])
        classe = d["classe"]

        cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)
        cv2.putText(frame, classe, (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

    # Sistema especialista
    status, cor = avaliar_epi(detections)

    cv2.putText(frame, status, (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1, cor, 3)

    cv2.imshow("Deteccao de EPIs", frame)

    if cv2.waitKey(1) & 0xFF == 27:  # ESC pra sair
        break

cap.release()
cv2.destroyAllWindows()