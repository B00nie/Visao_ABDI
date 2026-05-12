import argparse
import cv2
from detector import Detector
from especialista import avaliar_epi


def parse_args():
    p = argparse.ArgumentParser(description="Detecção de EPIs em tempo real")
    p.add_argument("--model", default="yolov8n.pt", help="caminho para o modelo YOLO")
    p.add_argument("--camera", type=int, default=0, help="ID da câmera (padrão 0)")
    p.add_argument("--conf", type=float, default=0.25, help="limiar de confiança para detecções")
    p.add_argument("--width", type=int, default=None, help="redimensionar largura (opcional)")
    p.add_argument("--height", type=int, default=None, help="redimensionar altura (opcional)")
    return p.parse_args()


def main():
    args = parse_args()

    img_size = None
    if args.width and args.height:
        img_size = (args.width, args.height)

    detector = Detector(args.model, conf_threshold=args.conf, img_size=img_size)

    cap = cv2.VideoCapture(args.camera)
    if not cap.isOpened():
        print("Erro: não foi possível abrir a câmera.")
        return

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            detections = detector.detectar(frame)

            for d in detections:
                x1, y1, x2, y2 = map(int, d["bbox"])
                classe = d.get("classe", "?")
                conf = d.get("conf", 0.0)

                # cores por classe simples
                if classe == "helmet":
                    color = (0, 200, 0)
                elif classe == "person":
                    color = (255, 0, 0)
                else:
                    color = (200, 200, 0)

                cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
                cv2.putText(frame, f"{classe} {conf:.2f}", (x1, max(15, y1 - 10)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

            status, cor = avaliar_epi(detections)

            cv2.putText(frame, status, (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, cor, 3)

            cv2.imshow("Deteccao de EPIs", frame)

            if cv2.waitKey(1) & 0xFF == 27:
                break

    except KeyboardInterrupt:
        pass

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()